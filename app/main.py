from fastapi import FastAPI
from app.routers import personas

app = FastAPI(title="Consulta por Cédula API")

app.include_router(personas.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Consulta por Cédula API"}