from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import uuid
import os

app = FastAPI()

class ScriptRequest(BaseModel):
    language: str
    code: str

@app.post("/generate")
def generate_script(data: ScriptRequest):
    run_id = str(uuid.uuid4())
    output_dir = f"outputs/{run_id}"
    os.makedirs(output_dir, exist_ok=True)

    if data.language.lower() == "python":
        docker_image = "languageagnosticwebapp-python-runner"
        extension = "py"
    elif data.language.lower() == "r":
        docker_image = "languageagnosticwebapp-r-runner"
        extension = "R"
    else:
        raise HTTPException(status_code=400, detail="Invalid language")

    script_path = f"{output_dir}/script.{extension}"
    with open(script_path, "w") as f:
        f.write(data.code)

    try:
        subprocess.run([
            "docker", "run", "--rm",
            "-v", f"{os.getcwd()}/{output_dir}:/app/output",
            docker_image
        ], check=True)
    except subprocess.CalledProcessError:
        raise HTTPException(status_code=500, detail="Script execution failed")

    files = os.listdir(output_dir)
    return {"id": run_id, "files": files}
