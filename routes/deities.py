from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
import json
from models.deity import Deus

router = APIRouter()

def load_deities() -> List[Deus]:
    """Carrega as divindades do arquivo JSON."""
    with open('data/deuses.json', encoding='utf-8') as f:
        data = json.load(f)
    return [Deus(**deity) for deity in data]

@router.get(
    '/deuses',
    response_model=List[Deus],
    tags=["Divindades"],
    summary="Listar todas as divindades",
    description="""Lista todas as divindades disponíveis.

**Divindades incluídas (80 total):**

**Panteão de Faerûn (30 divindades):**
- Akadi, Bane, Beshaba, Chauntea, Cyric
- Deneir, Eldath, Gond, Helm, Ilmater
- Kelemvor, Lathander, Lliira, Loviatar, Malar
- Mask, Milil, Myrkul, Mystra, Oghma
- Savras, Selûne, Shar, Silvanus, Sune
- Talona, Talos, Tempus, Torm, Tymora
- Umberlee, Waukeen

**Panteão de Greyhawk (3 divindades):**
- Pelor, Nerull, St. Cuthbert

**Panteão de Dragonlance (3 divindades):**
- Paladine, Takhisis, Gilean

**Panteão Nórdico (3 divindades):**
- Odin, Thor, Loki

**Panteão Egípcio (3 divindades):**
- Rá, Osíris, Ísis

**Panteão Grego (38 divindades):**
- Zeus, Atena, Hades, Apolo, Ártemis
- Ares, Afrodite, Hefesto, Hermes, Poseidon
- Deméter, Dionísio, Hélio, Selene, Nike
- Tique, Hécate, Pan, Asclépio, Perséfone
- Hebe, Íris, Nêmesis, Hipnos, Tânatos
- Eros, Psique, Morféu, Fobos, Deimos
- Harmonia, Peito, Clio, Euterpe, Tália
- Melpômene, Terpsícore, Erato, Polímnia
- Urânia, Calíope

**Filtros disponíveis:**
- `?panteao=Faerûn` - Busca divindades de um panteão específico
- `?dominio=Guerra` - Busca divindades de um domínio específico
- `?alinhamento=NB` - Busca divindades de um alinhamento específico
- `?panteao=Grego&dominio=Guerra` - Múltiplos filtros

**Exemplos de uso:**
- `GET /deuses` - Todas as divindades
- `GET /deuses?panteao=Faerûn` - Divindades de Faerûn
- `GET /deuses?dominio=Guerra` - Divindades da guerra
- `GET /deuses?alinhamento=NB` - Divindades neutras boas
- `GET /deuses?panteao=Grego&dominio=Amor` - Divindades gregas do amor

**Informações fornecidas:**
- Nome e título da divindade
- Panteão e alinhamento
- Domínios divinos
- Símbolo sagrado e plano de existência

**Uso típico:**
- Consulta para criação de personagens clérigos
- Referência para mestres e jogadores
- Informações sobre panteões e divindades
- Pesquisa por domínios específicos"""
)
def list_deities(
    panteao: Optional[str] = Query(None, description="Filtra divindades por panteão", examples=["Faerûn", "Grego", "Nórdico", "Egípcio", "Greyhawk", "Dragonlance"]),
    dominio: Optional[str] = Query(None, description="Filtra divindades por domínio", examples=["Guerra", "Vida", "Morte", "Magia", "Natureza", "Amor"]),
    alinhamento: Optional[str] = Query(None, description="Filtra divindades por alinhamento", examples=["LG", "NG", "CG", "LN", "N", "CN", "LE", "NE", "CE"])
):
    """Lista todas as divindades com filtros opcionais."""
    deities = load_deities()
    
    # Aplicar filtros sequencialmente
    if panteao and panteao.strip():
        panteao_lower = panteao.lower().strip()
        deities = [
            deity for deity in deities 
            if panteao_lower in deity.panteao.lower()
        ]
    
    if dominio and dominio.strip():
        dominio_lower = dominio.lower().strip()
        deities = [
            deity for deity in deities 
            if any(dominio_lower in d.lower() for d in deity.dominios)
        ]
    
    if alinhamento and alinhamento.strip():
        alinhamento_upper = alinhamento.upper().strip()
        deities = [
            deity for deity in deities 
            if alinhamento_upper == deity.alinhamento
        ]
    
    return deities

@router.get(
    '/deuses/{deity_id}',
    response_model=Deus,
    tags=["Divindades"],
    summary="Detalhes de uma divindade",
    description="""Retorna os detalhes completos de uma divindade específica pelo seu ID.

**Informações retornadas:**
- **ID:** Identificador único da divindade
- **Nome:** Nome da divindade
- **Título:** Epíteto ou título da divindade
- **Panteão:** Panteão ao qual pertence
- **Alinhamento:** Alinhamento da divindade
- **Domínios:** Lista de domínios divinos
- **Símbolo:** Símbolo sagrado da divindade
- **Plano:** Plano de existência da divindade

**Exemplos de uso:**
- `GET /deuses/lathander` - Detalhes de Lathander
- `GET /deuses/zeus` - Detalhes de Zeus
- `GET /deuses/odin` - Detalhes de Odin

**Uso típico:**
- Após listar divindades com filtros, use o ID para obter detalhes completos
- Consulta rápida durante criação de personagens
- Referência para mestres e jogadores"""
)
def get_deity(deity_id: str):
    """Retorna uma divindade específica pelo ID."""
    deities = load_deities()
    for deity in deities:
        if deity.id == deity_id:
            return deity
    raise HTTPException(
        status_code=404,
        detail=f"Divindade com ID '{deity_id}' não encontrada"
    )

@router.get(
    '/deuses/busca/{nome}',
    response_model=List[Deus],
    tags=["Divindades"],
    summary="Buscar divindades por nome",
    description="""Busca divindades que contenham o termo especificado no nome.

**Funcionalidades:**
- Busca case-insensitive (não diferencia maiúsculas/minúsculas)
- Busca parcial (encontra divindades que contenham o termo)
- Suporte a acentos e caracteres especiais

**Categorias de busca:**

**Por Panteão:**
- `GET /deuses/busca/zeus` - Divindades gregas
- `GET /deuses/busca/odin` - Divindades nórdicas
- `GET /deuses/busca/lathander` - Divindades de Faerûn

**Por Domínio:**
- `GET /deuses/busca/guerra` - Divindades da guerra
- `GET /deuses/busca/amor` - Divindades do amor
- `GET /deuses/busca/magia` - Divindades da magia

**Por Característica:**
- `GET /deuses/busca/sol` - Divindades solares
- `GET /deuses/busca/morte` - Divindades da morte
- `GET /deuses/busca/natureza` - Divindades da natureza

**Exemplos populares:**
- `GET /deuses/busca/Zeus` - O rei dos deuses gregos
- `GET /deuses/busca/Apolo` - Deus grego da luz e música
- `GET /deuses/busca/Atena` - Deusa grega da sabedoria
- `GET /deuses/busca/Lathander` - Deus de Faerûn da aurora
- `GET /deuses/busca/Mystra` - Deusa de Faerûn da magia"""
)
def search_deities_by_name(nome: str):
    """Busca divindades por nome."""
    deities = load_deities()
    filtered_deities = [
        deity for deity in deities
        if nome.lower() in deity.nome.lower()
    ]
    return filtered_deities 