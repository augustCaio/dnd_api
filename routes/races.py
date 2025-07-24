from fastapi import APIRouter, HTTPException, Query
from models.race import Race
from typing import List, Optional
import json
import os
import unicodedata

router = APIRouter()

DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/races.json')

def normalize(text: str) -> str:
    if not text:
        return ""
    return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII').lower()

def load_races() -> List[Race]:
    with open(DATA_PATH, encoding='utf-8') as f:
        data = json.load(f)
        return [Race(**race) for race in data]

@router.get(
    "/races",
    response_model=List[Race],
    summary="Lista todas as raças ou filtra por nome/tamanho",
    description="Retorna todas as raças disponíveis. Permite busca por nome (parâmetro 'name') e filtro por tamanho (parâmetro 'size')."
)
def get_races(
    name: Optional[str] = Query(None, description="Busca parcial pelo nome da raça, ex: 'anão' ou 'anao'"),
    size: Optional[str] = Query(None, alias="size", description="Filtra raças pelo tamanho, ex: 'médio' ou 'medio'")
):
    """Lista todas as raças ou filtra por nome/tamanho."""
    races = load_races()
    if name:
        name_norm = normalize(name)
        races = [race for race in races if name_norm in normalize(race.nome)]
    if size:
        size_norm = normalize(size)
        races = [race for race in races if size_norm in normalize(race.tamanho)]
    return races

@router.get(
    "/races/{race_id}",
    response_model=Race,
    summary="Detalhes de uma raça específica",
    description="Retorna todos os detalhes de uma raça a partir do seu ID."
)
def get_race(race_id: int):
    """Retorna detalhes de uma raça pelo ID."""
    races = load_races()
    for race in races:
        if race.id == race_id:
            return race
    raise HTTPException(status_code=404, detail="Raça não encontrada") 