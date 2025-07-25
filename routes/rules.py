from fastapi import APIRouter
from typing import List
import json
from models.rule import Rule

router = APIRouter()

with open('data/rules.json', encoding='utf-8') as f:
    rules_data = json.load(f)

@router.get('/rules', response_model=List[Rule], tags=["Regras"], summary="Listar regras gerais", description="Retorna uma lista de regras gerais aplicáveis a testes, CD, vantagem/desvantagem, passivo, ajuda, etc.")
def list_rules():
    return rules_data 