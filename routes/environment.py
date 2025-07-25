from fastapi import APIRouter
from typing import List
import json
from models.environment_condition import EnvironmentCondition

router = APIRouter()

with open('data/environment.json', encoding='utf-8') as f:
    environment_data = json.load(f)

@router.get('/environment', response_model=List[EnvironmentCondition], tags=["Ambiente"], summary="Listar condições ambientais", description="Retorna regras de terreno, visibilidade, clima, obstáculos e ambientes especiais.")
def list_environment():
    return environment_data 