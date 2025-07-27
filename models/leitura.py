from pydantic import BaseModel, Field
from typing import Optional

class LeituraInspiradora(BaseModel):
    """Modelo para leituras inspiradoras que influenciaram D&D."""
    id: str = Field(..., description="Identificador único da leitura (slug)")
    titulo: str = Field(..., description="Título da obra")
    autor: str = Field(..., description="Autor da obra")
    categoria: str = Field(..., description="Categoria da obra (Ficção, Fantasia, Mitologia, Terror, etc.)")
    descricao: Optional[str] = Field(None, description="Descrição da obra e sua importância")
    influencia: Optional[str] = Field(None, description="Como a obra influenciou D&D ou outros jogos")
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "senhor-dos-aneis",
                    "titulo": "O Senhor dos Anéis",
                    "autor": "J.R.R. Tolkien",
                    "categoria": "Fantasia",
                    "descricao": "Trilogia épica que estabeleceu muitos dos fundamentos da fantasia moderna, incluindo raças como elfos, anões e hobbits.",
                    "influencia": "Inspirou diretamente as raças e o mundo de D&D, especialmente os elfos e anões. Influenciou o conceito de magia e aventura épica."
                },
                {
                    "id": "conan-o-barbaro",
                    "titulo": "Conan, o Bárbaro",
                    "autor": "Robert E. Howard",
                    "categoria": "Espada e Feitiçaria",
                    "descricao": "Série de contos sobre o guerreiro bárbaro Conan em um mundo de fantasia sombria.",
                    "influencia": "Inspirou a classe Bárbaro e o conceito de mundos de fantasia sombria e brutal."
                }
            ]
        }
    } 