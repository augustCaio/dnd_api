from pydantic import BaseModel, Field
from typing import List, Optional

class Spell(BaseModel):
    nome: str = Field(..., description="Nome da magia.")
    nivel: int = Field(..., description="Nível da magia (0 para truques).")
    escola: str = Field(..., description="Escola de magia.")
    tempo_conjuracao: str = Field(..., description="Tempo necessário para conjurar a magia.")
    alcance: str = Field(..., description="Alcance da magia.")
    componentes: List[str] = Field(..., description="Componentes necessários: V (verbal), S (somático), M (material).")
    duracao: str = Field(..., description="Duração da magia.")
    classes_conjuradoras: List[str] = Field(..., description="Classes que podem conjurar esta magia.")
    texto: str = Field(..., description="Texto completo da descrição da magia.")
    ritual: bool = Field(False, description="Se a magia pode ser conjurada como ritual.")
    concentracao: bool = Field(False, description="Se a magia requer concentração.")
    material_especifico: Optional[str] = Field(None, description="Material específico necessário, se houver.")
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nome": "Bola de Fogo",
                    "nivel": 3,
                    "escola": "Evocação",
                    "tempo_conjuracao": "1 ação",
                    "alcance": "45 metros",
                    "componentes": ["V", "S", "M"],
                    "duracao": "Instantânea",
                    "classes_conjuradoras": ["Mago", "Feiticeiro"],
                    "texto": "Uma luz brilhante se forma em seu dedo indicador escolhido...",
                    "ritual": False,
                    "concentracao": False,
                    "material_especifico": "Um pequeno pedaço de fio de cobre"
                }
            ]
        }
    } 