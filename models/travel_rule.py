from pydantic import BaseModel
from typing import Optional, Dict

class TravelRule(BaseModel):
    nome: str
    descricao: str
    ritmo: Optional[str] = None  # lento, normal, rápido
    distancia_por_hora: Optional[float] = None
    distancia_por_dia: Optional[float] = None
    penalidades: Optional[str] = None
    beneficios: Optional[str] = None
    parametros: Optional[Dict[str, str]] = None 