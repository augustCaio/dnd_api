from pydantic import BaseModel
from typing import Optional, List, Dict

class EnvironmentCondition(BaseModel):
    nome: str
    tipo: Optional[str] = None  # visibilidade, clima, obstáculo, etc.
    descricao: str
    efeitos: Optional[List[str]] = None
    parametros: Optional[Dict[str, str]] = None 