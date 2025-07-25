from fastapi import APIRouter, Query
from typing import List, Optional
import json
from models.skill import Skill

router = APIRouter()

with open('data/skills.json', encoding='utf-8') as f:
    skills_data = json.load(f)

@router.get('/skills', response_model=List[Skill], tags=["Perícias"], summary="Listar todas as perícias", description="Retorna uma lista de todas as perícias do sistema, com habilidade associada e descrição. Permite filtrar por habilidade associada.")
def list_skills(
    ability: Optional[str] = Query(None, description="Filtrar por habilidade associada (ex: Destreza)")
):
    results = skills_data
    if ability:
        results = [s for s in results if s['habilidade_associada'].lower() == ability.lower()]
    return results 