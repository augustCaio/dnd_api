from pydantic import BaseModel
from typing import Optional, Dict

class RestRule(BaseModel):
    nome: str
    descricao: str
    tipo: Optional[str] = None  # curto, longo
    beneficios: Optional[str] = None
    requisitos: Optional[str] = None
    parametros: Optional[Dict[str, str]] = None 