from pydantic import BaseModel, Field
from typing import List, Optional

class Deus(BaseModel):
    id: str = Field(..., description="Identificador único da divindade")
    nome: str = Field(..., description="Nome da divindade")
    titulo: Optional[str] = Field(None, description="Título ou epíteto da divindade")
    panteao: str = Field(..., description="Panteão ao qual a divindade pertence")
    alinhamento: str = Field(..., description="Alinhamento da divindade (formato abreviado)")
    dominios: List[str] = Field(..., description="Lista de domínios divinos")
    simbolo: Optional[str] = Field(None, description="Símbolo sagrado da divindade")
    plano: Optional[str] = Field(None, description="Plano de existência da divindade")
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "lathander",
                    "nome": "Lathander",
                    "titulo": "O Senhor da Aurora",
                    "panteao": "Faerûniano",
                    "alinhamento": "NB",
                    "dominios": ["Vida", "Luz", "Nascimento"],
                    "simbolo": "Círculo de luz dourada",
                    "plano": "Plano Material"
                },
                {
                    "id": "mystra",
                    "nome": "Mystra",
                    "titulo": "A Senhora dos Mistérios",
                    "panteao": "Faerûniano",
                    "alinhamento": "NM",
                    "dominios": ["Magia", "Conhecimento", "Arcanos"],
                    "simbolo": "Círculo de sete estrelas",
                    "plano": "Plano Material"
                }
            ]
        }
    } 