from pydantic import BaseModel

class Persona(BaseModel):
    cedula: str
    nombre: str

class ErrorResponse(BaseModel):
    error: str
    detalle: str