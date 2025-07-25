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

@router.get('/backgrounds', response_model=List[Background], tags=["Antecedentes"], summary="Listar todos os antecedentes", description="Retorna uma lista de todos os antecedentes disponíveis, com filtros por nome, proficiência e ideal.")
def list_backgrounds(
    name: Optional[str] = Query(None, description="Filtrar por nome"),
    prof: Optional[str] = Query(None, description="Filtrar por proficiência"),
    ideal: Optional[str] = Query(None, description="Filtrar por ideal")
):
    """Lista todos os antecedentes, com filtros opcionais por nome, proficiência e ideal."""
    results = backgrounds_data
    if name:
        results = [bg for bg in results if name.lower() in bg['nome'].lower()]
    if prof:
        results = [bg for bg in results if any(prof.lower() in p.lower() for p in bg.get('proficiencias', []))]
    if ideal:
        results = [bg for bg in results if any(ideal.lower() in i.lower() for i in bg.get('personalidade', {}).get('ideais', []))]
    return results

@router.get('/backgrounds/{id}', response_model=Background, tags=["Antecedentes"], summary="Detalhes de um antecedente", description="Retorna os detalhes de um antecedente específico pelo índice.")
def get_background(id: int):
    """Detalhes de um antecedente pelo índice."""
    bg = get_background_by_id(id)
    if not bg:
        raise HTTPException(status_code=404, detail='Antecedente não encontrado')
    return bg

@router.get('/backgrounds/{id}/traits', tags=["Antecedentes"], summary="Traços de personalidade de um antecedente", description="Retorna apenas os traços de personalidade do antecedente pelo índice.")
def get_background_traits(id: int):
    """Retorna apenas os traços de personalidade do antecedente."""
    bg = get_background_by_id(id)
    if not bg:
        raise HTTPException(status_code=404, detail='Antecedente não encontrado')
    return bg['personalidade']

with open('data/currency.json', encoding='utf-8') as f:
    currency_data = json.load(f)
with open('data/services.json', encoding='utf-8') as f:
    services_data = json.load(f)
with open('data/lifestyles.json', encoding='utf-8') as f:
    lifestyles_data = json.load(f)

@router.get('/currency', tags=["Moedas"], summary="Listar moedas e conversões", description="Retorna todas as moedas do PHB e suas conversões.")
def list_currency():
    """Lista todas as moedas e conversões do PHB."""
    return currency_data

@router.get('/services', tags=["Serviços"], summary="Listar serviços", description="Retorna todos os serviços e preços aproximados do PHB.")
def list_services():
    """Lista todos os serviços e preços aproximados do PHB."""
    return services_data

@router.get('/lifestyles', tags=["Estilos de Vida"], summary="Listar estilos de vida", description="Retorna todos os estilos de vida e custos diários do PHB.")
def list_lifestyles():
    """Lista todos os estilos de vida e custos diários do PHB."""
    return lifestyles_data 