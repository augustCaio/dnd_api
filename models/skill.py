from pydantic import BaseModel

class Skill(BaseModel):
    nome: str
    habilidade_associada: str
    descricao: str 