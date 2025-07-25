from pydantic import BaseModel

class Rule(BaseModel):
    nome: str
    descricao: str 