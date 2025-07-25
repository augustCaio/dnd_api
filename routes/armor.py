from fastapi import APIRouter, HTTPException
from typing import List
import json
from models.armor import Armor

router = APIRouter()

with open('data/armor.json', encoding='utf-8') as f:
    armor_data = json.load(f)

def get_armor_by_id(idx: int):
    if 0 <= idx < len(armor_data):
        return armor_data[idx]
    return None

@router.get('/armor', response_model=List[Armor], tags=["Armaduras"], summary="Listar todas as armaduras", description="Retorna uma lista de todas as armaduras disponíveis.")
def list_armor():
    """Lista todas as armaduras do PHB."""
    return armor_data

@router.get('/armor/{id}', response_model=Armor, tags=["Armaduras"], summary="Detalhes de uma armadura", description="Retorna os detalhes de uma armadura específica pelo índice.")
def get_armor(id: int):
    """Detalhes de uma armadura pelo índice."""
    item = get_armor_by_id(id)
    if not item:
        raise HTTPException(status_code=404, detail='Armadura não encontrada')
    return item 