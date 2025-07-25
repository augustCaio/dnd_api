from fastapi import APIRouter, HTTPException
from typing import List
import json
from models.item import ItemBase

router = APIRouter()

with open('data/equipment.json', encoding='utf-8') as f:
    equipment_data = json.load(f)

def get_equipment_by_id(idx: int):
    if 0 <= idx < len(equipment_data):
        return equipment_data[idx]
    return None

@router.get('/equipment', response_model=List[ItemBase], tags=["Equipamentos"], summary="Listar todos os equipamentos", description="Retorna uma lista de todos os equipamentos de aventura disponíveis.")
def list_equipment():
    """Lista todos os equipamentos de aventura do PHB."""
    return equipment_data

@router.get('/equipment/{id}', response_model=ItemBase, tags=["Equipamentos"], summary="Detalhes de um equipamento", description="Retorna os detalhes de um equipamento específico pelo índice.")
def get_equipment(id: int):
    """Detalhes de um equipamento de aventura pelo índice."""
    item = get_equipment_by_id(id)
    if not item:
        raise HTTPException(status_code=404, detail='Equipamento não encontrado')
    return item 