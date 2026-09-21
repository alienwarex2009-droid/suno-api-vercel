from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests  # O httpx para llamadas asíncronas

app = FastAPI(title="Warex Music API", version="2.0")

# Configuración de CORS para permitir peticiones desde tu web local y tu futuro dominio
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción podés limitar esto a tu dominio final
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de datos que recibe exactamente lo que manda tu formulario HTML
class SongRequest(BaseModel):
    title: str
    style: str
    prompt: str

@app.get("/")
def read_root():
    return {"status": "online", "message": "Warex Music Studio Backend activo"}

@app.post("/api/custom_generate")
async def custom_generate(song: SongRequest):
    try:
        # Aquí es donde en el futuro realizaremos la integración o llamada 
        # hacia la API de generación (Suno u otro wrapper activo) usando los datos:
        # song.title, song.style, song.prompt
        
        # Por ahora, simulamos una respuesta exitosa estructurada para el estudio:
        return {
            "success": True,
            "message": "Parámetros recibidos correctamente en el servidor",
            "data": {
                "title": song.title,
                "style": song.style,
                "prompt_length": len(song.prompt),
                "audio_url": "" # Aquí llegará la URL de la música generada próximamente
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
