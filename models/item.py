from pydantic import BaseModel, Field, ConfigDict

class ItemBase(BaseModel):
    """Modelo base para todos os itens de equipamento, armas, armaduras, ferramentas, montarias e veículos."""
    nome: str = Field(..., description="Nome do item.")
    custo: str = Field(..., description="Custo do item (ex: 10 PO).")
    peso: float = Field(..., description="Peso do item em kg.")
    descricao: str = Field(..., description="Descrição do item.")

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "nome": "Mochila",
            "custo": "2 PO",
            "peso": 2.3,
            "descricao": "Bolsa resistente para carregar equipamentos e suprimentos."
        }
    }) 