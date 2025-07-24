from fastapi import APIRouter, HTTPException, Query
from models.race import Race, SubRace
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

def load_all_subraces() -> List[dict]:
    """Retorna todas as sub-raças do arquivo, com referência ao id da raça."""
    races = load_races()
    subraces = []
    for race in races:
        if race.subracas:
            for idx, sub in enumerate(race.subracas):
                sub_dict = sub.model_dump() if hasattr(sub, 'model_dump') else (sub.dict() if hasattr(sub, 'dict') else dict(sub))
                sub_dict['race_id'] = race.id
                sub_dict['subrace_id'] = f"{race.id}_{idx+1}"
                sub_dict['race_nome'] = race.nome
                subraces.append(sub_dict)
    return subraces

@router.get(
    "/races",
    response_model=List[Race],
    summary="Lista todas as raças ou filtra por nome/tamanho",
    description="Retorna todas as raças disponíveis. Permite busca por nome (parâmetro 'name'), filtro por tamanho (parâmetro 'size'), ordenação por nome (order=nome), filtro por característica (filter=...) e filtro por bônus (bonus=...)."
)
def get_races(
    name: Optional[str] = Query(None, description="Busca parcial pelo nome da raça, ex: 'anão' ou 'anao'"),
    size: Optional[str] = Query(None, alias="size", description="Filtra raças pelo tamanho, ex: 'médio' ou 'medio'"),
    order: Optional[str] = Query(None, description="Ordena as raças pelo campo especificado, ex: 'nome'"),
    filter: Optional[str] = Query(None, description="Filtra raças por característica, ex: 'visao_no_escuro', 'resiliencia', 'proficiencias', etc."),
    bonus: Optional[str] = Query(None, description="Filtra raças por bônus de habilidade, ex: 'forca', 'destreza', etc.")
):
    """Lista todas as raças ou filtra por nome/tamanho, característica, bônus e permite ordenação."""
    races = load_races()
    if name:
        name_norm = normalize(name)
        races = [race for race in races if name_norm in normalize(race.nome)]
    if size:
        size_norm = normalize(size)
        races = [race for race in races if size_norm in normalize(race.tamanho)]
    if filter:
        filter_norm = normalize(filter)
        filtered = []
        for race in races:
            # Verifica se o campo existe e não é None
            value = getattr(race, filter, None)
            if value:
                # Se for lista, verifica se não está vazia
                if isinstance(value, list) and len(value) > 0:
                    filtered.append(race)
                # Se for string, verifica se não está vazia
                elif isinstance(value, str) and value.strip():
                    filtered.append(race)
        races = filtered
    if bonus:
        bonus_norm = normalize(bonus)
        filtered = []
        for race in races:
            if bonus_norm in normalize(race.aumento_habilidade):
                filtered.append(race)
        races = filtered
    if order == "nome":
        races = sorted(races, key=lambda r: normalize(r.nome))
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

@router.get("/races/{race_id}/subraces", response_model=List[SubRace], summary="Lista sub-raças de uma raça")
def get_subraces_of_race(race_id: int):
    races = load_races()
    for race in races:
        if race.id == race_id:
            if not race.subracas:
                return []
            return race.subracas
    raise HTTPException(status_code=404, detail="Raça não encontrada")

@router.get("/subraces/{subrace_id}", summary="Detalhes de uma sub-raça")
def get_subrace_by_id(subrace_id: str):
    subraces = load_all_subraces()
    for sub in subraces:
        if sub["subrace_id"] == subrace_id:
            return sub
    raise HTTPException(status_code=404, detail="Sub-raça não encontrada")

@router.get("/subraces", summary="Busca sub-raças por nome")
def search_subraces(name: Optional[str] = Query(None, description="Busca parcial pelo nome da sub-raça")):
    subraces = load_all_subraces()
    if name:
        name_norm = normalize(name)
        subraces = [sub for sub in subraces if name_norm in normalize(sub["nome"])]
    return subraces 