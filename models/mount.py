from pydantic import Field, ConfigDict
from models.item import ItemBase

class Mount(ItemBase):
    """Modelo de montaria ou veículo, incluindo velocidade, capacidade e tipo."""
    velocidade: str = Field(..., description="Velocidade da montaria ou veículo.")
    capacidade: str = Field(..., description="Capacidade de carga.")
    tipo: str = Field(..., description="Tipo de montaria ou veículo.")

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "nome": "Cavalo",
            "custo": "75 PO",
            "peso": 400.0,
            "descricao": "Cavalo treinado para transporte de pessoas e cargas leves.",
            "velocidade": "60 ft.",
            "capacidade": "240 kg",
            "tipo": "Montaria"
        }
    }) 