from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class Subrace(BaseModel):
    """Sub-raça de uma raça de D&D 5e."""
    nome: str = Field(..., description="Nome da sub-raça.")
    bonus: Optional[str] = Field(None, description="Bônus de atributo da sub-raça.")
    descricao: Optional[str] = Field(None, description="Descrição ou características especiais da sub-raça.")

class Race(BaseModel):
    """Modelo de Raça de D&D 5e."""
    id: int = Field(..., description="Identificador único da raça.")
    nome: str = Field(..., description="Nome da raça.")
    aumento_habilidade: str = Field(..., description="Aumento no valor de habilidade da raça.")
    idade: str = Field(..., description="Descrição da idade típica da raça.")
    alinhamento: str = Field(..., description="Tendência de alinhamento da raça.")
    tamanho: str = Field(..., description="Descrição do tamanho da raça.")
    deslocamento: str = Field(..., description="Deslocamento base da raça em metros.")
    visao_no_escuro: Optional[str] = Field(None, description="Alcance de visão no escuro, se aplicável.")
    proficiencias: Optional[List[str]] = Field(None, description="Lista de proficiências concedidas pela raça.")
    resiliencia: Optional[str] = Field(None, description="Resiliência especial da raça, se houver.")
    outras_caracteristicas: Optional[List[str]] = Field(None, description="Outras características especiais da raça.")
    idiomas: List[str] = Field(..., description="Idiomas conhecidos pela raça.")
    subracas: Optional[List[Subrace]] = Field(None, description="Lista de sub-raças disponíveis para a raça.") 