from fastapi import APIRouter
from typing import List, Dict, Any
from pydantic import BaseModel, Field

router = APIRouter()

class VersionChange(BaseModel):
    """Modelo para mudanças em uma versão."""
    type: str = Field(..., description="Tipo da mudança (feature, fix, improvement, breaking)")
    description: str = Field(..., description="Descrição da mudança")
    details: List[str] = Field(..., description="Detalhes específicos da mudança")

class Version(BaseModel):
    """Modelo para uma versão da API."""
    version: str = Field(..., description="Número da versão")
    release_date: str = Field(..., description="Data de lançamento")
    codename: str = Field(..., description="Nome código da versão")
    description: str = Field(..., description="Descrição geral da versão")
    changes: List[VersionChange] = Field(..., description="Lista de mudanças")
    statistics: Dict[str, Any] = Field(..., description="Estatísticas da versão")

class ChangelogResponse(BaseModel):
    """Modelo para resposta do changelog."""
    current_version: str = Field(..., description="Versão atual da API")
    total_versions: int = Field(..., description="Total de versões")
    versions: List[Version] = Field(..., description="Lista de todas as versões")

def get_changelog_data() -> List[Version]:
    """Retorna os dados do changelog."""
    return [
        Version(
            version="2.1.0",
            release_date="2024-12-27",
            codename="Sistema de Criaturas e Planos de Existência",
            description="Feature release com sistema completo de criaturas do PHB e planos de existência, além de testes abrangentes.",
            changes=[
                VersionChange(
                    type="feature",
                    description="Sistema de Criaturas Completo",
                    details=[
                        "32 criaturas do PHB com estatísticas completas",
                        "Filtros por tipo, tamanho e nível de desafio",
                        "Endpoints especializados para categorias de criaturas",
                        "Dados estruturados com ataques, sentidos e atributos"
                    ]
                ),
                VersionChange(
                    type="feature",
                    description="Sistema de Planos de Existência",
                    details=[
                        "30 planos de existência com tipos e alinhamentos",
                        "Filtros por tipo (Material, Interior, Exterior, Transitivo)",
                        "Busca por alinhamento e associações divinas",
                        "Criaturas típicas de cada plano documentadas"
                    ]
                ),
                VersionChange(
                    type="improvement",
                    description="Cobertura de Testes Expandida",
                    details=[
                        "220+ testes cobrindo todos os sistemas da API",
                        "Testes específicos para criaturas e planos",
                        "Validação de estrutura de dados e distribuições",
                        "Testes de filtros e casos de erro"
                    ]
                ),
                VersionChange(
                    type="improvement",
                    description="Documentação e Estatísticas Atualizadas",
                    details=[
                        "Estatísticas atualizadas para incluir criaturas e planos",
                        "Documentação Swagger aprimorada para novos sistemas",
                        "Exemplos práticos para todos os novos endpoints",
                        "Guias de uso para mestres e jogadores"
                    ]
                )
            ],
            statistics={
                "endpoints": "30+",
                "creatures": "32",
                "planes": "30",
                "tests": "220+"
            }
        ),
        Version(
            version="2.0.0",
            release_date="2024-12-27",
            codename="Sistema de Condições e Magias Aprimorado",
            description="Major release com sistemas completos de condições, magias e divindades, além de migração para Pydantic V2.",
            changes=[
                VersionChange(
                    type="feature",
                    description="Sistema de Condições Completo",
                    details=[
                        "14 condições do PHB com efeitos mecânicos detalhados",
                        "Filtros avançados por efeito aplicado e fonte",
                        "Busca inteligente por nome com suporte a acentos",
                        "Documentação completa com exemplos práticos"
                    ]
                ),
                VersionChange(
                    type="feature",
                    description="Sistema de Magias Expandido",
                    details=[
                        "25 magias traduzidas do PHB com dados completos",
                        "Filtros múltiplos por nível, escola, classe conjuradora",
                        "Endpoints especializados para rituais e concentração",
                        "Regras de conjuração detalhadas com componentes"
                    ]
                ),
                VersionChange(
                    type="feature",
                    description="Sistema de Divindades",
                    details=[
                        "85 divindades de múltiplos panteões (Faerûn, Grego, Nórdico, etc.)",
                        "Filtros por panteão, domínio e alinhamento",
                        "Busca por nome com suporte a caracteres especiais",
                        "Documentação detalhada com exemplos"
                    ]
                ),
                VersionChange(
                    type="improvement",
                    description="Documentação Swagger Aprimorada",
                    details=[
                        "Exemplos práticos para todos os endpoints",
                        "Categorização profissional por funcionalidade",
                        "Guias de uso específicos para jogadores e mestres",
                        "Casos de teste comuns documentados"
                    ]
                ),
                VersionChange(
                    type="improvement",
                    description="Compatibilidade Pydantic V2",
                    details=[
                        "Migração completa para Pydantic V2",
                        "Eliminação de todos os warnings de depreciação",
                        "Melhor performance e validação de dados",
                        "Estrutura de modelos otimizada"
                    ]
                ),
                VersionChange(
                    type="fix",
                    description="Correções e Otimizações",
                    details=[
                        "Resolução de conflitos de rotas em endpoints de magias",
                        "Correção de filtros para funcionamento correto",
                        "Ajuste de estrutura de dados para consistência",
                        "Otimização de queries e validações"
                    ]
                )
            ],
            statistics={
                "endpoints": "25+",
                "conditions": "14",
                "spells": "25",
                "deities": "85",
                "pydantic_compatibility": "100%"
            }
        ),
        Version(
            version="1.5.0",
            release_date="2024-12-20",
            codename="Sistema de Regras e Combate",
            description="Feature release com sistema completo de regras de combate, viagem, descanso e condições ambientais.",
            changes=[
                VersionChange(
                    type="feature",
                    description="Sistema de Regras de Combate",
                    details=[
                        "Regras específicas de combate: iniciativa, rodadas, tipos de ataque",
                        "Acertos críticos, dano, morte, cobertura",
                        "Combate montado, subaquático e em massa",
                        "Documentação completa com exemplos"
                    ]
                ),
                VersionChange(
                    type="feature",
                    description="Sistema de Viagem e Descanso",
                    details=[
                        "Ritmos de viagem e marcha forçada",
                        "Navegação e regras de movimentação",
                        "Regras de descanso curto e longo",
                        "Sistema de exaustão, fome e sede"
                    ]
                ),
                VersionChange(
                    type="feature",
                    description="Condições Ambientais",
                    details=[
                        "Condições ambientais: terreno, visibilidade, clima",
                        "Obstáculos e ambientes especiais",
                        "Ações de combate disponíveis",
                        "Sistema de habilidades e perícias"
                    ]
                )
            ],
            statistics={
                "endpoints": "20+",
                "combat_rules": "15+",
                "travel_rules": "8",
                "environment_rules": "12"
            }
        ),
        Version(
            version="1.0.0",
            release_date="2024-12-15",
            codename="Fundação da API",
            description="Initial release com sistemas base de raças, classes, equipamentos e ferramentas.",
            changes=[
                VersionChange(
                    type="feature",
                    description="Sistema de Raças e Classes",
                    details=[
                        "Sistema completo de raças e sub-raças",
                        "Classes com níveis, habilidades e magias",
                        "Antecedentes e talentos",
                        "Filtros avançados por características"
                    ]
                ),
                VersionChange(
                    type="feature",
                    description="Sistema de Equipamentos",
                    details=[
                        "Armas simples e marciais com propriedades",
                        "Armaduras leves, médias, pesadas e escudos",
                        "Ferramentas de artesão e ladrão",
                        "Montarias, veículos e equipamentos relacionados"
                    ]
                ),
                VersionChange(
                    type="feature",
                    description="Sistema de Utilidades",
                    details=[
                        "Moedas, serviços e estilos de vida",
                        "Tabelas auxiliares e referências",
                        "Multiclasse e combinações possíveis",
                        "Documentação base da API"
                    ]
                )
            ],
            statistics={
                "endpoints": "15+",
                "races": "9",
                "classes": "12",
                "equipment": "50+"
            }
        )
    ]

@router.get(
    "/changelog",
    response_model=ChangelogResponse,
    tags=["Changelog"],
    summary="Changelog Completo",
    description="""Retorna o changelog completo da API com todas as versões e suas mudanças.

**Funcionalidades:**
- Histórico completo de todas as versões
- Detalhes específicos de cada mudança
- Estatísticas por versão
- Categorização por tipo de mudança

**Tipos de Mudança:**
- **feature:** Novos recursos e funcionalidades
- **improvement:** Melhorias em recursos existentes
- **fix:** Correções de bugs e problemas
- **breaking:** Mudanças que quebram compatibilidade

**Exemplos de uso:**
- Consulta do histórico de desenvolvimento
- Referência para desenvolvedores
- Documentação de evolução da API
- Planejamento de migrações

**Versões disponíveis:**
- **v2.1.0:** Sistema de Criaturas e Planos de Existência
- **v2.0.0:** Sistema de Condições e Magias Aprimorado
- **v1.5.0:** Sistema de Regras e Combate
- **v1.0.0:** Fundação da API"""
)
def get_changelog():
    """Retorna o changelog completo da API."""
    versions = get_changelog_data()
    return ChangelogResponse(
        current_version="2.1.0",
        total_versions=len(versions),
        versions=versions
    )

@router.get(
    "/changelog/latest",
    response_model=Version,
    tags=["Changelog"],
    summary="Versão Mais Recente",
    description="""Retorna os detalhes da versão mais recente da API.

**Funcionalidades:**
- Acesso rápido à versão atual
- Destaques principais da versão
- Mudanças mais recentes
- Estatísticas atualizadas

**Uso típico:**
- Verificação da versão atual
- Destaques da versão mais recente
- Mudanças recentes
- Status da API"""
)
def get_latest_version():
    """Retorna a versão mais recente da API."""
    versions = get_changelog_data()
    return versions[0]  # A primeira versão é sempre a mais recente

@router.get(
    "/changelog/{version}",
    response_model=Version,
    tags=["Changelog"],
    summary="Detalhes de uma Versão",
    description="""Retorna os detalhes completos de uma versão específica.

**Informações retornadas:**
- Número da versão e data de lançamento
- Nome código e descrição geral
- Lista completa de mudanças
- Estatísticas da versão

**Exemplos de uso:**
- `GET /changelog/2.1.0` - Detalhes da versão atual
- `GET /changelog/2.0.0` - Detalhes da versão anterior
- `GET /changelog/1.5.0` - Detalhes da versão anterior
- `GET /changelog/1.0.0` - Detalhes da versão inicial

**Uso típico:**
- Consulta específica de uma versão
- Planejamento de migração
- Documentação de mudanças
- Referência para desenvolvedores"""
)
def get_version_details(version: str):
    """Retorna os detalhes de uma versão específica."""
    versions = get_changelog_data()
    for v in versions:
        if v.version == version:
            return v
    
    from fastapi import HTTPException
    raise HTTPException(
        status_code=404,
        detail=f"Versão '{version}' não encontrada. Versões disponíveis: {[v.version for v in versions]}"
    ) 