from pydantic import BaseModel, Field, ConfigDict
from typing import List

class TraitBlock(BaseModel):
    """Bloco de personalidade contendo traços, ideais, vínculos e defeitos."""
    tracos: List[str] = Field(..., description="Traços de personalidade do personagem.")
    ideais: List[str] = Field(..., description="Ideais que motivam o personagem.")
    vinculos: List[str] = Field(..., description="Vínculos importantes para o personagem.")
    defeitos: List[str] = Field(..., description="Defeitos e fraquezas do personagem.")

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "tracos": ["Sou tolerante com outras religiões.", "Sempre vejo um presságio em cada evento."],
            "ideais": ["Tradição: As antigas tradições devem ser preservadas."],
            "vinculos": ["Fiel a um templo específico."],
            "defeitos": ["Não consigo esconder meu desprezo por outras crenças."]
        }
    })

class HabilidadeEspecial(BaseModel):
    """Habilidade especial concedida pelo antecedente."""
    nome: str = Field(..., description="Nome da habilidade especial.")
    descricao: str = Field(..., description="Descrição detalhada da habilidade especial.")

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "nome": "Abrigo dos Fiéis",
            "descricao": "Você e seus companheiros podem receber cura e abrigo em templos da sua fé."
        }
    })

class Background(BaseModel):
    """Antecedente do personagem, incluindo proficiências, equipamentos e bloco de personalidade."""
    nome: str = Field(..., description="Nome do antecedente.")
    descricao: str = Field(..., description="Descrição do antecedente.")
    proficiencias: List[str] = Field(..., description="Lista de proficiências concedidas pelo antecedente.")
    idiomas: List[str] = Field(..., description="Idiomas concedidos pelo antecedente.")
    equipamentos: List[str] = Field(..., description="Equipamentos iniciais do antecedente.")
    habilidade: HabilidadeEspecial = Field(..., description="Habilidade especial do antecedente.")
    personalidade: TraitBlock = Field(..., description="Bloco de personalidade do antecedente.")

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "nome": "Acólito",
            "descricao": "Você passou sua vida a serviço de um templo específico de um deus ou panteão.",
            "proficiencias": ["Intuição", "Religião"],
            "idiomas": ["2 à sua escolha"],
            "equipamentos": ["Símbolo sagrado", "Livro de orações", "5 varetas de incenso", "Vestes", "Vestes comuns", "15 PO"],
            "habilidade": {
                "nome": "Abrigo dos Fiéis",
                "descricao": "Você e seus companheiros podem receber cura e abrigo em templos da sua fé."
            },
            "personalidade": {
                "tracos": ["Sou tolerante com outras religiões.", "Sempre vejo um presságio em cada evento."],
                "ideais": ["Tradição: As antigas tradições devem ser preservadas."],
                "vinculos": ["Fiel a um templo específico."],
                "defeitos": ["Não consigo esconder meu desprezo por outras crenças."]
            }
        }
    }) 