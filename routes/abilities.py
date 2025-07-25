from fastapi import APIRouter, HTTPException
from typing import List
import json
from models.ability import Ability

router = APIRouter()

with open('data/abilities.json', encoding='utf-8') as f:
    abilities_data = json.load(f)

def get_ability_by_id(idx: int):
    if 0 <= idx < len(abilities_data):
        return abilities_data[idx]
    return None

@router.get('/abilities', response_model=List[Ability], tags=["Habilidades"], summary="Listar todas as habilidades", description="Retorna uma lista das 6 habilidades do personagem (Força, Destreza, Constituição, Inteligência, Sabedoria, Carisma).")
def list_abilities():
    return abilities_data

@router.get('/abilities/{id}', response_model=Ability, tags=["Habilidades"], summary="Detalhes de uma habilidade", description="Retorna os detalhes de uma habilidade específica pelo índice (0 a 5).")
def get_ability(id: int):
    item = get_ability_by_id(id)
    if not item:
        raise HTTPException(status_code=404, detail='Habilidade não encontrada')
    return item 