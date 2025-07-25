from pydantic import Field, ConfigDict
from models.item import ItemBase

class Tool(ItemBase):
    """Modelo de ferramenta, incluindo tipo e uso."""
    tipo: str = Field(..., description="Tipo de ferramenta (ex: kit de ladrão, instrumento musical).")
    uso: str = Field(..., description="Descrição do uso da ferramenta.")

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "nome": "Kit de Disfarce",
            "custo": "25 PO",
            "peso": 2.2,
            "descricao": "Contém tintas, pós, roupas e acessórios para criar disfarces convincentes.",
            "tipo": "Disfarce",
            "uso": "Permite criar disfarces convincentes para enganar outras pessoas."
        }
    }) 