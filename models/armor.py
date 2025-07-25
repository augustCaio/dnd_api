from pydantic import Field, ConfigDict
from models.item import ItemBase

class Armor(ItemBase):
    """Modelo de armadura, incluindo CA, tipo, força mínima e penalidade de furtividade."""
    ca: int = Field(..., description="Classe de Armadura fornecida.")
    tipo: str = Field(..., description="Tipo de armadura (leve, média, pesada, escudo).")
    forca_minima: int = Field(..., description="Força mínima necessária para usar.")
    penalidade_furtividade: bool = Field(..., description="Se impõe penalidade em testes de furtividade.")

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "nome": "Couro",
            "custo": "10 PO",
            "peso": 2.3,
            "descricao": "Armadura leve feita de couro endurecido, oferece mobilidade e proteção básica.",
            "ca": 11,
            "tipo": "Leve",
            "forca_minima": 0,
            "penalidade_furtividade": False
        }
    }) 