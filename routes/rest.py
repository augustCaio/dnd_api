from fastapi import APIRouter
from typing import List
import json
from models.rest_rule import RestRule

router = APIRouter()

with open('data/rest.json', encoding='utf-8') as f:
    rest_data = json.load(f)

@router.get('/rest', response_model=List[RestRule], tags=["Descanso"], summary="Listar regras de descanso", description="Retorna regras de descanso curto, longo, exaustão, fome e sede.")
def list_rest():
    return rest_data 