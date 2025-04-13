from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import os
import time

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class ScriptRequest(BaseModel):
    language: str
    code: str

@app.post("/generate")
def generate_script(data: ScriptRequest):
    print("📥 /generate endpoint called")

    # Create a unique output directory for this run
    run_id = str(uuid.uuid4())
    output_dir = f"outputs/{run_id}"
    os.makedirs(output_dir, exist_ok=True)

    # Determine file extension
    if data.language.lower() == "python":
        extension = "py"
    elif data.language.lower() == "r":
        extension = "R"
    else:
        raise HTTPException(status_code=400, detail="Invalid language")

    # Write script to file
    script_path = f"{output_dir}/script.{extension}"
    with open(script_path, "w") as f:
        f.write(data.code)

    print(f"📄 Script written to {script_path}")
    print(f"📂 OUTPUT_DIR set to {output_dir}")

    try:
        if data.language.lower() == "python":
            # Inject OUTPUT_DIR into the Python environment
            code = open(script_path).read()
            code = f"OUTPUT_DIR = '{output_dir}'\n" + code
            exec(code, {"__name__": "__main__"})

            # Return files immediately for Python
            files = [f for f in os.listdir(output_dir) if os.path.isfile(os.path.join(output_dir, f))]
            print("📦 Returning files (Python):", files)
            return {"id": run_id, "files": files}

        elif data.language.lower() == "r":
            # Let watcher.R pick it up — wait for output
            timeout = 50  # seconds
            interval = 0.5
            elapsed = 0
            found=False
            while elapsed < timeout:
                current_files = os.listdir(output_dir)
                if any(f.endswith(".png") or f.endswith(".html") for f in current_files):
                    found = True
                    print("⏳ Visualization file detected...")
                    time.sleep(0.5)  # small buffer for file write to complete
                    break
                time.sleep(interval)
                elapsed += interval
            if not found:
                raise HTTPException(status_code=500, detail="Timed out waiting for R output.")


            # ✅ Fetch files after they're likely generated
            files = [f for f in os.listdir(output_dir) if os.path.isfile(os.path.join(output_dir, f))]
            print("📦 Returning files (R):", files)
            return {"id": run_id, "files": files}

        print("✅ Script execution completed or delegated")
    except Exception as e:
        print("❌ Script execution failed:", str(e))
        raise HTTPException(status_code=500, detail=f"Script failed: {str(e)}")

# Serve outputs statically
from fastapi.staticfiles import StaticFiles
app.mount("/outputs", StaticFiles(directory="outputs"), name="outputs")
