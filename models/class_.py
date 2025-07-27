from pydantic import BaseModel, Field
from typing import List, Optional

class Feature(BaseModel):
    nome: str = Field(..., description="Nome da habilidade.")
    descricao: str = Field(..., description="Descrição da habilidade.")
    nivel: Optional[int] = Field(None, description="Nível em que a habilidade é adquirida.")
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nome": "Fúria",
                    "descricao": "Dano bônus, resistência a dano físico, vantagem em testes de Força.",
                    "nivel": 1
                }
            ]
        }
    }

class ClassLevel(BaseModel):
    nivel: int = Field(..., description="Nível da classe.")
    habilidades: List[Feature] = Field(..., description="Lista de habilidades adquiridas neste nível.")
    magias: Optional[List[str]] = Field(None, description="Magias adquiridas neste nível, se houver.")
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nivel": 1,
                    "habilidades": [
                        {
                            "nome": "Fúria",
                            "descricao": "Dano bônus, resistência a dano físico, vantagem em testes de Força.",
                            "nivel": 1
                        }
                    ],
                    "magias": ["Truques e magias conhecidos aumentam com o nível"]
                }
            ]
        }
    }

class Class(BaseModel):
    nome: str = Field(..., description="Nome da classe.")
    dado_vida: str = Field(..., description="Dado de vida da classe, ex: '1d8'.")
    proficiencias: List[str] = Field(..., description="Lista de proficiências iniciais da classe.")
    equipamentos_iniciais: List[str] = Field(..., description="Equipamentos iniciais da classe.")
    niveis: List[ClassLevel] = Field(..., description="Lista de níveis da classe, com habilidades e magias.")
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nome": "Bárbaro",
                    "dado_vida": "1d12",
                    "proficiencias": [
                        "Armaduras: leves, médias, escudos",
                        "Armas: simples e marciais",
                        "Testes de resistência: Força, Constituição",
                        "Perícias: escolha 2 entre Adestrar Animais, Atletismo, Intimidação, Natureza, Percepção, Sobrevivência"
                    ],
                    "equipamentos_iniciais": [
                        "(a) machado grande ou (b) qualquer arma marcial corpo a corpo",
                        "(a) dois machados de mão ou (b) qualquer arma simples",
                        "Pacote de explorador",
                        "Quatro javalis"
                    ],
                    "niveis": [
                        {
                            "nivel": 1,
                            "habilidades": [
                                {
                                    "nome": "Fúria",
                                    "descricao": "Dano bônus, resistência a dano físico, vantagem em testes de Força.",
                                    "nivel": 1
                                }
                            ],
                            "magias": None
                        }
                    ]
                }
            ]
        }
    } 