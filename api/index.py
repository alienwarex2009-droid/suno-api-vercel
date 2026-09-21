from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
@app.get("/api/index")
def read_root():
    return {"message": "¡La API de Suno está funcionando correctamente en Vercel!"}

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
