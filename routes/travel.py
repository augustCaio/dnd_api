from fastapi import APIRouter, Query
from typing import List, Optional
import json
from models.travel_rule import TravelRule

router = APIRouter()

with open('data/travel.json', encoding='utf-8') as f:
    travel_data = json.load(f)

@router.get('/travel', response_model=List[TravelRule], tags=["Viagem"], summary="Listar ritmos de viagem", description="Retorna todos os ritmos de viagem e regras relacionadas. Permite filtrar por ritmo (pace).")
def list_travel(
    pace: Optional[str] = Query(None, description="Filtrar por ritmo de viagem: lento, normal, rápido")
):
    results = travel_data
    if pace:
        results = [t for t in results if t.get('ritmo', '').lower() == pace.lower()]
    return results 