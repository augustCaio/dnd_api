from fastapi import APIRouter, Query
from typing import List, Optional
import json
from models.multiclass_requirement import MulticlassRequirement

router = APIRouter()

with open('data/multiclass_requirements.json', encoding='utf-8') as f:
    multiclass_data = json.load(f)

@router.get('/multiclass', response_model=List[MulticlassRequirement], tags=["Multiclasse"], summary="Listar todas as combinações de multiclasses", description="Retorna todas as combinações possíveis de multiclasses, requisitos de atributos, benefícios e regras gerais. Permite filtrar por classe base (from) e classe desejada (to).")
def list_multiclass(
    from_: Optional[str] = Query(None, alias="from", description="Classe base"),
    to: Optional[str] = Query(None, description="Classe desejada")
):
    """Lista todas as combinações possíveis de multiclasses, com filtros opcionais."""
    results = [m for m in multiclass_data if 'classe_base' in m and 'classe_desejada' in m]
    if from_:
        results = [m for m in results if m.get('classe_base', '').lower() == from_.lower()]
    if to:
        results = [m for m in results if m.get('classe_desejada', '').lower() == to.lower()]
    return results 