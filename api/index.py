from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Suno API Vercel",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")
def read_root():
    return {"message": "Suno API is running successfully!", "docs": "/docs"}

@app.post("/api/custom_generate")
async def generate_song(request: Request):
    try:
        data = await request.json()
    except Exception:
        data = {}
        
    return JSONResponse({
        "status": "success",
        "title": data.get("title", "Unknown"),
        "style": data.get("style", "Unknown"),
        "lyrics": data.get("prompt", "Unknown"),
        "id": "fake_song_id_123"
    })
