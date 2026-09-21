from fastapi import FastAPI

app = FastAPI()

@app.get("/")
@app.get("/api/index")
def root():
    return {"status": "ONLINE_DIAGNOSTIC_OK"}
