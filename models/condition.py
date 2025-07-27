from pydantic import BaseModel, Field
from typing import List, Optional

class Condition(BaseModel):
    nome: str = Field(..., description="Nome da condição")
    descricao: str = Field(..., description="Descrição detalhada da condição")
    efeitos: List[str] = Field(..., description="Lista de efeitos mecânicos da condição")
    interacoes: Optional[List[str]] = Field(None, description="Como a condição interage com outras regras ou condições")
    fontes_comuns: Optional[List[str]] = Field(None, description="Fontes comuns que causam esta condição")
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nome": "Enfeitiçado",
                    "descricao": "Uma criatura enfeitiçada não pode atacar o conjurador ou escolher o conjurador como alvo de uma habilidade ou magia prejudicial.",
                    "efeitos": ["Não pode atacar o conjurador", "Não pode escolher o conjurador como alvo de habilidades prejudiciais"],
                    "interacoes": ["Pode ser removida com Remove Maldição", "Não afeta criaturas imunes a encantamento"],
                    "fontes_comuns": ["Charme Pessoa", "Dominação", "Sussurro"]
                }
            ]
        }
    } 