from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

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
