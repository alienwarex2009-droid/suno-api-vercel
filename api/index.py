from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI(title="Warex Music API", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        # URL de la API de Suno (reemplázala por tu endpoint o wrapper oficial/privado si cambia)
        SUNO_API_URL = "https://suno-api-vercel-sepia.vercel.app/api/custom_generate"
        
        # Estructura del payload que espera el servicio de Suno
        payload = {
            "prompt": song.prompt,
            "tags": song.style,
            "title": song.title,
            "make_instrumental": False
        }
        
        # Petición al servicio de generación
        response = requests.post(SUNO_API_URL, json=payload, timeout=60)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code, 
                detail=f"Error en el servicio de Suno: {response.text}"
            )
            
        result_data = response.json()
        
        # Retornamos la respuesta limpia hacia tu página web
        return {
            "success": True,
            "message": "Petición procesada por Suno exitosamente",
            "data": result_data
        }
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error de conexión con Suno: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
