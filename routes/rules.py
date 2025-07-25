from fastapi import APIRouter, Query
from typing import List, Optional
import json
from models.rule import Rule

router = APIRouter()

with open('data/rules.json', encoding='utf-8') as f:
    rules_data = json.load(f)

with open('data/combat_rules.json', encoding='utf-8') as f:
    combat_rules_data = json.load(f)

@router.get('/rules', response_model=List[Rule], tags=["Regras"], summary="Listar regras gerais", description="Retorna uma lista de regras gerais aplicáveis a testes, CD, vantagem/desvantagem, passivo, ajuda, etc.")
def list_rules(type: Optional[str] = Query(None, description="Filtrar por tipo de regra, ex: exaustao, percepcao")):
    results = rules_data
    if type:
        results = [r for r in results if type.lower() in r['nome'].lower()]
    return results 

@router.get('/rules/combat', tags=["Regras de Combate"], summary="Listar regras de combate", description="Retorna uma lista de regras específicas de combate. Permite filtrar por tipo.")
def list_combat_rules(type: Optional[str] = Query(None, description="Filtrar por tipo de regra, ex: iniciativa, rodada, dano")):
    results = combat_rules_data
    if type:
        results = [r for r in results if type.lower() in r['tipo'].lower()]
    return results 