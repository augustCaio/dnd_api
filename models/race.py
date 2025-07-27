from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class SubRace(BaseModel):
    """Sub-raça de uma raça de D&D 5e."""
    nome: str = Field(..., description="Nome da sub-raça.")
    bonus_habilidade: Optional[str] = Field(None, description="Bônus de habilidade da sub-raça.")
    caracteristicas: Optional[List[str]] = Field(None, description="Características especiais da sub-raça.")
    descricao: Optional[str] = Field(None, description="Descrição adicional da sub-raça.")
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nome": "Elfo da Floresta",
                    "bonus_habilidade": "+1 Sabedoria",
                    "caracteristicas": [
                        "Deslocamento 10,5 m",
                        "Pode se esconder com cobertura natural",
                        "Proficiência com armas élficas"
                    ],
                    "descricao": "Elfos da floresta são ágeis e possuem forte ligação com a natureza."
                }
            ]
        }
    }

class Race(BaseModel):
    """Modelo de Raça de D&D 5e."""
    id: int = Field(..., description="Identificador único da raça.")
    nome: str = Field(..., description="Nome da raça.")
    aumento_habilidade: str = Field(..., description="Aumento no valor de habilidade da raça.")
    idade: str = Field(..., description="Descrição da idade típica da raça.")
    alinhamento: str = Field(..., description="Tendência de alinhamento da raça.")
    tamanho: str = Field(..., description="Descrição do tamanho da raça.")
    deslocamento: str = Field(..., description="Deslocamento base da raça em metros.")
    visao_no_escuro: Optional[str] = Field(None, description="Alcance de visão no escuro, se aplicável.")
    proficiencias: Optional[List[str]] = Field(None, description="Lista de proficiências concedidas pela raça.")
    resiliencia: Optional[str] = Field(None, description="Resiliência especial da raça, se houver.")
    outras_caracteristicas: Optional[List[str]] = Field(None, description="Outras características especiais da raça.")
    idiomas: List[str] = Field(..., description="Idiomas conhecidos pela raça.")
    subracas: Optional[List[SubRace]] = Field(None, description="Lista de sub-raças disponíveis para a raça.")
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
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
            ]
        }
    } 