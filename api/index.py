from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(
    title="Suno API Vercel",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Definimos la estructura de los datos que va a recibir el POST
class SongRequest(BaseModel):
    title: str = "Mi gran canción"
    style: str = "Rock melódico 80s"
    prompt: str = "Una letra sobre misterios y tecnología"

@app.get("/")
@app.get("/api/index")
def root():
    return {"status": "ONLINE_DIAGNOSTIC_OK", "docs": "/docs"}

@app.post("/api/custom_generate")
async def generate_song(body: SongRequest):
    return JSONResponse({
        "status": "success",
        "message": "Solicitud lista para enviar a Suno",
        "data_received": {
            "title": body.title,
            "style": body.style,
            "prompt": body.prompt
        }
    })
