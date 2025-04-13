import os
import glob

print("📁 Scanning for script.py in subfolders...")

script_paths = glob.glob("/app/output/*/script.py")

for path in script_paths:
    print(f"📄 Found script: {path}")
    try:
        # Inject OUTPUT_DIR into the globals before execution
        folder = os.path.dirname(path)
        with open(path, "r") as f:
            code = f.read()
        exec(code, {"__name__": "__main__", "OUTPUT_DIR": folder})
        print("✅ Script executed.")
    except Exception as e:
        print("❌ Error running script:", str(e))
