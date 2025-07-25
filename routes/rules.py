from fastapi import APIRouter
from typing import List, Optional
import json
from models.rule import Rule
from fastapi import Query

router = APIRouter()

with open('data/rules.json', encoding='utf-8') as f:
    rules_data = json.load(f)

@router.get('/rules', response_model=List[Rule], tags=["Regras"], summary="Listar regras gerais", description="Retorna uma lista de regras gerais aplicáveis a testes, CD, vantagem/desvantagem, passivo, ajuda, etc.")
def list_rules(type: Optional[str] = Query(None, description="Filtrar por tipo de regra, ex: exaustao, percepcao")):
    results = rules_data
    if type:
        results = [r for r in results if type.lower() in r['nome'].lower()]
    return results 