from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Suno API Vercel",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 1. Modelo para los datos que RECIBIMOS (Request)
class SongRequest(BaseModel):
    title: str = "Mi gran canción"
    style: str = "Rock melódico 80s"
    prompt: str = "Una letra sobre misterios y tecnología"

# 2. Modelo para los datos que DEVOLVEMOS (Response)
class SongResponse(BaseModel):
    status: str
    message: str
    data_received: SongRequest

@app.get("/")
@app.get("/api/index")
def root():
    return {"status": "ONLINE_DIAGNOSTIC_OK", "docs": "/docs"}

# Indicamos que este endpoint responde usando el modelo SongResponse
@app.post("/api/custom_generate", response_model=SongResponse)
async def generate_song(body: SongRequest):
    return {
        "status": "success",
        "message": "Solicitud lista para enviar a Suno",
        "data_received": body
    }
