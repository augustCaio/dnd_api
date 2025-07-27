from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
import json
from models.condition import Condition

router = APIRouter()

def load_conditions() -> List[Condition]:
    """Carrega as condições do arquivo JSON."""
    with open('data/conditions.json', encoding='utf-8') as f:
        data = json.load(f)
    return [Condition(**condition) for condition in data]

@router.get(
    '/conditions', 
    response_model=List[Condition],
    tags=["Condições"], 
    summary="Listar todas as condições", 
    description="""Lista todas as condições de combate disponíveis.

**Condições incluídas (14 total):**

**Condições de Percepção:**
- **Cego:** Falha em testes de visão, vantagem/desvantagem em ataques
- **Surdo:** Falha em testes de audição

**Condições de Movimento:**
- **Caído:** Movimento limitado, penalidades em ataques
- **Esgrimado:** Velocidade 0, não pode se mover
- **Impedido:** Velocidade 0, penalidades em ataques

**Condições de Controle Mental:**
- **Enfeitiçado:** Não pode atacar o encantador
- **Incapacitado:** Não pode realizar ações ou reações
- **Atordoado:** Incapacitado, fala arrastada

**Condições de Estado:**
- **Envenenado:** Desvantagem em ataques e testes
- **Exausto:** 6 níveis cumulativos com efeitos progressivos
- **Invisível:** Não pode ser visto, vantagem em ataques
- **Paralisado:** Incapacitado, críticos automáticos próximos
- **Petrificado:** Transformado em pedra, imune a veneno
- **Inconsciente:** Inconsciente, críticos automáticos próximos

**Filtros disponíveis:**
- `?effect=desvantagem` - Busca condições que causam desvantagem
- `?effect=vantagem` - Busca condições que causam vantagem
- `?effect=ataque` - Busca condições que afetam ataques
- `?effect=movimento` - Busca condições que afetam movimento
- `?source=magia` - Busca condições causadas por magia
- `?source=veneno` - Busca condições causadas por veneno
- `?source=trauma` - Busca condições causadas por trauma

**Exemplos de uso:**
- `GET /conditions` - Todas as condições
- `GET /conditions?effect=desvantagem` - Condições que causam desvantagem
- `GET /conditions?source=magia` - Condições causadas por magia
- `GET /conditions?effect=ataque&source=veneno` - Condições que afetam ataques e são causadas por veneno
- `GET /conditions?effect=movimento` - Condições que afetam movimento

**Informações fornecidas:**
- Nome e descrição da condição
- Efeitos mecânicos detalhados
- Interações com outras regras
- Fontes comuns que causam a condição

**Uso típico:**
- Consulta durante combate para verificar efeitos
- Referência para criação de personagens
- Ajuda para mestres e jogadores
- Planejamento estratégico de combate"""
)
def list_conditions(
    effect: Optional[str] = Query(None, description="Filtra condições por efeito específico", examples=["desvantagem", "vantagem", "ataque", "movimento"]),
    source: Optional[str] = Query(None, description="Filtra condições por fonte", examples=["magia", "veneno", "trauma", "armadilha"])
):
    """Lista todas as condições de combate com filtros opcionais."""
    conditions = load_conditions()
    
    # Aplicar filtros sequencialmente
    if effect and effect.strip():
        effect_lower = effect.lower().strip()
        conditions = [
            condition for condition in conditions 
            if any(effect_lower in efeito.lower() for efeito in condition.efeitos)
        ]
    
    if source and source.strip():
        source_lower = source.lower().strip()
        conditions = [
            condition for condition in conditions 
            if condition.fontes_comuns and any(source_lower in fonte.lower() for fonte in condition.fontes_comuns)
        ]
    
    return conditions

@router.get(
    '/conditions/{condition_id}',
    response_model=Condition,
    tags=["Condições"],
    summary="Detalhes de uma condição",
    description="""Retorna os detalhes completos de uma condição específica pelo seu ID.

**Informações retornadas:**
- **Nome:** Nome da condição
- **Descrição:** Explicação detalhada dos efeitos
- **Efeitos:** Lista de efeitos mecânicos específicos
- **Interações:** Como a condição interage com outras regras
- **Fontes Comuns:** O que causa esta condição

**IDs válidos:**
- IDs de 1 a 14 (todas as condições do PHB)
- Retorna 404 para IDs inválidos

**Exemplos de uso:**
- `GET /conditions/1` - Detalhes da condição "Cego"
- `GET /conditions/5` - Detalhes da condição "Envenenado"
- `GET /conditions/10` - Detalhes da condição "Invisível"
- `GET /conditions/14` - Detalhes da condição "Inconsciente"

**Uso típico:**
- Após listar condições com filtros, use o ID para obter detalhes completos
- Consulta rápida durante combate
- Referência para mestres e jogadores

**Condições por ID:**
- **1:** Cego
- **2:** Caído
- **3:** Surdo
- **4:** Enfeitiçado
- **5:** Envenenado
- **6:** Esgrimado
- **7:** Exausto
- **8:** Incapacitado
- **9:** Impedido
- **10:** Invisível
- **11:** Paralisado
- **12:** Petrificado
- **13:** Atordoado
- **14:** Inconsciente"""
)
def get_condition(condition_id: int):
    """Retorna uma condição específica pelo ID."""
    conditions = load_conditions()
    if condition_id < 1 or condition_id > len(conditions):
        raise HTTPException(
            status_code=404, 
            detail=f"Condição com ID {condition_id} não encontrada. IDs válidos: 1-{len(conditions)}"
        )
    return conditions[condition_id - 1]

@router.get(
    '/conditions/busca/{nome}',
    response_model=List[Condition],
    tags=["Condições"],
    summary="Buscar condições por nome",
    description="""Busca condições que contenham o termo especificado no nome.

**Funcionalidades:**
- Busca case-insensitive (não diferencia maiúsculas/minúsculas)
- Busca parcial (encontra condições que contenham o termo)
- Suporte a acentos e caracteres especiais

**Categorias de busca:**

**Por Sintomas:**
- `GET /conditions/busca/cego` - Condições de cegueira
- `GET /conditions/busca/surdo` - Condições de surdez
- `GET /conditions/busca/paralis` - Condições de paralisia
- `GET /conditions/busca/atordo` - Condições de atordoamento

**Por Causas:**
- `GET /conditions/busca/veneno` - Condições causadas por veneno
- `GET /conditions/busca/magia` - Condições causadas por magia
- `GET /conditions/busca/trauma` - Condições causadas por trauma

**Por Efeitos:**
- `GET /conditions/busca/invis` - Condições de invisibilidade
- `GET /conditions/busca/petrific` - Condições de petrificação
- `GET /conditions/busca/enfeiti` - Condições de encantamento

**Por Estado:**
- `GET /conditions/busca/exausto` - Condições de exaustão
- `GET /conditions/busca/inconsciente` - Condições de inconsciência
- `GET /conditions/busca/incapacitado` - Condições de incapacitação

**Dicas de busca:**
- Use termos em português
- Busque por sintomas (cego, surdo, paralisado)
- Busque por causas (veneno, magia, trauma)
- Busque por efeitos (invisível, petrificado)
- Busque por estados (exausto, inconsciente)

**Exemplos populares:**
- `GET /conditions/busca/Cego` - Condição de cegueira
- `GET /conditions/busca/Veneno` - Condição de envenenamento
- `GET /conditions/busca/Paralis` - Condição de paralisia
- `GET /conditions/busca/Invis` - Condição de invisibilidade
- `GET /conditions/busca/Exausto` - Condição de exaustão
- `GET /conditions/busca/Enfeiti` - Condição de encantamento"""
)
def search_conditions_by_name(nome: str):
    """Busca condições por nome."""
    conditions = load_conditions()
    filtered_conditions = [
        condition for condition in conditions 
        if nome.lower() in condition.nome.lower()
    ]
    return filtered_conditions 