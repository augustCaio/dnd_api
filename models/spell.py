from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional

class Spell(BaseModel):
    nome: str = Field(..., description="Nome da magia.", examples=["Bola de Fogo"])
    nivel: int = Field(..., description="Nível da magia (0 para truques).", examples=[3])
    escola: str = Field(..., description="Escola de magia.", examples=["Evocação"])
    tempo_conjuracao: str = Field(..., description="Tempo necessário para conjurar a magia.", examples=["1 ação"])
    alcance: str = Field(..., description="Alcance da magia.", examples=["45 metros"])
    componentes: List[str] = Field(..., description="Componentes necessários: V (verbal), S (somático), M (material).", examples=[["V", "S", "M"]])
    duracao: str = Field(..., description="Duração da magia.", examples=["Instantânea"])
    classes_conjuradoras: List[str] = Field(..., description="Classes que podem conjurar esta magia.", examples=[["Mago", "Feiticeiro"]])
    texto: str = Field(..., description="Texto completo da descrição da magia.")
    ritual: bool = Field(False, description="Se a magia pode ser conjurada como ritual.", examples=[False])
    concentracao: bool = Field(False, description="Se a magia requer concentração.", examples=[True])
    material_especifico: Optional[str] = Field(None, description="Material específico necessário, se houver.", examples=["Um pequeno pedaço de fio de cobre"])

    model_config = ConfigDict(json_schema_extra={
        "example": {
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
    }) 