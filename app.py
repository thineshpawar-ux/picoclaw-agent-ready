from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Picoclaw running 🚀"}

@app.get("/run")
def run():
    try:
        result = subprocess.run(
            ["./picoclaw", "--help"],
            capture_output=True,
            text=True
        )
        return {"output": result.stdout}
    except Exception as e:
        return {"error": str(e)}
