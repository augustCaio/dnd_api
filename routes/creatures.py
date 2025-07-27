from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
import json
import os
from models.creature import Criatura

router = APIRouter()

def load_creatures_data() -> List[dict]:
    """Carrega os dados das criaturas do arquivo JSON."""
    try:
        with open("data/criaturas.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

@router.get(
    "/criaturas",
    response_model=List[Criatura],
    tags=["Criaturas"],
    summary="Listar Todas as Criaturas",
    description="""Retorna todas as criaturas disponíveis na API.

**Funcionalidades:**
- Lista completa de todas as criaturas
- Filtros opcionais por tipo, tamanho e nível de desafio
- Busca inteligente com suporte a acentos
- Dados estruturados com ataques e sentidos

**Parâmetros de Filtro:**
- `tipo`: Filtra por tipo de criatura (Besta, Morto-vivo, Humanoide, etc.)
- `tamanho`: Filtra por tamanho (Miúdo, Pequeno, Médio, Grande, Enorme)
- `nd`: Filtra por nível de desafio (0, 1/8, 1/4, 1/2, etc.)

**Exemplos de uso:**
- `GET /criaturas` - Todas as criaturas
- `GET /criaturas?tipo=Besta` - Apenas bestas
- `GET /criaturas?tamanho=Médio` - Criaturas médias
- `GET /criaturas?nd=1/4` - Criaturas com ND 1/4
- `GET /criaturas?tipo=Besta&tamanho=Miúdo` - Bestas miúdas

**Uso típico:**
- Consulta geral de criaturas
- Filtros por categoria
- Busca por nível de desafio
- Referência para mestres e jogadores"""
)
def get_creatures(
    tipo: Optional[str] = Query(None, alias="tipo", description="Filtrar por tipo de criatura"),
    tamanho: Optional[str] = Query(None, alias="tamanho", description="Filtrar por tamanho da criatura"),
    nd: Optional[str] = Query(None, alias="nd", description="Filtrar por nível de desafio")
):
    """Retorna todas as criaturas com filtros opcionais."""
    creatures_data = load_creatures_data()
    
    if not creatures_data:
        return []
    
    # Aplicar filtros
    filtered_creatures = creatures_data
    
    if tipo:
        filtered_creatures = [
            creature for creature in filtered_creatures 
            if creature.get("tipo", "").lower().strip() == tipo.lower().strip()
        ]
    
    if tamanho:
        filtered_creatures = [
            creature for creature in filtered_creatures 
            if creature.get("tamanho", "").lower().strip() == tamanho.lower().strip()
        ]
    
    if nd:
        filtered_creatures = [
            creature for creature in filtered_creatures 
            if creature.get("nivel_desafio", "").lower().strip() == nd.lower().strip()
        ]
    
    return [Criatura(**creature) for creature in filtered_creatures]

@router.get(
    "/criaturas/{creature_id}",
    response_model=Criatura,
    tags=["Criaturas"],
    summary="Detalhes de uma Criatura",
    description="""Retorna os detalhes completos de uma criatura específica.

**Informações retornadas:**
- Nome e tipo da criatura
- Estatísticas completas (CA, PV, atributos)
- Ataques e habilidades
- Sentidos e idiomas
- Notas descritivas

**Exemplos de uso:**
- `GET /criaturas/goblin` - Detalhes do Goblin
- `GET /criaturas/dragao-vermelho-adulto` - Detalhes do Dragão
- `GET /criaturas/esqueleto` - Detalhes do Esqueleto
- `GET /criaturas/corvo` - Detalhes do Corvo

**Uso típico:**
- Consulta específica de uma criatura
- Referência para combate
- Informações para invocação
- Contexto para narrativa

**IDs disponíveis:**
- `aguia-gigante`, `cavalo-guerra`, `corvo`
- `cao-guarda`, `cavalo-ponei`, `lagarto-gigante`
- `esqueleto`, `zumbi`, `lobo`, `gato`
- E muitos outros..."""
)
def get_creature_by_id(creature_id: str):
    """Retorna os detalhes de uma criatura específica."""
    creatures_data = load_creatures_data()
    
    for creature in creatures_data:
        if creature.get("id") == creature_id:
            return Criatura(**creature)
    
    # Se não encontrou, tenta buscar por nome (case-insensitive)
    for creature in creatures_data:
        if creature.get("nome", "").lower().replace(" ", "-").replace("ã", "a").replace("ç", "c") == creature_id.lower():
            return Criatura(**creature)
    
    raise HTTPException(
        status_code=404,
        detail=f"Criatura '{creature_id}' não encontrada. Use /criaturas para ver todas as criaturas disponíveis."
    )

@router.get(
    "/criaturas/tipos/{tipo}",
    response_model=List[Criatura],
    tags=["Criaturas"],
    summary="Criaturas por Tipo",
    description="""Retorna todas as criaturas de um tipo específico.

**Tipos disponíveis:**
- `Besta` - Animais e criaturas naturais
- `Morto-vivo` - Esqueletos, zumbis e outros mortos-vivos
- `Humanoide` - Goblins, orcs e outras criaturas humanoides
- `Dragão` - Dragões de todos os tipos
- `Elemental` - Criaturas elementais
- `Fada` - Criaturas feéricas

**Exemplos de uso:**
- `GET /criaturas/tipos/Besta` - Todas as bestas
- `GET /criaturas/tipos/Morto-vivo` - Todos os mortos-vivos
- `GET /criaturas/tipos/Humanoide` - Todos os humanoides
- `GET /criaturas/tipos/Dragão` - Todos os dragões

**Uso típico:**
- Consulta por categoria de criatura
- Planejamento de encontros
- Referência para invocação
- Contexto para aventuras"""
)
def get_creatures_by_type(tipo: str):
    """Retorna todas as criaturas de um tipo específico."""
    creatures_data = load_creatures_data()
    
    filtered_creatures = [
        creature for creature in creatures_data 
        if creature.get("tipo", "").lower().strip() == tipo.lower().strip()
    ]
    
    if not filtered_creatures:
        raise HTTPException(
            status_code=404,
            detail=f"Nenhuma criatura encontrada do tipo '{tipo}'. Tipos disponíveis: Besta, Morto-vivo, Humanoide, Dragão, Elemental, Fada"
        )
    
    return [Criatura(**creature) for creature in filtered_creatures]

@router.get(
    "/criaturas/tamanhos/{tamanho}",
    response_model=List[Criatura],
    tags=["Criaturas"],
    summary="Criaturas por Tamanho",
    description="""Retorna todas as criaturas de um tamanho específico.

**Tamanhos disponíveis:**
- `Miúdo` - Criaturas muito pequenas (insetos, ratos)
- `Pequeno` - Criaturas pequenas (goblins, gatos)
- `Médio` - Criaturas humanas (humanos, lobos)
- `Grande` - Criaturas grandes (cavalos, águias gigantes)
- `Enorme` - Criaturas enormes (dragões adultos)
- `Colossal` - Criaturas colossais (dragões anciões)

**Exemplos de uso:**
- `GET /criaturas/tamanhos/Miúdo` - Criaturas miúdas
- `GET /criaturas/tamanhos/Médio` - Criaturas médias
- `GET /criaturas/tamanhos/Grande` - Criaturas grandes
- `GET /criaturas/tamanhos/Enorme` - Criaturas enormes

**Uso típico:**
- Consulta por tamanho de criatura
- Planejamento de combate
- Referência para espaços
- Contexto para ambientes"""
)
def get_creatures_by_size(tamanho: str):
    """Retorna todas as criaturas de um tamanho específico."""
    creatures_data = load_creatures_data()
    
    filtered_creatures = [
        creature for creature in creatures_data 
        if creature.get("tamanho", "").lower().strip() == tamanho.lower().strip()
    ]
    
    if not filtered_creatures:
        raise HTTPException(
            status_code=404,
            detail=f"Nenhuma criatura encontrada do tamanho '{tamanho}'. Tamanhos disponíveis: Miúdo, Pequeno, Médio, Grande, Enorme, Colossal"
        )
    
    return [Criatura(**creature) for creature in filtered_creatures]

@router.get(
    "/criaturas/niveis/{nd}",
    response_model=List[Criatura],
    tags=["Criaturas"],
    summary="Criaturas por Nível de Desafio",
    description="""Retorna todas as criaturas de um nível de desafio específico.

**Níveis de Desafio disponíveis:**
- `0` - Criaturas inofensivas (ratos, insetos)
- `1_8` - Criaturas fracas (cães, poneis) - use 1_8 no lugar de 1/8
- `1_4` - Criaturas perigosas (lobos, esqueletos) - use 1_4 no lugar de 1/4
- `1_2` - Criaturas moderadas (cavalos de guerra) - use 1_2 no lugar de 1/2
- `1` - Criaturas desafiadoras
- `2+` - Criaturas poderosas

**Exemplos de uso:**
- `GET /criaturas/niveis/0` - Criaturas com ND 0
- `GET /criaturas/niveis/1_4` - Criaturas com ND 1/4
- `GET /criaturas/niveis/1_2` - Criaturas com ND 1/2
- `GET /criaturas/niveis/1` - Criaturas com ND 1

**Uso típico:**
- Consulta por dificuldade
- Planejamento de encontros
- Balanceamento de combate
- Referência para mestres"""
)
def get_creatures_by_challenge_rating(nd: str):
    """Retorna todas as criaturas de um nível de desafio específico."""
    creatures_data = load_creatures_data()
    
    # Converter underscore para slash para compatibilidade
    nd_normalized = nd.replace("_", "/")
    
    filtered_creatures = [
        creature for creature in creatures_data 
        if creature.get("nivel_desafio", "").lower().strip() == nd_normalized.lower().strip()
    ]
    
    if not filtered_creatures:
        raise HTTPException(
            status_code=404,
            detail=f"Nenhuma criatura encontrada com nível de desafio '{nd_normalized}'. Use /criaturas para ver todos os níveis disponíveis."
        )
    
    return [Criatura(**creature) for creature in filtered_creatures] 