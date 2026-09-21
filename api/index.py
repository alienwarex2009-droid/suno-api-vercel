from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import httpx

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
        body = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON payload")

    prompt = body.get("prompt")
    tags = body.get("style")
    title = body.get("title")
    
    if not prompt or not tags:
        raise HTTPException(status_code=400, detail="Faltan los campos 'prompt' (letra/descripción) y 'style' (estilo).")

    # Aquí integrarás la llamada al servicio o API de Suno mediante httpx
    # Ejemplo conceptual:
    # async with httpx.AsyncClient() as client:
    #     response = await client.post("URL_DE_SUNO_O_WRAPPER", json={...})
    
    return JSONResponse({
        "status": "success",
        "message": "Solicitud lista para enviar a Suno",
        "data_received": {
            "title": title,
            "style": tags,
            "prompt": prompt
        }
    })
