from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Suno API Vercel",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")
@app.get("/api/index")
def root():
    return {"status": "ONLINE_DIAGNOSTIC_OK", "docs": "/docs"}

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
