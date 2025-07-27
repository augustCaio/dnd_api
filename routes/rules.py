from fastapi import APIRouter, Query
from typing import List, Optional
import json
from models.rule import Rule

router = APIRouter()

with open('data/rules.json', encoding='utf-8') as f:
    rules_data = json.load(f)

with open('data/combat_rules.json', encoding='utf-8') as f:
    combat_rules_data = json.load(f)

@router.get('/rules', response_model=List[Rule], tags=["Regras"], summary="Listar regras gerais", description="Retorna uma lista de regras gerais aplicáveis a testes, CD, vantagem/desvantagem, passivo, ajuda, etc.")
def list_rules(type: Optional[str] = Query(None, description="Filtrar por tipo de regra, ex: exaustao, percepcao")):
    results = rules_data
    if type:
        results = [r for r in results if type.lower() in r['nome'].lower()]
    return results 

@router.get('/rules/combat', tags=["Regras de Combate"], summary="Listar regras de combate", description="Retorna uma lista de regras específicas de combate. Permite filtrar por tipo.")
def list_combat_rules(type: Optional[str] = Query(None, description="Filtrar por tipo de regra, ex: iniciativa, rodada, dano")):
    results = combat_rules_data
    if type:
        results = [r for r in results if type.lower() in r['tipo'].lower()]
    return results

@router.get('/rules/spells', tags=["Regras de Conjuração"], summary="Regras gerais de conjuração", description="""Retorna as regras gerais de conjuração de magias, incluindo espaços de magia, preparação, habilidade de conjuração e mais.

**Conteúdo incluído:**
- Espaços de Magia e como são consumidos
- Preparação e conjuração de magias
- Habilidades de conjuração por classe
- Conjuração com armadura
- Cálculo de CD de magia
- Ataques mágicos
- Magia em combate
- Escolha de alvos
- Contra magia e interrupções
- Magia e ambiente

**Exemplos de uso:**
- `GET /rules/spells` - Todas as regras gerais
- Use como referência durante o jogo
- Consulte para esclarecer dúvidas sobre conjuração

**Regras importantes:**
- CD = 8 + bônus de proficiência + modificador da habilidade
- Ataques mágicos: 1d20 + modificador + proficiência
- Apenas uma magia de concentração por vez
- Magias podem gerar ataques de oportunidade"""
)
def get_spellcasting_rules():
    """Regras gerais de conjuração de magias."""
    spellcasting_rules = {
        "titulo": "Regras Gerais de Conjuração",
        "descricao": "Fundamentos da conjuração de magias em D&D 5e",
        "regras": [
            {
                "nome": "Espaços de Magia",
                "descricao": "Cada magia exige um espaço de determinado nível. Um espaço é consumido ao conjurar uma magia.",
                "detalhes": "Magias de nível 1+ consomem espaços de magia. Truques (nível 0) não consomem espaços."
            },
            {
                "nome": "Preparar e Conjurar Magias",
                "descricao": "Algumas classes preparam magias diariamente (como clérigos e druidas), outras aprendem um número fixo (como feiticeiros e bardos).",
                "detalhes": "Classes preparadoras: Clérigo, Druida, Paladino, Ranger. Classes espontâneas: Bardo, Feiticeiro, Warlock, Mago (prepara mas tem número fixo)."
            },
            {
                "nome": "Habilidade de Conjuração",
                "descricao": "Determina a CD para resistência contra magias e o bônus de ataque mágico. Varia por classe.",
                "detalhes": "INT (Mago), SAB (Clérigo, Druida, Ranger), CAR (Bardo, Feiticeiro, Warlock, Paladino)."
            },
            {
                "nome": "Conjurar com Armadura",
                "descricao": "Algumas classes (como magos) não conseguem conjurar com armadura sem proficiência.",
                "detalhes": "Verificar proficiência em armadura da classe antes de conjurar."
            },
            {
                "nome": "CD da Magia",
                "descricao": "CD = 8 + bônus de proficiência + modificador da habilidade de conjuração",
                "detalhes": "Usado para determinar se criaturas resistem aos efeitos das magias."
            },
            {
                "nome": "Ataques Mágicos",
                "descricao": "Usam 1d20 + modificador da habilidade + proficiência (se aplicável)",
                "detalhes": "Para magias que exigem ataques, como Bola de Fogo e Raio."
            },
            {
                "nome": "Magia em Combate",
                "descricao": "Pode provocar ataques de oportunidade se conjurada em alcance corpo a corpo.",
                "detalhes": "Conjurar magias em alcance de ataque corpo a corpo pode gerar ataques de oportunidade."
            },
            {
                "nome": "Escolhendo Alvos",
                "descricao": "Magias exigem alvos válidos e visíveis, a critério do Mestre.",
                "detalhes": "Algumas magias afetam áreas inteiras sem exigir ataque ou resistência."
            },
            {
                "nome": "Contra Magia e Interrupções",
                "descricao": "Contra magia pode anular magias em conjuração. Dissipar magia remove efeitos mágicos ativos.",
                "detalhes": "Reação que pode ser usada para tentar anular magias sendo conjuradas."
            },
            {
                "nome": "Magia e Ambiente",
                "descricao": "Algumas magias não funcionam em certas áreas (ex: campo antimagia).",
                "detalhes": "Verificar se o ambiente permite conjuração de magias."
            }
        ]
    }
    return spellcasting_rules

@router.get('/rules/spells/components', tags=["Regras de Conjuração"], summary="Componentes de magia", description="""Explica os três tipos de componentes de magia: Verbal (V), Somático (S) e Material (M).

**Componentes de Magia:**

**Verbal (V):**
- Requer fala audível
- Palavras específicas devem ser pronunciadas
- Magias silenciosas não podem ser conjuradas se o conjurador não puder falar
- Exemplos: Palavras arcanas, orações, comandos mágicos

**Somático (S):**
- Requer gestos livres com as mãos
- Gestos específicos devem ser realizados
- Magias somáticas não podem ser conjuradas se as mãos estiverem ocupadas
- Exemplos: Gestos arcanos, sinais sagrados, movimentos específicos

**Material (M):**
- Requer componentes físicos ou foco arcano/símbolo sagrado
- Se o componente tem custo, deve ser fornecido
- Focos podem substituir componentes sem custo
- Exemplos: Pó de diamante, ervas específicas, foco arcano

**Notas importantes:**
- Focos arcanos substituem componentes materiais sem custo
- Símbolos sagrados substituem componentes para clérigos e paladinos
- Componentes com custo específico devem ser fornecidos mesmo com foco
- Componentes são consumidos apenas se especificado na descrição da magia"""
)
def get_spell_components():
    """Explicação dos componentes de magia."""
    components_rules = {
        "titulo": "Componentes de Magia",
        "descricao": "Os três tipos de componentes necessários para conjurar magias",
        "componentes": [
            {
                "tipo": "Verbal (V)",
                "descricao": "Requer fala audível",
                "detalhes": "Palavras específicas devem ser pronunciadas de forma clara e audível. Magias silenciosas não podem ser conjuradas se o conjurador não puder falar.",
                "exemplos": "Palavras arcanas, orações, comandos mágicos"
            },
            {
                "tipo": "Somático (S)",
                "descricao": "Requer gestos livres com as mãos",
                "detalhes": "Gestos específicos devem ser realizados com pelo menos uma mão livre. Magias somáticas não podem ser conjuradas se as mãos estiverem ocupadas ou amarradas.",
                "exemplos": "Gestos arcanos, sinais sagrados, movimentos específicos"
            },
            {
                "tipo": "Material (M)",
                "descricao": "Requer componentes físicos, que podem ser substituídos por foco arcano ou símbolo sagrado",
                "detalhes": "Componentes físicos específicos ou um foco arcano/símbolo sagrado. Se o componente tem custo, deve ser fornecido. Focos podem substituir componentes sem custo.",
                "exemplos": "Pó de diamante, ervas específicas, foco arcano, símbolo sagrado"
            }
        ],
        "notas_importantes": [
            "Focos arcanos substituem componentes materiais sem custo",
            "Símbolos sagrados substituem componentes materiais para clérigos e paladinos",
            "Componentes com custo específico devem ser fornecidos mesmo com foco",
            "Componentes são consumidos apenas se especificado na descrição da magia"
        ]
    }
    return components_rules

@router.get('/rules/spells/rituals', tags=["Regras de Conjuração"], summary="Magias rituais", description="""Explica a diferença entre magia normal e ritual, incluindo tempo de conjuração e custo.

**Magias Rituais:**

**Conjuração Normal:**
- Magias conjuradas normalmente gastam um espaço de magia
- Tempo de conjuração padrão (geralmente 1 ação)
- Consome espaço de magia do nível apropriado

**Conjuração Ritual:**
- Magias rituais podem ser conjuradas sem gastar espaço de magia
- Tempo de conjuração + 10 minutos
- Não consome espaço de magia

**Requisitos para Ritual:**
- A magia deve ter a tag 'ritual'
- O personagem deve ter a habilidade de ritual
- Classes preparadoras podem conjurar qualquer magia conhecida como ritual
- Classes espontâneas precisam ter a magia preparada

**Vantagens dos Rituais:**
- Economia de espaços de magia
- Útil para magias de utilidade
- Ideal para magias como Detectar Magia, Identificar, Compreender Idiomas

**Desvantagens dos Rituais:**
- Tempo muito maior
- Não pode ser usado em combate
- Rituais são impraticáveis durante combate

**Exemplos de magias rituais:**
- Detectar Magia
- Identificar
- Compreender Idiomas
- Alarme
- Purificar Comida e Bebida"""
)
def get_spell_rituals():
    """Diferença entre magia normal e ritual."""
    ritual_rules = {
        "titulo": "Magias Rituais",
        "descricao": "Algumas magias podem ser conjuradas como rituais, sem gastar espaço de magia",
        "regras": [
            {
                "nome": "Conjuração Normal",
                "descricao": "Magias conjuradas normalmente gastam um espaço de magia do nível apropriado",
                "detalhes": "Tempo de conjuração padrão (geralmente 1 ação), consome espaço de magia"
            },
            {
                "nome": "Conjuração Ritual",
                "descricao": "Magias rituais podem ser conjuradas sem gastar espaço de magia, mas levam mais tempo",
                "detalhes": "Tempo de conjuração + 10 minutos, não consome espaço de magia"
            },
            {
                "nome": "Requisitos para Ritual",
                "descricao": "A magia deve ter a tag 'ritual' e o personagem deve ter a habilidade de ritual",
                "detalhes": "Classes preparadoras podem conjurar qualquer magia conhecida como ritual. Classes espontâneas precisam ter a magia preparada."
            },
            {
                "nome": "Tempo de Conjuração",
                "descricao": "Rituais levam 10 minutos a mais que o tempo normal de conjuração",
                "detalhes": "Exemplo: Magia de 1 ação + 10 minutos = 10 minutos e 1 ação"
            },
            {
                "nome": "Vantagens dos Rituais",
                "descricao": "Economia de espaços de magia, útil para magias de utilidade",
                "detalhes": "Ideal para magias como Detectar Magia, Identificar, Compreender Idiomas"
            },
            {
                "nome": "Desvantagens dos Rituais",
                "descricao": "Tempo muito maior, não pode ser usado em combate",
                "detalhes": "Rituais são impraticáveis durante combate devido ao tempo necessário"
            }
        ],
        "exemplos_rituais": [
            "Detectar Magia",
            "Identificar", 
            "Compreender Idiomas",
            "Alarme",
            "Purificar Comida e Bebida"
        ]
    }
    return ritual_rules

@router.get('/rules/spells/slot-table', tags=["Regras de Conjuração"], summary="Tabela de espaços de magia", description="""Tabela de espaços de magia por nível de personagem e classe conjuradora.

**Tabela de Espaços de Magia:**

**Conjuradores Completos:**
- **Mago:** Conjurador arcano completo, acesso a magias de 1º a 9º nível
- **Clérigo:** Conjurador divino completo, acesso a magias de 1º a 9º nível
- **Druida:** Conjurador natural completo, acesso a magias de 1º a 9º nível

**Conjuradores Parciais:**
- **Paladino:** Conjurador divino parcial, menos espaços
- **Ranger:** Conjurador natural parcial, menos espaços

**Conjuradores Espontâneos:**
- **Bardo:** Conjurador carismático, tabela similar
- **Feiticeiro:** Conjurador inato, tabela similar
- **Warlock:** Conjurador pactuário, tabela similar

**Notas importantes:**
- Esta tabela mostra os espaços para conjuradores completos
- Conjuradores parciais têm menos espaços
- Conjuradores espontâneos seguem tabelas similares
- Truques (nível 0) não consomem espaços de magia

**Uso da tabela:**
- Linha = Nível do personagem (1-20)
- Coluna = Nível da magia (1-9)
- Valor = Número de espaços disponíveis

**Exemplo:**
- Mago nível 5: 4 espaços de 1º nível, 3 espaços de 2º nível, 2 espaços de 3º nível"""
)
def get_spell_slot_table():
    """Tabela de espaços de magia por nível e classe."""
    slot_table = {
        "titulo": "Tabela de Espaços de Magia",
        "descricao": "Número de espaços de magia disponíveis por nível de personagem e classe conjuradora",
        "classes": {
            "Mago": {
                "descricao": "Conjurador completo, acesso a magias de 1º a 9º nível",
                "tabela": {
                    "1": {"1": 2, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "2": {"1": 3, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "3": {"1": 4, "2": 2, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "4": {"1": 4, "2": 3, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "5": {"1": 4, "2": 3, "3": 2, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "6": {"1": 4, "2": 3, "3": 3, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "7": {"1": 4, "2": 3, "3": 3, "4": 1, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "8": {"1": 4, "2": 3, "3": 3, "4": 2, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "9": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 1, "6": 0, "7": 0, "8": 0, "9": 0},
                    "10": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 0, "7": 0, "8": 0, "9": 0},
                    "11": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 0, "8": 0, "9": 0},
                    "12": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 0, "8": 0, "9": 0},
                    "13": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 0, "9": 0},
                    "14": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 0, "9": 0},
                    "15": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 1, "9": 0},
                    "16": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 1, "9": 0},
                    "17": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 1, "9": 1},
                    "18": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 1, "9": 1},
                    "19": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 1, "9": 1},
                    "20": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 1, "9": 1}
                }
            },
            "Clérigo": {
                "descricao": "Conjurador completo, acesso a magias de 1º a 9º nível",
                "tabela": {
                    "1": {"1": 2, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "2": {"1": 3, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "3": {"1": 4, "2": 2, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "4": {"1": 4, "2": 3, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "5": {"1": 4, "2": 3, "3": 2, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "6": {"1": 4, "2": 3, "3": 3, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "7": {"1": 4, "2": 3, "3": 3, "4": 1, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "8": {"1": 4, "2": 3, "3": 3, "4": 2, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "9": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 1, "6": 0, "7": 0, "8": 0, "9": 0},
                    "10": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 0, "7": 0, "8": 0, "9": 0},
                    "11": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 0, "8": 0, "9": 0},
                    "12": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 0, "8": 0, "9": 0},
                    "13": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 0, "9": 0},
                    "14": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 0, "9": 0},
                    "15": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 1, "9": 0},
                    "16": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 1, "9": 0},
                    "17": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 1, "9": 1},
                    "18": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 1, "9": 1},
                    "19": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 1, "9": 1},
                    "20": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 1, "9": 1}
                }
            },
            "Druida": {
                "descricao": "Conjurador completo, acesso a magias de 1º a 9º nível",
                "tabela": {
                    "1": {"1": 2, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "2": {"1": 3, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "3": {"1": 4, "2": 2, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "4": {"1": 4, "2": 3, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "5": {"1": 4, "2": 3, "3": 2, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "6": {"1": 4, "2": 3, "3": 3, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "7": {"1": 4, "2": 3, "3": 3, "4": 1, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "8": {"1": 4, "2": 3, "3": 3, "4": 2, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
                    "9": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 1, "6": 0, "7": 0, "8": 0, "9": 0},
                    "10": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 0, "7": 0, "8": 0, "9": 0},
                    "11": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 0, "8": 0, "9": 0},
                    "12": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 0, "8": 0, "9": 0},
                    "13": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 0, "9": 0},
                    "14": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 0, "9": 0},
                    "15": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 1, "9": 0},
                    "16": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 1, "9": 0},
                    "17": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 1, "9": 1},
                    "18": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 1, "9": 1},
                    "19": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 1, "9": 1},
                    "20": {"1": 4, "2": 3, "3": 3, "4": 3, "5": 2, "6": 1, "7": 1, "8": 1, "9": 1}
                }
            }
        },
        "notas": [
            "Esta tabela mostra os espaços de magia para conjuradores completos (Mago, Clérigo, Druida)",
            "Conjuradores parciais (Paladino, Ranger) têm menos espaços",
            "Conjuradores espontâneos (Bardo, Feiticeiro, Warlock) seguem tabelas similares",
            "Truques (nível 0) não consomem espaços de magia"
        ]
    }
    return slot_table 