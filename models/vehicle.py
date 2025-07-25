from pydantic import Field
from models.item import ItemBase

class Vehicle(ItemBase):
    """Veículo: inclui velocidade, capacidade e tipo."""
    velocidade: str = Field(..., description="Velocidade do veículo.")
    capacidade: str = Field(..., description="Capacidade de carga do veículo.")
    tipo: str = Field(..., description="Tipo de veículo (terrestre, aquático, etc).") 