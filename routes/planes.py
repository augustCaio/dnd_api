from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
import json
import os
from models.plane import PlanoExistencia

router = APIRouter()

def load_planes_data() -> List[dict]:
    """Carrega os dados dos planos do arquivo JSON."""
    try:
        with open("data/planos.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

@router.get(
    "/planos",
    response_model=List[PlanoExistencia],
    tags=["Planos"],
    summary="Listar Todos os Planos",
    description="""Retorna todos os planos de existência disponíveis na API.

**Funcionalidades:**
- Lista completa de todos os planos
- Filtros opcionais por tipo, alinhamento e associação
- Busca inteligente com suporte a acentos
- Dados estruturados com criaturas típicas

**Parâmetros de Filtro:**
- `tipo`: Filtra por tipo de plano (Material, Interior, Exterior, Transitivo)
- `alinhamento`: Filtra por alinhamento moral/ético
- `associado_a`: Filtra por deus, elemento ou energia associada

**Exemplos de uso:**
- `GET /planos` - Todos os planos
- `GET /planos?tipo=Exterior` - Apenas planos exteriores
- `GET /planos?alinhamento=Caótico e Bom` - Planos caóticos e bons
- `GET /planos?associado_a=Tyr` - Planos associados a Tyr

**Uso típico:**
- Consulta geral de planos
- Filtros por categoria
- Busca por alinhamento
- Referência para mestres e jogadores"""
)
def get_planes(
    tipo: Optional[str] = Query(None, alias="tipo", description="Filtrar por tipo de plano"),
    alinhamento: Optional[str] = Query(None, alias="alinhamento", description="Filtrar por alinhamento"),
    associado_a: Optional[str] = Query(None, alias="associado_a", description="Filtrar por deus, elemento ou energia associada")
):
    """Retorna todos os planos com filtros opcionais."""
    planes_data = load_planes_data()
    
    if not planes_data:
        return []
    
    # Aplicar filtros
    filtered_planes = planes_data
    
    if tipo:
        filtered_planes = [
            plane for plane in filtered_planes 
            if plane.get("tipo", "").lower().strip() == tipo.lower().strip()
        ]
    
    if alinhamento:
        filtered_planes = [
            plane for plane in filtered_planes 
            if plane.get("alinhamento", "").lower().strip() == alinhamento.lower().strip()
        ]
    
    if associado_a:
        filtered_planes = [
            plane for plane in filtered_planes 
            if associado_a.lower().strip() in plane.get("associado_a", "").lower().strip()
        ]
    
    return [PlanoExistencia(**plane) for plane in filtered_planes]

@router.get(
    "/planos/{plane_id}",
    response_model=PlanoExistencia,
    tags=["Planos"],
    summary="Detalhes de um Plano",
    description="""Retorna os detalhes completos de um plano específico.

**Informações retornadas:**
- Nome e tipo do plano
- Descrição detalhada
- Alinhamento e associações
- Criaturas típicas do plano

**Exemplos de uso:**
- `GET /planos/plano-material` - Detalhes do Plano Material
- `GET /planos/monte-celestia` - Detalhes do Monte Celéstia
- `GET /planos/abismo` - Detalhes do Abismo
- `GET /planos/plano-etereo` - Detalhes do Plano Etéreo

**Uso típico:**
- Consulta específica de um plano
- Referência para aventuras planárias
- Informações para conjuração de magias
- Contexto para narrativa

**IDs disponíveis:**
- `plano-material`, `plano-etereo`, `plano-astral`
- `monte-celestia`, `campos-eliseos`, `arborea`
- `abismo`, `inferno`, `limbo`, `acheron`
- E muitos outros..."""
)
def get_plane_by_id(plane_id: str):
    """Retorna os detalhes de um plano específico."""
    planes_data = load_planes_data()
    
    for plane in planes_data:
        if plane.get("id") == plane_id:
            return PlanoExistencia(**plane)
    
    # Se não encontrou, tenta buscar por nome (case-insensitive)
    for plane in planes_data:
        if plane.get("nome", "").lower().replace(" ", "-").replace("ã", "a").replace("ç", "c") == plane_id.lower():
            return PlanoExistencia(**plane)
    
    raise HTTPException(
        status_code=404,
        detail=f"Plano '{plane_id}' não encontrado. Use /planos para ver todos os planos disponíveis."
    )

@router.get(
    "/planos/tipos/{tipo}",
    response_model=List[PlanoExistencia],
    tags=["Planos"],
    summary="Planos por Tipo",
    description="""Retorna todos os planos de um tipo específico.

**Tipos disponíveis:**
- `Material` - Plano Material
- `Interior` - Planos Elementais e de Energia
- `Exterior` - Planos dos Deuses e Almas
- `Transitivo` - Planos de Conexão e Viagem

**Exemplos de uso:**
- `GET /planos/tipos/Exterior` - Todos os planos exteriores
- `GET /planos/tipos/Interior` - Todos os planos elementais
- `GET /planos/tipos/Transitivo` - Todos os planos transitivos
- `GET /planos/tipos/Material` - Plano Material

**Uso típico:**
- Consulta por categoria de plano
- Planejamento de viagem planar
- Referência para conjuração
- Contexto para aventuras"""
)
def get_planes_by_type(tipo: str):
    """Retorna todos os planos de um tipo específico."""
    planes_data = load_planes_data()
    
    filtered_planes = [
        plane for plane in planes_data 
        if plane.get("tipo", "").lower().strip() == tipo.lower().strip()
    ]
    
    if not filtered_planes:
        raise HTTPException(
            status_code=404,
            detail=f"Nenhum plano encontrado do tipo '{tipo}'. Tipos disponíveis: Material, Interior, Exterior, Transitivo"
        )
    
    return [PlanoExistencia(**plane) for plane in filtered_planes]

@router.get(
    "/planos/alinhamentos/{alinhamento}",
    response_model=List[PlanoExistencia],
    tags=["Planos"],
    summary="Planos por Alinhamento",
    description="""Retorna todos os planos de um alinhamento específico.

**Alinhamentos disponíveis:**
- `Leal e Bom`, `Neutro e Bom`, `Caótico e Bom`
- `Leal e Neutro`, `Neutro`, `Caótico e Neutro`
- `Leal e Mau`, `Neutro e Mau`, `Caótico e Mau`

**Exemplos de uso:**
- `GET /planos/alinhamentos/Leal e Bom` - Planos leais e bons
- `GET /planos/alinhamentos/Caótico e Mau` - Planos caóticos e maus
- `GET /planos/alinhamentos/Neutro` - Planos neutros
- `GET /planos/alinhamentos/Leal e Neutro` - Planos leais e neutros

**Uso típico:**
- Consulta por alinhamento moral
- Planejamento de personagens
- Contexto para narrativa
- Referência para deuses"""
)
def get_planes_by_alignment(alinhamento: str):
    """Retorna todos os planos de um alinhamento específico."""
    planes_data = load_planes_data()
    
    filtered_planes = [
        plane for plane in planes_data 
        if plane.get("alinhamento", "").lower().strip() == alinhamento.lower().strip()
    ]
    
    if not filtered_planes:
        raise HTTPException(
            status_code=404,
            detail=f"Nenhum plano encontrado com alinhamento '{alinhamento}'. Use /planos para ver todos os alinhamentos disponíveis."
        )
    
    return [PlanoExistencia(**plane) for plane in filtered_planes] 