from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
import json
import os
from models.leitura import LeituraInspiradora

router = APIRouter()

def load_leituras_data() -> List[dict]:
    """Carrega os dados das leituras inspiradoras do arquivo JSON."""
    try:
        with open("data/leituras.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

@router.get(
    "/leituras",
    response_model=List[LeituraInspiradora],
    tags=["Leituras Inspiradoras"],
    summary="Listar Todas as Leituras Inspiradoras",
    description="""Retorna todas as leituras inspiradoras que influenciaram D&D.

**Funcionalidades:**
- Lista completa de obras literárias e mitológicas
- Filtros por categoria e autor
- Busca inteligente com suporte a acentos
- Dados estruturados com influências específicas

**Parâmetros de Filtro:**
- `categoria`: Filtra por categoria (Fantasia, Mitologia, Espada e Feitiçaria, etc.)
- `autor`: Filtra por autor específico
- `influencia`: Filtra por influência específica em D&D

**Exemplos de uso:**
- `GET /leituras` - Todas as leituras
- `GET /leituras?categoria=Fantasia` - Apenas fantasia
- `GET /leituras?autor=J.R.R. Tolkien` - Obras de Tolkien
- `GET /leituras?influencia=Forgotten Realms` - Obras que influenciaram Forgotten Realms
- `GET /leituras?categoria=Mitologia&autor=Vários` - Mitologias

**Uso típico:**
- Consulta geral de inspirações literárias
- Filtros por categoria de obra
- Busca por autor específico
- Referência para mestres e jogadores"""
)
def get_leituras(
    categoria: Optional[str] = Query(None, alias="categoria", description="Filtrar por categoria da obra"),
    autor: Optional[str] = Query(None, alias="autor", description="Filtrar por autor da obra"),
    influencia: Optional[str] = Query(None, alias="influencia", description="Filtrar por influência específica em D&D")
):
    """Retorna todas as leituras inspiradoras com filtros opcionais."""
    leituras_data = load_leituras_data()
    
    if not leituras_data:
        return []
    
    # Aplicar filtros
    filtered_leituras = leituras_data
    
    if categoria:
        filtered_leituras = [
            leitura for leitura in filtered_leituras 
            if leitura.get("categoria", "").lower().strip() == categoria.lower().strip()
        ]
    
    if autor:
        filtered_leituras = [
            leitura for leitura in filtered_leituras 
            if leitura.get("autor", "").lower().strip() == autor.lower().strip()
        ]
    
    if influencia:
        filtered_leituras = [
            leitura for leitura in filtered_leituras 
            if influencia.lower().strip() in leitura.get("influencia", "").lower().strip()
        ]
    
    return [LeituraInspiradora(**leitura) for leitura in filtered_leituras]

@router.get(
    "/leituras/{leitura_id}",
    response_model=LeituraInspiradora,
    tags=["Leituras Inspiradoras"],
    summary="Detalhes de uma Leitura Inspiradora",
    description="""Retorna os detalhes completos de uma leitura inspiradora específica.

**Informações retornadas:**
- Título e autor da obra
- Categoria e descrição
- Influência específica em D&D
- Detalhes sobre a importância da obra

**Exemplos de uso:**
- `GET /leituras/senhor-dos-aneis` - Detalhes de O Senhor dos Anéis
- `GET /leituras/conan-o-barbaro` - Detalhes de Conan
- `GET /leituras/mitologia-nordica` - Detalhes da Mitologia Nórdica
- `GET /leituras/duna` - Detalhes de Duna

**Uso típico:**
- Consulta específica de uma obra
- Referência para inspiração
- Contexto histórico e cultural
- Informações para mestres

**IDs disponíveis:**
- `senhor-dos-aneis`, `conan-o-barbaro`, `duna`
- `mitologia-nordica`, `mitologia-grega`, `mitologia-celta`
- E muitos outros..."""
)
def get_leitura_by_id(leitura_id: str):
    """Retorna os detalhes de uma leitura inspiradora específica."""
    leituras_data = load_leituras_data()
    
    for leitura in leituras_data:
        if leitura.get("id") == leitura_id:
            return LeituraInspiradora(**leitura)
    
    # Se não encontrou, tenta buscar por título (case-insensitive)
    for leitura in leituras_data:
        if leitura.get("titulo", "").lower().replace(" ", "-").replace("ã", "a").replace("ç", "c") == leitura_id.lower():
            return LeituraInspiradora(**leitura)
    
    raise HTTPException(
        status_code=404,
        detail=f"Leitura inspiradora '{leitura_id}' não encontrada. Use /leituras para ver todas as leituras disponíveis."
    )

@router.get(
    "/leituras/categorias/{categoria}",
    response_model=List[LeituraInspiradora],
    tags=["Leituras Inspiradoras"],
    summary="Leituras por Categoria",
    description="""Retorna todas as leituras de uma categoria específica.

**Categorias disponíveis:**
- `Fantasia` - Obras de fantasia épica
- `Mitologia` - Mitologias de diversos povos
- `Espada e Feitiçaria` - Literatura de espada e feitiçaria
- `Ficção Científica` - Obras de ficção científica
- `Terror` - Literatura de terror e horror

**Exemplos de uso:**
- `GET /leituras/categorias/Fantasia` - Todas as obras de fantasia
- `GET /leituras/categorias/Mitologia` - Todas as mitologias
- `GET /leituras/categorias/Espada e Feitiçaria` - Espada e feitiçaria
- `GET /leituras/categorias/Ficção Científica` - Ficção científica

**Uso típico:**
- Consulta por categoria de obra
- Planejamento de inspirações
- Referência para mestres
- Contexto para campanhas"""
)
def get_leituras_by_category(categoria: str):
    """Retorna todas as leituras de uma categoria específica."""
    leituras_data = load_leituras_data()
    
    filtered_leituras = [
        leitura for leitura in leituras_data 
        if leitura.get("categoria", "").lower().strip() == categoria.lower().strip()
    ]
    
    if not filtered_leituras:
        raise HTTPException(
            status_code=404,
            detail=f"Nenhuma leitura encontrada da categoria '{categoria}'. Categorias disponíveis: Fantasia, Mitologia, Espada e Feitiçaria, Ficção Científica, Terror"
        )
    
    return [LeituraInspiradora(**leitura) for leitura in filtered_leituras]

@router.get(
    "/leituras/autores/{autor}",
    response_model=List[LeituraInspiradora],
    tags=["Leituras Inspiradoras"],
    summary="Leituras por Autor",
    description="""Retorna todas as leituras de um autor específico.

**Autores disponíveis:**
- `J.R.R. Tolkien` - O Senhor dos Anéis
- `Robert E. Howard` - Conan, o Bárbaro
- `Frank Herbert` - Duna
- `Fritz Leiber` - Fafhrd e o Mago Cinzento
- `Michael Moorcock` - Elric de Melniboné
- `Clark Ashton Smith` - Terra Morta
- `Vários` - Mitologias diversas

**Exemplos de uso:**
- `GET /leituras/autores/J.R.R. Tolkien` - Obras de Tolkien
- `GET /leituras/autores/Robert E. Howard` - Obras de Howard
- `GET /leituras/autores/Vários` - Mitologias
- `GET /leituras/autores/Frank Herbert` - Obras de Herbert

**Uso típico:**
- Consulta por autor específico
- Estudo de influências literárias
- Referência para mestres
- Contexto para campanhas"""
)
def get_leituras_by_author(autor: str):
    """Retorna todas as leituras de um autor específico."""
    leituras_data = load_leituras_data()
    
    filtered_leituras = [
        leitura for leitura in leituras_data 
        if leitura.get("autor", "").lower().strip() == autor.lower().strip()
    ]
    
    if not filtered_leituras:
        raise HTTPException(
            status_code=404,
            detail=f"Nenhuma leitura encontrada do autor '{autor}'. Use /leituras para ver todos os autores disponíveis."
        )
    
    return [LeituraInspiradora(**leitura) for leitura in filtered_leituras] 