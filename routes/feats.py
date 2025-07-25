from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
import json
from models.feat import Feat

router = APIRouter()

with open('data/feats.json', encoding='utf-8') as f:
    feats_data = json.load(f)

def get_feat_by_id(idx: int):
    if 0 <= idx < len(feats_data):
        return feats_data[idx]
    return None

@router.get('/feats', response_model=List[Feat], tags=["Talentos"], summary="Listar todos os talentos", description="Retorna uma lista de todos os talentos (feats) disponíveis no Livro do Jogador. Permite filtrar por classe e raça.")
def list_feats(
    class_: Optional[str] = Query(None, alias="class", description="Filtrar por classe"),
    race: Optional[str] = Query(None, description="Filtrar por raça")
):
    """Lista todos os talentos, com filtros opcionais por classe e raça."""
    results = feats_data
    if class_:
        results = [f for f in results if f.get('requisitos', {}).get('classe', '').lower() == class_.lower()]
    if race:
        results = [f for f in results if f.get('requisitos', {}).get('raça', '').lower() == race.lower()]
    return results

@router.get('/feats/{id}', response_model=Feat, tags=["Talentos"], summary="Detalhes de um talento", description="Retorna os detalhes completos de um talento (feat) específico pelo índice na lista.")
def get_feat(id: int):
    """Detalhes de um talento pelo índice."""
    item = get_feat_by_id(id)
    if not item:
        raise HTTPException(status_code=404, detail='Talento não encontrado')
    return item 