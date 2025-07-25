from pydantic import BaseModel
from typing import List, Optional

class Ability(BaseModel):
    nome: str
    descricao: str
    usos: Optional[List[str]] = None
    testes_comuns: Optional[List[str]] = None 