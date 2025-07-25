from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
import json
from models.weapon import Weapon

router = APIRouter()

with open('data/weapons.json', encoding='utf-8') as f:
    weapons_data = json.load(f)

def get_weapon_by_id(idx: int):
    if 0 <= idx < len(weapons_data):
        return weapons_data[idx]
    return None

@router.get('/weapons', response_model=List[Weapon], tags=["Armas"], summary="Listar todas as armas", description="Retorna uma lista de todas as armas disponíveis. Permite filtrar por tipo e propriedade.")
def list_weapons(
    type: Optional[str] = Query(None, description="Filtrar por categoria da arma (ex: simples, marcial)"),
    property: Optional[str] = Query(None, description="Filtrar por propriedade da arma (ex: leve, pesada, acuidade)")
):
    """Lista todas as armas do PHB, com filtros opcionais por tipo e propriedade."""
    results = weapons_data
    if type:
        results = [w for w in results if type.lower() in w.get('categoria', '').lower()]
    if property:
        results = [w for w in results if any(property.lower() in p.lower() for p in w.get('propriedades', []))]
    return results

@router.get('/weapons/{id}', response_model=Weapon, tags=["Armas"], summary="Detalhes de uma arma", description="Retorna os detalhes de uma arma específica pelo índice.")
def get_weapon(id: int):
    """Detalhes de uma arma pelo índice."""
    item = get_weapon_by_id(id)
    if not item:
        raise HTTPException(status_code=404, detail='Arma não encontrada')
    return item 