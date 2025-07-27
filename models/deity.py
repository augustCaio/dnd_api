from pydantic import BaseModel, Field
from typing import List, Optional

class Deus(BaseModel):
    id: str = Field(..., description="Identificador único da divindade", example="lathander")
    nome: str = Field(..., description="Nome da divindade", example="Lathander")
    titulo: Optional[str] = Field(None, description="Título ou epíteto da divindade", example="O Senhor da Aurora")
    panteao: str = Field(..., description="Panteão ao qual a divindade pertence", example="Faerûniano")
    alinhamento: str = Field(..., description="Alinhamento da divindade (formato abreviado)", example="NB")
    dominios: List[str] = Field(..., description="Lista de domínios divinos", examples=[["Vida", "Luz", "Nascimento"]])
    simbolo: Optional[str] = Field(None, description="Símbolo sagrado da divindade", example="Círculo de luz dourada")
    plano: Optional[str] = Field(None, description="Plano de existência da divindade", example="Plano Material")
    
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