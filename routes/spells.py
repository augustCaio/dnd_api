from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from models.spell import Spell
import json
import os

router = APIRouter()

DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/spells.json')

def load_spells() -> List[Spell]:
    with open(DATA_PATH, encoding='utf-8') as f:
        data = json.load(f)
        return [Spell(**spell) for spell in data]

@router.get(
    "/spells",
    response_model=List[Spell],
    tags=["Magias"],
    summary="Lista todas as magias",
    description="""Lista todas as magias disponíveis com filtros avançados.

**Exemplos de uso:**
- `GET /spells` - Lista todas as magias
- `GET /spells?level=1` - Magias de 1º nível
- `GET /spells?school=Evocação` - Magias de evocação
- `GET /spells?class=mago` - Magias do mago
- `GET /spells?component=V` - Magias com componente verbal
- `GET /spells?ritual=true` - Magias rituais
- `GET /spells?concentration=true` - Magias de concentração
- `GET /spells?range=Toque` - Magias com alcance toque
- `GET /spells?level=3&school=Evocação&class=mago` - Múltiplos filtros

**Escolas disponíveis:** Abjuração, Conjuração, Divinação, Encantamento, Evocação, Ilusão, Necromancia, Transmutação

**Classes disponíveis:** Mago, Clérigo, Druida, Bardo, Feiticeiro, Warlock, Paladino, Ranger

**Componentes:** V (Verbal), S (Somático), M (Material)

**Alcances:** Pessoal, Toque, 9 metros, 18 metros, 36 metros, 45 metros, etc."""
)
def get_spells(
    level: Optional[int] = Query(None, description="Filtra magias por nível (0-9)", examples=[0, 1, 3, 5, 9]),
    school: Optional[str] = Query(None, description="Filtra magias por escola", examples=["Evocação", "Abjuração", "Ilusão", "Necromancia"]),
    class_: Optional[str] = Query(None, description="Filtra magias por classe conjuradora", examples=["Mago", "Clérigo", "Druida", "Bardo"]),
    component: Optional[str] = Query(None, description="Filtra magias por componente (V, S, M)", examples=["V", "S", "M"]),
    ritual: Optional[bool] = Query(None, description="Filtra magias que podem ser conjuradas como ritual", examples=[True, False]),
    concentration: Optional[bool] = Query(None, description="Filtra magias que requerem concentração", examples=[True, False]),
    range_: Optional[str] = Query(None, description="Filtra magias por alcance", examples=["Toque", "Pessoal", "9 metros", "45 metros"])
):
    """Lista todas as magias do PHB, com filtros opcionais."""
    spells = load_spells()
    
    # Aplicar filtros sequencialmente
    if level is not None and level >= 0:
        spells = [spell for spell in spells if spell.nivel == level]
    
    if school and school.strip():
        spells = [spell for spell in spells if school.lower().strip() == spell.escola.lower()]
    
    if class_ and class_.strip():
        spells = [spell for spell in spells if any(class_.lower().strip() == c.lower() for c in spell.classes_conjuradoras)]
    
    if component and component.strip():
        spells = [spell for spell in spells if component.upper().strip() in spell.componentes]
    
    if ritual is not None:
        spells = [spell for spell in spells if spell.ritual == ritual]
    
    if concentration is not None:
        spells = [spell for spell in spells if spell.concentracao == concentration]
    
    if range_ and range_.strip():
        spells = [spell for spell in spells if range_.lower().strip() == spell.alcance.lower()]
    
    return spells

@router.get(
    "/spells/ritual",
    response_model=List[Spell],
    tags=["Magias"],
    summary="Magias rituais",
    description="""Lista todas as magias que podem ser conjuradas como ritual.

**O que são magias rituais?**
Magias rituais podem ser conjuradas sem gastar espaço de magia, mas levam 10 minutos a mais que o tempo normal de conjuração.

**Exemplos de magias rituais:**
- Detectar Magia
- Identificar
- Compreender Idiomas
- Alarme
- Purificar Comida e Bebida

**Vantagens:**
- Economia de espaços de magia
- Útil para magias de utilidade
- Pode ser conjurada fora de combate

**Desvantagens:**
- Tempo muito maior
- Não pode ser usado em combate"""
)
def get_ritual_spells():
    """Lista todas as magias que podem ser conjuradas como ritual."""
    spells = load_spells()
    ritual_spells = [spell for spell in spells if spell.ritual]
    return ritual_spells

@router.get(
    "/spells/concentracao",
    response_model=List[Spell],
    tags=["Magias"],
    summary="Magias de concentração",
    description="""Lista todas as magias que requerem concentração.

**O que são magias de concentração?**
Magias de concentração mantêm seu efeito ativo enquanto o conjurador mantém a concentração. Apenas uma magia de concentração pode estar ativa por vez.

**Regras importantes:**
- Apenas uma magia de concentração ativa por vez
- Concentração pode ser quebrada por dano
- Teste de resistência: CD = maior entre 10 e metade do dano recebido
- Ação para terminar concentração voluntariamente

**Exemplos de magias de concentração:**
- Invisibilidade
- Voo
- Parede de Fogo
- Proteção contra Mal e Bem
- Transformar-se

**Dicas de jogo:**
- Use magias de concentração para efeitos duradouros
- Proteja o conjurador para manter a concentração
- Tenha planos alternativos caso a concentração seja quebrada"""
)
def get_concentration_spells():
    """Lista todas as magias que requerem concentração."""
    spells = load_spells()
    concentration_spells = [spell for spell in spells if spell.concentracao]
    return concentration_spells

@router.get(
    "/spells/nivel/{nivel}",
    response_model=List[Spell],
    tags=["Magias"],
    summary="Magias por nível",
    description="""Lista todas as magias de um nível específico.

**Níveis de magia:**
- **0 (Truques):** Magias básicas que não consomem espaços de magia
- **1-3 (Baixos):** Magias de baixo nível, fundamentais para conjuradores
- **4-6 (Médios):** Magias intermediárias, mais poderosas
- **7-9 (Altos):** Magias de alto nível, extremamente poderosas

**Exemplos de uso:**
- `GET /spells/nivel/0` - Todos os truques
- `GET /spells/nivel/1` - Magias de 1º nível
- `GET /spells/nivel/3` - Magias de 3º nível (Bola de Fogo, etc.)
- `GET /spells/nivel/9` - Magias de 9º nível (Desejo, etc.)

**Dicas por nível:**
- **Nível 0:** Truques são essenciais para conjuradores
- **Nível 1:** Magias de cura e dano básico
- **Nível 3:** Magias de combate importantes (Bola de Fogo)
- **Nível 5:** Magias de grupo e controle
- **Nível 7-9:** Magias épicas e transformadoras"""
)
def get_spells_by_level(nivel: int):
    """Lista todas as magias de um nível específico."""
    spells = load_spells()
    filtered_spells = [spell for spell in spells if spell.nivel == nivel]
    if not filtered_spells:
        raise HTTPException(status_code=404, detail=f"Nenhuma magia encontrada para o nível {nivel}")
    return filtered_spells

@router.get(
    "/spells/escola/{escola}",
    response_model=List[Spell],
    tags=["Magias"],
    summary="Magias por escola",
    description="""Lista todas as magias de uma escola específica.

**Escolas de Magia:**

**Abjuração:** Magias de proteção e banimento
- Exemplos: Escudo, Proteção contra Mal e Bem, Dissipar Magia
- Foco: Defesa e remoção de efeitos mágicos

**Conjuração:** Magias de criação e teleporte
- Exemplos: Conjurar Elemental, Teleporte, Portal
- Foco: Criação de objetos e movimento instantâneo

**Divinação:** Magias de informação e previsão
- Exemplos: Detectar Magia, Identificar, Clarividência
- Foco: Obtenção de informações e visão do futuro

**Encantamento:** Magias de influência mental
- Exemplos: Charme Pessoa, Sussurro, Dominação
- Foco: Controle mental e influência social

**Evocação:** Magias de energia e dano
- Exemplos: Bola de Fogo, Raio, Cone de Frio
- Foco: Dano elemental e manipulação de energia

**Ilusão:** Magias de engano e invisibilidade
- Exemplos: Invisibilidade, Imagem Espelhada, Sombra Maior
- Foco: Engano e ocultação

**Necromancia:** Magias de morte e vida
- Exemplos: Reviver os Mortos, Animar Mortos, Drenar Vida
- Foco: Manipulação da vida e morte

**Transmutação:** Magias de transformação
- Exemplos: Transformar-se, Voo, Pedra para Carne
- Foco: Mudança de forma e propriedades

**Exemplos de uso:**
- `GET /spells/escola/Evocação` - Magias de dano
- `GET /spells/escola/Abjuração` - Magias de proteção
- `GET /spells/escola/Ilusão` - Magias de engano"""
)
def get_spells_by_school(escola: str):
    """Lista todas as magias de uma escola específica."""
    spells = load_spells()
    filtered_spells = [spell for spell in spells if escola.lower() in spell.escola.lower()]
    if not filtered_spells:
        raise HTTPException(status_code=404, detail=f"Nenhuma magia encontrada para a escola {escola}")
    return filtered_spells

@router.get(
    "/spells/classe/{classe}",
    response_model=List[Spell],
    tags=["Magias"],
    summary="Magias por classe",
    description="""Lista todas as magias que uma classe específica pode conjurar.

**Classes Conjuradoras:**

**Mago:** Conjurador arcano completo
- Habilidade: Inteligência
- Foco: Magias versáteis e poderosas
- Especialidade: Evocação e Ilusão

**Clérigo:** Conjurador divino completo
- Habilidade: Sabedoria
- Foco: Cura e proteção
- Especialidade: Abjuração e Evocação

**Druida:** Conjurador natural completo
- Habilidade: Sabedoria
- Foco: Natureza e transformação
- Especialidade: Conjuração e Transmutação

**Bardo:** Conjurador carismático
- Habilidade: Carisma
- Foco: Suporte e controle
- Especialidade: Encantamento e Ilusão

**Feiticeiro:** Conjurador inato
- Habilidade: Carisma
- Foco: Magias poderosas e metamágicas
- Especialidade: Evocação

**Warlock:** Conjurador pactuário
- Habilidade: Carisma
- Foco: Magias de curto alcance e invocações
- Especialidade: Evocação e Encantamento

**Paladino:** Conjurador divino parcial
- Habilidade: Carisma
- Foco: Proteção e combate
- Especialidade: Abjuração

**Ranger:** Conjurador natural parcial
- Habilidade: Sabedoria
- Foco: Sobrevivência e combate
- Especialidade: Conjuração

**Exemplos de uso:**
- `GET /spells/classe/Mago` - Magias do mago
- `GET /spells/classe/Clérigo` - Magias do clérigo
- `GET /spells/classe/Druida` - Magias do druida"""
)
def get_spells_by_class(classe: str):
    """Lista todas as magias que uma classe específica pode conjurar."""
    spells = load_spells()
    filtered_spells = [spell for spell in spells if classe.lower() in [c.lower() for c in spell.classes_conjuradoras]]
    if not filtered_spells:
        raise HTTPException(status_code=404, detail=f"Nenhuma magia encontrada para a classe {classe}")
    return filtered_spells

@router.get(
    "/spells/busca/{nome}",
    response_model=List[Spell],
    tags=["Magias"],
    summary="Busca magias por nome",
    description="""Busca magias que contenham o termo especificado no nome.

**Funcionalidades:**
- Busca case-insensitive (não diferencia maiúsculas/minúsculas)
- Busca parcial (encontra magias que contenham o termo)
- Suporte a acentos e caracteres especiais

**Exemplos de busca:**
- `GET /spells/busca/Bola` - Encontra "Bola de Fogo"
- `GET /spells/busca/fogo` - Encontra magias com "fogo" no nome
- `GET /spells/busca/curar` - Encontra magias de cura
- `GET /spells/busca/invis` - Encontra "Invisibilidade"
- `GET /spells/busca/raio` - Encontra magias com "raio"

**Dicas de busca:**
- Use termos em português
- Busque por elementos (fogo, gelo, raio)
- Busque por efeitos (curar, proteger, transformar)
- Busque por tipos (detectar, identificar, conjurar)

**Exemplos populares:**
- `GET /spells/busca/Bola` - Bola de Fogo
- `GET /spells/busca/Curar` - Curar Ferimentos
- `GET /spells/busca/Invis` - Invisibilidade
- `GET /spells/busca/Missil` - Mísseis Mágicos"""
)
def search_spells_by_name(nome: str):
    """Busca magias que contenham o termo especificado no nome."""
    spells = load_spells()
    filtered_spells = [spell for spell in spells if nome.lower() in spell.nome.lower()]
    if not filtered_spells:
        raise HTTPException(status_code=404, detail=f"Nenhuma magia encontrada contendo '{nome}'")
    return filtered_spells

@router.get(
    "/spells/classes/{class_name}",
    response_model=List[Spell],
    tags=["Magias"],
    summary="Lista de magias por classe",
    description="""Lista todas as magias conhecidas/preparadas por uma classe específica, baseado no PHB.

**Diferença do endpoint /spells/classe/{classe}:**
Este endpoint oferece mapeamento inteligente de nomes e suporte a variações, sendo mais flexível para uso em aplicações.

**Classes suportadas:**
- **Mago:** `mago`, `magos`
- **Clérigo:** `clerigo`, `clerigos`
- **Druida:** `druida`, `druidas`
- **Bardo:** `bardo`, `bardos`
- **Feiticeiro:** `feiticeiro`, `feiticeiros`
- **Warlock:** `warlock`, `warlocks`
- **Paladino:** `paladino`, `paladinos`
- **Ranger:** `ranger`, `rangers`

**Exemplos de uso:**
- `GET /spells/classes/mago` - Magias do mago
- `GET /spells/classes/clerigo` - Magias do clérigo
- `GET /spells/classes/clerigos` - Mesmo resultado (plural)
- `GET /spells/classes/druida` - Magias do druida

**Vantagens:**
- Suporte a variações de nomes
- Tratamento de acentos
- Mensagens de erro informativas
- Mapeamento inteligente

**Uso recomendado:**
Para aplicações que precisam de flexibilidade na entrada do usuário."""
)
def get_spells_by_class_name(class_name: str):
    """Lista todas as magias conhecidas/preparadas por uma classe específica."""
    spells = load_spells()
    
    # Normalizar o nome da classe para comparação
    class_name_lower = class_name.lower().strip()
    
    # Mapeamento de nomes de classes para variações aceitas
    class_mapping = {
        "mago": ["Mago"],
        "magos": ["Mago"],
        "clerigo": ["Clérigo"],
        "clerigos": ["Clérigo"],
        "druida": ["Druida"],
        "druidas": ["Druida"],
        "bardo": ["Bardo"],
        "bardos": ["Bardo"],
        "feiticeiro": ["Feiticeiro"],
        "feiticeiros": ["Feiticeiro"],
        "warlock": ["Warlock"],
        "warlocks": ["Warlock"],
        "paladino": ["Paladino"],
        "paladinos": ["Paladino"],
        "ranger": ["Ranger"],
        "rangers": ["Ranger"]
    }
    
    # Buscar a classe no mapeamento
    target_classes = class_mapping.get(class_name_lower, [class_name])
    
    # Filtrar magias que a classe pode conjurar
    filtered_spells = []
    for spell in spells:
        for target_class in target_classes:
            if any(target_class.lower() == c.lower() for c in spell.classes_conjuradoras):
                filtered_spells.append(spell)
                break
    
    if not filtered_spells:
        raise HTTPException(
            status_code=404, 
            detail=f"Nenhuma magia encontrada para a classe '{class_name}'. Classes disponíveis: Mago, Clérigo, Druida, Bardo, Feiticeiro, Warlock, Paladino, Ranger"
        )
    
    return filtered_spells

@router.get(
    "/spells/{spell_id}",
    response_model=Spell,
    tags=["Magias"],
    summary="Detalhes de uma magia",
    description="""Retorna todos os detalhes de uma magia pelo seu ID.

**Informações retornadas:**
- **Nome:** Nome da magia
- **Nível:** Nível da magia (0-9)
- **Escola:** Escola de magia
- **Tempo de Conjuração:** Tempo necessário para conjurar
- **Alcance:** Distância ou área de efeito
- **Componentes:** Componentes necessários (V, S, M)
- **Duração:** Quanto tempo o efeito dura
- **Classes Conjuradoras:** Quais classes podem conjurar
- **Texto:** Descrição completa da magia
- **Ritual:** Se pode ser conjurada como ritual
- **Concentração:** Se requer concentração
- **Material Específico:** Componente material específico (se houver)

**Exemplos de uso:**
- `GET /spells/1` - Detalhes da primeira magia
- `GET /spells/5` - Detalhes da quinta magia
- `GET /spells/25` - Detalhes da vigésima quinta magia

**IDs válidos:**
- IDs de 1 a 25 (baseado nas magias do PHB documentadas)
- Retorna 404 para IDs inválidos

**Uso típico:**
Após listar magias com filtros, use o ID para obter detalhes completos."""
)
def get_spell(spell_id: int):
    """Detalhes de uma magia pelo ID."""
    spells = load_spells()
    if 1 <= spell_id <= len(spells):
        return spells[spell_id - 1]
    raise HTTPException(status_code=404, detail="Magia não encontrada") 