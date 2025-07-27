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
            version="2.4.0",
            release_date="2024-12-27",
            codename="Apêndice E: Leitura Inspiradora",
            description="Feature release com sistema completo de leituras inspiradoras que influenciaram D&D, incluindo obras literárias e mitologias.",
            changes=[
                VersionChange(
                    type="feature",
                    description="Sistema de Leitura Inspiradora",
                    details=[
                        "36 leituras inspiradoras com influências documentadas",
                        "Obras literárias, mitologias e suas influências em D&D",
                        "Filtros por categoria, autor e influência",
                        "Endpoints especializados para categorias e autores"
                    ]
                ),
                VersionChange(
                    type="improvement",
                    description="Documentação e Estatísticas Atualizadas",
                    details=[
                        "Estatísticas atualizadas para incluir leituras inspiradoras",
                        "Documentação Swagger aprimorada para novo sistema",
                        "Exemplos práticos para todos os novos endpoints",
                        "Guias de uso para mestres e jogadores"
                    ]
                )
            ],
            statistics={
                "endpoints": "35+",
                "leituras": "36",
                "tests": "385+"
            }
        ),
        Version(
            version="2.3.0",
            release_date="2024-12-27",
            codename="Apêndice D: Estatísticas de Criaturas",
            description="Feature release com sistema completo de criaturas do PHB com estatísticas detalhadas.",
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
                    type="improvement",
                    description="Cobertura de Testes Expandida",
                    details=[
                        "385+ testes cobrindo todos os sistemas da API",
                        "Testes específicos para criaturas",
                        "Validação de estrutura de dados e distribuições",
                        "Testes de filtros e casos de erro"
                    ]
                )
            ],
            statistics={
                "endpoints": "30+",
                "creatures": "32",
                "tests": "385+"
            }
        ),
        Version(
            version="2.2.0",
            release_date="2024-12-27",
            codename="Apêndice C: Planos de Existência",
            description="Feature release com sistema completo de planos de existência e suas características.",
            changes=[
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
                        "385+ testes cobrindo todos os sistemas da API",
                        "Testes específicos para planos",
                        "Validação de estrutura de dados e distribuições",
                        "Testes de filtros e casos de erro"
                    ]
                )
            ],
            statistics={
                "endpoints": "30+",
                "planes": "30",
                "tests": "385+"
            }
        ),
        Version(
            version="2.1.0",
            release_date="2024-12-27",
            codename="Deuses do Multiverso",
            description="Feature release com sistema completo de divindades de múltiplos panteões.",
            changes=[
                VersionChange(
                    type="feature",
                    description="Sistema de Divindades",
                    details=[
                        "85 divindades de múltiplos panteões",
                        "Filtros por panteão, domínio e alinhamento",
                        "Endpoints especializados para busca de divindades",
                        "Dados estruturados com símbolos e esferas de influência"
                    ]
                ),
                VersionChange(
                    type="improvement",
                    description="Cobertura de Testes Expandida",
                    details=[
                        "385+ testes cobrindo todos os sistemas da API",
                        "Testes específicos para divindades",
                        "Validação de estrutura de dados e distribuições",
                        "Testes de filtros e casos de erro"
                    ]
                )
            ],
            statistics={
                "endpoints": "30+",
                "deities": "85",
                "tests": "385+"
            }
        ),
        Version(
            version="2.0.0",
            release_date="2024-12-27",
            codename="Apêndice A: Condições",
            description="Feature release com sistema completo de condições de combate do PHB.",
            changes=[
                VersionChange(
                    type="feature",
                    description="Sistema de Condições Completo",
                    details=[
                        "14 condições oficiais do PHB documentadas",
                        "Efeitos mecânicos e interações detalhadas",
                        "Fontes comuns (magias, habilidades) para cada condição",
                        "Filtros por efeito e fonte"
                    ]
                ),
                VersionChange(
                    type="improvement",
                    description="Cobertura de Testes Expandida",
                    details=[
                        "385+ testes cobrindo todos os sistemas da API",
                        "Testes específicos para condições",
                        "Validação de estrutura de dados e distribuições",
                        "Testes de filtros e casos de erro"
                    ]
                )
            ],
            statistics={
                "endpoints": "30+",
                "conditions": "14",
                "tests": "385+"
            }
        ),
        Version(
            version="1.9.0",
            release_date="2024-12-27",
            codename="Capítulo 10: Conjuração",
            description="Feature release com sistema completo de magias e conjuração.",
            changes=[
                VersionChange(
                    type="feature",
                    description="Sistema de Magias",
                    details=[
                        "25 magias do Livro do Jogador implementadas",
                        "Filtros por classe, nível, escola, tempo de conjuração",
                        "Componentes, alcance e duração documentados",
                        "Sistema de ritual e concentração"
                    ]
                ),
                VersionChange(
                    type="improvement",
                    description="Documentação e Testes",
                    details=[
                        "Documentação Swagger completa para magias",
                        "Testes automatizados para todos os endpoints",
                        "Exemplos práticos para mestres e jogadores",
                        "Guias de uso para conjuração"
                    ]
                )
            ],
            statistics={
                "endpoints": "25+",
                "spells": "25",
                "tests": "200+"
            }
        ),
        Version(
            version="1.8.0",
            release_date="2024-12-27",
            codename="Capítulo 9: Combate",
            description="Feature release com sistema completo de regras de combate.",
            changes=[
                VersionChange(
                    type="feature",
                    description="Sistema de Combate",
                    details=[
                        "Estrutura de turnos, iniciativa e ações",
                        "Modelos para ações especiais (esquiva, desengajar, preparar)",
                        "Regras de ataque, cobertura, invisibilidade",
                        "Sistema de dano crítico e morte"
                    ]
                ),
                VersionChange(
                    type="improvement",
                    description="Documentação e Testes",
                    details=[
                        "Documentação Swagger completa para combate",
                        "Testes automatizados para todas as regras",
                        "Exemplos práticos para mestres",
                        "Guias de uso para combate"
                    ]
                )
            ],
            statistics={
                "endpoints": "20+",
                "combat_rules": "15+",
                "tests": "180+"
            }
        ),
        Version(
            version="1.7.0",
            release_date="2024-12-27",
            codename="Capítulo 8: Aventurando-se",
            description="Feature release com sistema completo de regras de aventura e exploração.",
            changes=[
                VersionChange(
                    type="feature",
                    description="Sistema de Aventura",
                    details=[
                        "Regras de viagem, descanso, nutrição, clima",
                        "Modelo para tipos de terreno e efeitos",
                        "Regras de peso, carga e exaustão",
                        "Sistema de visão e percepção"
                    ]
                ),
                VersionChange(
                    type="improvement",
                    description="Documentação e Testes",
                    details=[
                        "Documentação Swagger completa para aventura",
                        "Testes automatizados para todas as regras",
                        "Exemplos práticos para mestres",
                        "Guias de uso para exploração"
                    ]
                )
            ],
            statistics={
                "endpoints": "18+",
                "adventure_rules": "12+",
                "tests": "160+"
            }
        ),
        Version(
            version="1.6.0",
            release_date="2024-12-27",
            codename="Capítulo 7: Utilizando Habilidades",
            description="Feature release com sistema completo de perícias e testes de habilidade.",
            changes=[
                VersionChange(
                    type="feature",
                    description="Sistema de Perícias",
                    details=[
                        "Modelo de Perícias com atributos associados",
                        "Regras de testes de habilidade",
                        "Sistema de vantagem/desvantagem",
                        "Perícias por habilidade (ex: Atletismo = Força)"
                    ]
                ),
                VersionChange(
                    type="improvement",
                    description="Documentação e Testes",
                    details=[
                        "Documentação Swagger completa para perícias",
                        "Testes automatizados para todas as perícias",
                        "Exemplos práticos para mestres",
                        "Guias de uso para testes"
                    ]
                )
            ],
            statistics={
                "endpoints": "15+",
                "skills": "18",
                "tests": "140+"
            }
        ),
        Version(
            version="1.5.0",
            release_date="2024-12-27",
            codename="Capítulo 6: Opções de Personalização",
            description="Feature release com sistema completo de personalização de personagens.",
            changes=[
                VersionChange(
                    type="feature",
                    description="Sistema de Personalização",
                    details=[
                        "Modelo para Ajustes de Atributo",
                        "Integração com raça e antecedentes",
                        "Suporte para variantes de humanos",
                        "Sistema de talentos e feats"
                    ]
                ),
                VersionChange(
                    type="improvement",
                    description="Documentação e Testes",
                    details=[
                        "Documentação Swagger completa para personalização",
                        "Testes automatizados para todas as opções",
                        "Exemplos práticos para jogadores",
                        "Guias de uso para criação de personagens"
                    ]
                )
            ],
            statistics={
                "endpoints": "12+",
                "customization": "10+",
                "tests": "120+"
            }
        ),
        Version(
            version="1.4.0",
            release_date="2024-12-27",
            codename="Capítulo 5: Equipamento",
            description="Feature release com sistema completo de equipamentos, armas, armaduras e ferramentas.",
            changes=[
                VersionChange(
                    type="feature",
                    description="Sistema de Equipamento",
                    details=[
                        "Modelos para armas, armaduras, equipamentos",
                        "Ferramentas, montarias e veículos",
                        "JSONs com todos os itens do capítulo",
                        "Filtros por tipo, custo, peso e categoria"
                    ]
                ),
                VersionChange(
                    type="improvement",
                    description="Documentação e Testes",
                    details=[
                        "Documentação Swagger completa para equipamentos",
                        "Testes automatizados para todos os itens",
                        "Exemplos práticos para jogadores",
                        "Guias de uso para equipamentos"
                    ]
                )
            ],
            statistics={
                "endpoints": "10+",
                "equipment": "100+",
                "tests": "100+"
            }
        ),
        Version(
            version="1.3.0",
            release_date="2024-12-27",
            codename="Personalidades e Antecedentes",
            description="Feature release com sistema completo de antecedentes e personalidades.",
            changes=[
                VersionChange(
                    type="feature",
                    description="Sistema de Antecedentes",
                    details=[
                        "Modelos de Personalidade, Ideal, Vínculo, Defeito",
                        "Modelo e rotas para Antecedentes",
                        "Relacionamento entre Antecedentes e Personalidades",
                        "Sistema completo de backgrounds"
                    ]
                ),
                VersionChange(
                    type="improvement",
                    description="Documentação e Testes",
                    details=[
                        "Documentação Swagger completa para antecedentes",
                        "Testes automatizados para todos os backgrounds",
                        "Exemplos práticos para jogadores",
                        "Guias de uso para criação de personagens"
                    ]
                )
            ],
            statistics={
                "endpoints": "8+",
                "backgrounds": "13",
                "tests": "80+"
            }
        ),
        Version(
            version="1.2.0",
            release_date="2024-12-27",
            codename="Ordenação, Filtros e Testes",
            description="Feature release com sistema de filtros, ordenação e testes automatizados.",
            changes=[
                VersionChange(
                    type="feature",
                    description="Sistema de Filtros e Ordenação",
                    details=[
                        "Parâmetros de filtro e ordenação para recursos existentes",
                        "Sistema de busca avançada",
                        "Ordenação por múltiplos critérios",
                        "Filtros combinados"
                    ]
                ),
                VersionChange(
                    type="feature",
                    description="Testes Automatizados",
                    details=[
                        "Testes automatizados (Pytest)",
                        "Cobertura completa de endpoints",
                        "Testes de filtros e ordenação",
                        "Validação de dados"
                    ]
                ),
                VersionChange(
                    type="improvement",
                    description="Documentação Swagger",
                    details=[
                        "Melhorias na documentação Swagger",
                        "Exemplos interativos",
                        "Descrições detalhadas",
                        "Guias de uso"
                    ]
                )
            ],
            statistics={
                "endpoints": "6+",
                "filters": "10+",
                "tests": "60+"
            }
        ),
        Version(
            version="1.1.0",
            release_date="2024-12-27",
            codename="Sub-raças",
            description="Feature release com sistema completo de sub-raças e relacionamentos.",
            changes=[
                VersionChange(
                    type="feature",
                    description="Sistema de Sub-raças",
                    details=[
                        "Modelo para Sub-raças",
                        "Relacionamento entre Raça e Sub-raça",
                        "Filtros por raça-mãe",
                        "JSON com sub-raças completas"
                    ]
                ),
                VersionChange(
                    type="improvement",
                    description="Documentação e Estrutura",
                    details=[
                        "Documentação Swagger para sub-raças",
                        "Estrutura de dados aprimorada",
                        "Relacionamentos bem definidos",
                        "Guias de uso para sub-raças"
                    ]
                )
            ],
            statistics={
                "endpoints": "4+",
                "subraces": "25+",
                "tests": "40+"
            }
        ),
        Version(
            version="1.0.0",
            release_date="2024-12-27",
            codename="Raças",
            description="Release inicial com estrutura base da API e sistema completo de raças.",
            changes=[
                VersionChange(
                    type="feature",
                    description="Estrutura Base da API",
                    details=[
                        "Estrutura base da API (FastAPI)",
                        "Sistema de roteamento",
                        "Documentação Swagger básica",
                        "Estrutura de dados JSON"
                    ]
                ),
                VersionChange(
                    type="feature",
                    description="Sistema de Raças",
                    details=[
                        "Modelo e rotas para Raças",
                        "JSON com dados completos das raças do Livro do Jogador",
                        "9 raças principais implementadas",
                        "Sistema de busca e filtros básicos"
                    ]
                ),
                VersionChange(
                    type="improvement",
                    description="Documentação Inicial",
                    details=[
                        "Documentação Swagger básica",
                        "Exemplos de uso",
                        "Estrutura de projeto",
                        "Guias de instalação"
                    ]
                )
            ],
            statistics={
                "endpoints": "2+",
                "races": "9",
                "tests": "20+"
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
- Histórico completo de todas as versões (1.0.0 a 2.4.0)
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
- **v2.4.0:** Apêndice E: Leitura Inspiradora
- **v2.3.0:** Apêndice D: Estatísticas de Criaturas
- **v2.2.0:** Apêndice C: Planos de Existência
- **v2.1.0:** Deuses do Multiverso
- **v2.0.0:** Apêndice A: Condições
- **v1.9.0:** Capítulo 10: Conjuração
- **v1.8.0:** Capítulo 9: Combate
- **v1.7.0:** Capítulo 8: Aventurando-se
- **v1.6.0:** Capítulo 7: Utilizando Habilidades
- **v1.5.0:** Capítulo 6: Opções de Personalização
- **v1.4.0:** Capítulo 5: Equipamento
- **v1.3.0:** Personalidades e Antecedentes
- **v1.2.0:** Ordenação, Filtros e Testes
- **v1.1.0:** Sub-raças
- **v1.0.0:** Raças (Fundação da API)"""
)
def get_changelog():
    """Retorna o changelog completo da API."""
    versions = get_changelog_data()
    return ChangelogResponse(
        current_version="2.4.0",
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
- Acesso rápido à versão atual (2.4.0)
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
- `GET /changelog/2.4.0` - Detalhes da versão atual
- `GET /changelog/2.3.0` - Detalhes da versão anterior
- `GET /changelog/2.2.0` - Detalhes da versão anterior
- `GET /changelog/2.1.0` - Detalhes da versão anterior
- `GET /changelog/2.0.0` - Detalhes da versão anterior
- `GET /changelog/1.9.0` - Detalhes da versão anterior
- `GET /changelog/1.8.0` - Detalhes da versão anterior
- `GET /changelog/1.7.0` - Detalhes da versão anterior
- `GET /changelog/1.6.0` - Detalhes da versão anterior
- `GET /changelog/1.5.0` - Detalhes da versão anterior
- `GET /changelog/1.4.0` - Detalhes da versão anterior
- `GET /changelog/1.3.0` - Detalhes da versão anterior
- `GET /changelog/1.2.0` - Detalhes da versão anterior
- `GET /changelog/1.1.0` - Detalhes da versão anterior
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
    
    # Se a versão não for encontrada, retorna 404
    from fastapi import HTTPException
    raise HTTPException(status_code=404, detail=f"Versão {version} não encontrada") 