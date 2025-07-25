from pydantic import BaseModel
from typing import Optional, Dict

class MovementRule(BaseModel):
    nome: str
    descricao: str
    categoria: Optional[str] = None
    parametros: Optional[Dict[str, str]] = None 