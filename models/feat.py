from typing import Optional, List, Dict
from pydantic import BaseModel

class Feat(BaseModel):
    nome: str
    requisitos: Optional[Dict[str, str]] = None  # Exemplo: {'nível': '4', 'raça': 'Humano', 'classe': 'Guerreiro'}
    efeito: str
    fonte: str  # Exemplo: 'PHB' 