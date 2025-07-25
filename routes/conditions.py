from fastapi import APIRouter
from typing import List
import json

router = APIRouter()

with open('data/conditions.json', encoding='utf-8') as f:
    conditions_data = json.load(f)

@router.get('/conditions', tags=["Condições"], summary="Listar todas as condições de combate", description="Retorna uma lista de todas as condições de combate.")
def list_conditions():
    return conditions_data 