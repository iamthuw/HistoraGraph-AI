from fastapi import FastAPI

app = FastAPI(
    title="HistoraGraph-AI API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "project": "HistoraGraph-AI",
        "status": "running"
    }