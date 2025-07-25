from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
import json
from models.background import Background

router = APIRouter()

# Carregar dados do JSON
with open('data/backgrounds.json', encoding='utf-8') as f:
    backgrounds_data = json.load(f)

# Função utilitária para buscar por índice (id)
def get_background_by_id(idx: int):
    if 0 <= idx < len(backgrounds_data):
        return backgrounds_data[idx]
    else:
        return None

@router.get('/backgrounds', response_model=List[Background])
def list_backgrounds(
    name: Optional[str] = Query(None, description="Filtrar por nome"),
    prof: Optional[str] = Query(None, description="Filtrar por proficiência"),
    ideal: Optional[str] = Query(None, description="Filtrar por ideal")
):
    results = backgrounds_data
    if name:
        results = [bg for bg in results if name.lower() in bg['nome'].lower()]
    if prof:
        results = [bg for bg in results if any(prof.lower() in p.lower() for p in bg.get('proficiencias', []))]
    if ideal:
        results = [bg for bg in results if any(ideal.lower() in i.lower() for i in bg.get('personalidade', {}).get('ideais', []))]
    return results

@router.get('/backgrounds/{id}', response_model=Background)
def get_background(id: int):
    bg = get_background_by_id(id)
    if not bg:
        raise HTTPException(status_code=404, detail='Antecedente não encontrado')
    return bg

@router.get('/backgrounds/{id}/traits')
def get_background_traits(id: int):
    bg = get_background_by_id(id)
    if not bg:
        raise HTTPException(status_code=404, detail='Antecedente não encontrado')
    return bg['personalidade'] 