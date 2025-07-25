from fastapi import APIRouter, HTTPException
from typing import List
import json
from models.mount import Mount

router = APIRouter()

with open('data/mounts.json', encoding='utf-8') as f:
    mounts_data = json.load(f)

def get_mount_by_id(idx: int):
    if 0 <= idx < len(mounts_data):
        return mounts_data[idx]
    return None

@router.get('/mounts', response_model=List[Mount], tags=["Montarias e Veículos"], summary="Listar todas as montarias e veículos", description="Retorna uma lista de todas as montarias, veículos e equipamentos relacionados disponíveis.")
def list_mounts():
    """Lista todas as montarias, veículos e equipamentos relacionados do PHB."""
    return mounts_data

@router.get('/mounts/{id}', response_model=Mount, tags=["Montarias e Veículos"], summary="Detalhes de uma montaria ou veículo", description="Retorna os detalhes de uma montaria ou veículo específico pelo índice.")
def get_mount(id: int):
    """Detalhes de uma montaria ou veículo pelo índice."""
    item = get_mount_by_id(id)
    if not item:
        raise HTTPException(status_code=404, detail='Montaria/veículo não encontrado')
    return item 