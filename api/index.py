from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI(
    title="Suno API Vercel",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

@app.post("/api/custom_generate")
async def generate_song(request: Request):
    data = await request.json()
    return JSONResponse({
        "status": "success",
        "title": data.get("title"),
        "style": data.get("style"),
        "lyrics": data.get("prompt"),
        "id": "fake_song_id_123"
    })
