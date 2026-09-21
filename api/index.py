import os
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Suno API Vercel",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 1. Modelo para los datos que RECIBIMOS
class SongRequest(BaseModel):
    title: str = "Mi gran canción"
    style: str = "Rock melódico 80s"
    prompt: str = "Una letra sobre misterios y tecnología"

# 2. Modelo para los datos que DEVOLVEMOS
class SongResponse(BaseModel):
    status: str
    message: str
    suno_response: dict | None = None

@app.get("/")
@app.get("/api/index")
def root():
    return {"status": "ONLINE_DIAGNOSTIC_OK", "docs": "/docs"}

@app.post("/api/custom_generate", response_model=SongResponse)
async def generate_song(body: SongRequest):
    # Aquí definimos la URL del servicio de Suno (puedes cambiarla o usar una variable de entorno)
    SUNO_API_URL = os.getenv("SUNO_API_URL", "https://tu-api-de-suno-endpoint.com/api/custom_generate")
    SUNO_API_KEY = os.getenv("SUNO_API_KEY", "")

    headers = {
        "Content-Type": "application/json",
    }
    if SUNO_API_KEY:
        headers["Authorization"] = f"Bearer {SUNO_API_KEY}"

    payload = {
        "prompt": body.prompt,
        "tags": body.style,
        "title": body.title,
        "wait_audio": False
    }

    # Intentamos conectar con Suno de forma asíncrona
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            # DESCOMENTA esta línea cuando tengas lista la URL real de Suno:
            # response = await client.post(SUNO_API_URL, json=payload, headers=headers)
            # response_data = response.json()
            
            # (Simulación de respuesta exitosa mientras conectas el endpoint definitivo)
            response_data = {"id": "mock-suno-id-12345", "status": "submitted"}

        return {
            "status": "success",
            "message": "Solicitud enviada a Suno correctamente",
            "suno_response": response_data
        }

    except httpx.RequestError as e:
        raise HTTPException(status_code=502, detail=f"Error de comunicación con Suno: {str(e)}")
