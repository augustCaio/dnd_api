from fastapi import APIRouter, Query
from typing import List, Optional
import json

router = APIRouter()

with open('data/actions.json', encoding='utf-8') as f:
    actions_data = json.load(f)

@router.get('/actions', tags=["Ações"], summary="Listar todas as ações de combate", description="Retorna uma lista de todas as ações possíveis no combate. Permite filtrar por tipo de ação.")
def list_actions(type: Optional[str] = Query(None, description="Filtrar por tipo de ação, ex: bonus, reação, movimento")):
    results = actions_data
    if type:
        results = [a for a in results if type.lower() in a['tipo'].lower()]
    return results 