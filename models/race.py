from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Dict

class SubRace(BaseModel):
    """Sub-raça de uma raça de D&D 5e."""
    nome: str = Field(..., description="Nome da sub-raça.", examples=["Elfo da Floresta"])
    bonus_habilidade: Optional[str] = Field(None, description="Bônus de habilidade da sub-raça.", examples=["+1 Sabedoria"])
    caracteristicas: Optional[List[str]] = Field(None, description="Características especiais da sub-raça.", examples=[["Deslocamento 10,5 m", "Pode se esconder com cobertura natural"]])
    descricao: Optional[str] = Field(None, description="Descrição adicional da sub-raça.", examples=["Elfos da floresta são ágeis e possuem forte ligação com a natureza."])

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "nome": "Elfo da Floresta",
            "bonus_habilidade": "+1 Sabedoria",
            "caracteristicas": [
                "Deslocamento 10,5 m",
                "Pode se esconder com cobertura natural",
                "Proficiência com armas élficas"
            ],
            "descricao": "Elfos da floresta são ágeis e possuem forte ligação com a natureza."
        }
    })

class Race(BaseModel):
    """Modelo de Raça de D&D 5e."""
    id: int = Field(..., description="Identificador único da raça.", examples=[1])
    nome: str = Field(..., description="Nome da raça.", examples=["Elfo"])
    aumento_habilidade: str = Field(..., description="Aumento no valor de habilidade da raça.", examples=["+2 Destreza"])
    idade: str = Field(..., description="Descrição da idade típica da raça.", examples=["Adultos aos 100 anos, vivem até 750 anos"])
    alinhamento: str = Field(..., description="Tendência de alinhamento da raça.", examples=["Tendem ao Caótico"])
    tamanho: str = Field(..., description="Descrição do tamanho da raça.", examples=["Médio, entre 1,50 m e 1,80 m"])
    deslocamento: str = Field(..., description="Deslocamento base da raça em metros.", examples=["9 m"])
    visao_no_escuro: Optional[str] = Field(None, description="Alcance de visão no escuro, se aplicável.", examples=["18 m"])
    proficiencias: Optional[List[str]] = Field(None, description="Lista de proficiências concedidas pela raça.", examples=[["Percepção"]])
    resiliencia: Optional[str] = Field(None, description="Resiliência especial da raça, se houver.", examples=["Vantagem contra veneno e resistência a dano de veneno"])
    outras_caracteristicas: Optional[List[str]] = Field(None, description="Outras características especiais da raça.", examples=[["Vantagem contra encantamento; imune a sono mágico"]])
    idiomas: List[str] = Field(..., description="Idiomas conhecidos pela raça.", examples=[["Comum", "Élfico"]])
    subracas: Optional[List[SubRace]] = Field(None, description="Lista de sub-raças disponíveis para a raça.")

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "id": 2,
            "nome": "Elfo",
            "aumento_habilidade": "+2 Destreza",
            "idade": "Adultos aos 100 anos, vivem até 750 anos",
            "alinhamento": "Tendem ao Caótico",
            "tamanho": "Médio, entre 1,50 m e 1,80 m",
            "deslocamento": "9 m",
            "visao_no_escuro": "18 m",
            "proficiencias": ["Percepção"],
            "outras_caracteristicas": [
                "Vantagem contra encantamento; imune a sono mágico",
                "4 horas de meditação substituem 8 horas de sono"
            ],
            "idiomas": ["Comum", "Élfico"],
            "subracas": [
                {
                    "nome": "Alto Elfo",
                    "bonus_habilidade": "+1 Inteligência",
                    "caracteristicas": [
                        "Sabe um truque de mago",
                        "Idioma extra",
                        "Proficiência com espada longa, espada curta, arco curto e arco longo"
                    ],
                    "descricao": None
                }
            ]
        }
    }) 