from pydantic import Field, ConfigDict
from models.item import ItemBase
from typing import List

class Weapon(ItemBase):
    """Modelo de arma, incluindo dano, tipo, propriedades e categoria."""
    dano: str = Field(..., description="Dano causado pela arma (ex: 1d8).")
    tipo: str = Field(..., description="Tipo de dano (ex: corte, perfurante, concussão).")
    propriedades: List[str] = Field(..., description="Propriedades especiais da arma.")
    categoria: str = Field(..., description="Categoria da arma (simples, marcial).")

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "nome": "Espada Curta",
            "custo": "10 PO",
            "peso": 0.9,
            "descricao": "Uma lâmina curta e leve, ideal para ataques rápidos e precisos.",
            "dano": "1d6",
            "tipo": "Perfurante",
            "propriedades": ["Acuidade", "Leve"],
            "categoria": "Simples"
        }
    }) 