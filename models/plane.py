from pydantic import BaseModel, Field
from typing import Optional, List

class PlanoExistencia(BaseModel):
    """Modelo para planos de existência de D&D 5e."""
    id: str = Field(..., description="Identificador único do plano (slug)")
    nome: str = Field(..., description="Nome do plano de existência")
    tipo: str = Field(..., description="Tipo do plano (Exterior, Interior, Transitivo)")
    descricao: str = Field(..., description="Descrição detalhada do plano")
    alinhamento: Optional[str] = Field(None, description="Alinhamento predominante do plano")
    associado_a: Optional[str] = Field(None, description="Elemento, deus ou energia associada ao plano")
    criaturas_tipicas: Optional[List[str]] = Field(None, description="Lista de criaturas típicas do plano")
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "plano-material",
                    "nome": "Plano Material",
                    "tipo": "Interior",
                    "descricao": "O mundo físico onde a maioria das campanhas se passa. É o plano da realidade normal onde vivem humanos, elfos, anões e outras raças mortais.",
                    "alinhamento": "Neutro",
                    "associado_a": "Realidade Física",
                    "criaturas_tipicas": ["Humanos", "Elfos", "Anões", "Orcs", "Goblins", "Dragões"]
                },
                {
                    "id": "plano-astral",
                    "nome": "Plano Astral",
                    "tipo": "Transitivo",
                    "descricao": "Um reino de pensamento e sonho, onde a consciência pode viajar sem o corpo físico. É usado para viagem entre planos.",
                    "alinhamento": "Neutro",
                    "associado_a": "Consciência",
                    "criaturas_tipicas": ["Githyanki", "Githzerai", "Psicopatas", "Entidades Astrais"]
                },
                {
                    "id": "plano-elemental-fogo",
                    "nome": "Plano Elemental do Fogo",
                    "tipo": "Exterior",
                    "descricao": "Um reino de chamas eternas e calor intenso. Tudo aqui é feito de fogo, desde o solo até o ar.",
                    "alinhamento": "Caótico e Mau",
                    "associado_a": "Elemento Fogo",
                    "criaturas_tipicas": ["Efriti", "Elementais de Fogo", "Salamandras", "Fênix"]
                }
            ]
        }
    } 