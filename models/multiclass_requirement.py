from typing import Dict
from pydantic import BaseModel

class MulticlassRequirement(BaseModel):
    classe_base: str
    classe_desejada: str
    requisitos: Dict[str, int]  # Exemplo: {'Força': 13, 'Destreza': 13} 