from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from models.class_ import Class, ClassLevel, Feature
import json
import os

router = APIRouter()

DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/classes.json')

def load_classes() -> List[Class]:
    with open(DATA_PATH, encoding='utf-8') as f:
        data = json.load(f)
        return [Class(**cls) for cls in data]

@router.get(
    "/classes",
    response_model=List[Class],
    summary="Lista todas as classes",
    description="Lista todas as classes disponíveis. Permite filtrar por magia, dado de vida e proficiência em armaduras."
)
def get_classes(
    magic: Optional[bool] = Query(None, description="Filtra classes que possuem magia", examples=[True]),
    hit_die: Optional[str] = Query(None, description="Filtra classes pelo dado de vida, ex: '1d10'", examples=["1d10"]),
    armor: Optional[str] = Query(None, description="Filtra classes por proficiência em armaduras, ex: 'leve', 'média', 'todas'", examples=["leve"])
):
    classes = load_classes()
    if magic is not None:
        def has_magic(cls):
            for nivel in cls.niveis:
                if hasattr(nivel, 'magias') and nivel.magias:
                    return True
            return False
        classes = [cls for cls in classes if has_magic(cls) == magic]
    if hit_die:
        classes = [cls for cls in classes if hit_die.lower() in cls.dado_vida.lower()]
    if armor:
        armor_norm = armor.lower()
        classes = [cls for cls in classes if any(armor_norm in prof.lower() for prof in cls.proficiencias if 'armadura' in prof.lower() or 'armaduras' in prof.lower())]
    return classes

@router.get(
    "/classes/{class_id}",
    response_model=Class,
    summary="Detalhes de uma classe",
    description="Retorna todos os detalhes de uma classe pelo seu ID."
)
def get_class(class_id: int):
    classes = load_classes()
    if 1 <= class_id <= len(classes):
        return classes[class_id - 1]
    raise HTTPException(status_code=404, detail="Classe não encontrada")

@router.get(
    "/classes/{class_id}/niveis",
    response_model=List[ClassLevel],
    summary="Habilidades por nível",
    description="Lista todas as habilidades e magias adquiridas por nível da classe."
)
def get_class_levels(class_id: int):
    classes = load_classes()
    if 1 <= class_id <= len(classes):
        return classes[class_id - 1].niveis
    raise HTTPException(status_code=404, detail="Classe não encontrada")

@router.get(
    "/classes/{class_id}/magias",
    summary="Magias conhecidas da classe",
    description="Lista todas as magias conhecidas pela classe, se aplicável."
)
def get_class_spells(class_id: int):
    classes = load_classes()
    if 1 <= class_id <= len(classes):
        spells = []
        for level in classes[class_id - 1].niveis:
            if hasattr(level, 'magias') and level.magias:
                spells.extend(level.magias)
        return spells
    raise HTTPException(status_code=404, detail="Classe não encontrada") 