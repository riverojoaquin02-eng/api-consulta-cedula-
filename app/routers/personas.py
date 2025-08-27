from fastapi import APIRouter, HTTPException
from app.models.schemas import Persona, ErrorResponse
from app.services.mongo_repo import get_persona_by_cedula
from app.config import CEDULA_MIN_LENGTH, CEDULA_MAX_LENGTH
import re

router = APIRouter()

@router.get("/personas/{cedula}", response_model=Persona, responses={
    400: {"model": ErrorResponse},
    404: {"model": ErrorResponse},
    500: {"model": ErrorResponse}
})
async def consultar_persona(cedula: str):
    if not cedula or not re.fullmatch(r"[0-9\-]+", cedula):
        raise HTTPException(status_code=400, detail="La cédula debe ser numérica y de longitud 6-15")
    if not (CEDULA_MIN_LENGTH <= len(cedula) <= CEDULA_MAX_LENGTH):
        raise HTTPException(status_code=400, detail="La cédula debe ser numérica y de longitud 6-15")

    persona = await get_persona_by_cedula(cedula)
    if not persona:
        raise HTTPException(status_code=404, detail="No existe registro para la cédula solicitada")

    return Persona(**persona)