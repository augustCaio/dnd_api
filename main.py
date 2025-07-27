from fastapi import FastAPI
from routes.races import router as races_router
from routes.classes import router as classes_router
from routes.backgrounds import router as backgrounds_router
from routes.equipment import router as equipment_router
from routes.weapons import router as weapons_router
from routes.armor import router as armor_router
from routes.tools import router as tools_router
from routes.mounts import router as mounts_router
from routes.feats import router as feats_router
from routes.multiclass import router as multiclass_router
from fastapi.responses import JSONResponse
from routes.abilities import router as abilities_router
from routes.skills import router as skills_router
from routes.rules import router as rules_router
from routes.travel import router as travel_router
from routes.rest import router as rest_router
from routes.environment import router as environment_router
from routes.actions import router as actions_router
from routes.conditions import router as conditions_router
from routes.spells import router as spells_router
from routes.deities import router as deities_router
from routes.planes import router as planes_router
from routes.creatures import router as creatures_router
from routes.leituras import router as leituras_router
from routes.changelog import router as changelog_router

# Definição das tags para Swagger
openapi_tags = [
    {"name": "Changelog", "description": "Histórico completo de versões da API com detalhes de mudanças, estatísticas e evolução do projeto. Inclui categorização por tipo de mudança e documentação de cada versão."},
    {"name": "Root", "description": "Endpoint raiz da API. Status e mensagem de boas-vindas."},
    {"name": "Raças", "description": "Consulta e filtros avançados para raças e sub-raças do Livro do Jogador."},
    {"name": "Sub-raças", "description": "Detalhes e busca de sub-raças."},
    {"name": "Classes", "description": "Consulta de classes, níveis, magias e habilidades."},
    {"name": "Antecedentes", "description": "Consulta de backgrounds, traços de personalidade, ideais, vínculos e defeitos."},
    {"name": "Equipamentos", "description": "Itens de aventura, mochilas, cordas, poções, etc."},
    {"name": "Armas", "description": "Armas simples, marciais, propriedades e categorias."},
    {"name": "Armaduras", "description": "Armaduras leves, médias, pesadas e escudos."},
    {"name": "Ferramentas", "description": "Kits, instrumentos musicais, ferramentas de artesão e ladrão."},
    {"name": "Montarias e Veículos", "description": "Cavalos, mulas, carroças, barcos, selas e equipamentos relacionados."},
    {"name": "Utilidades", "description": "Moedas, serviços, estilos de vida e outras tabelas auxiliares."},
    {"name": "Talentos", "description": "Consulta de talentos (feats), requisitos, efeitos e filtros por classe ou raça."},
    {"name": "Multiclasse", "description": "Regras e combinações possíveis de multiclasses, requisitos e filtros por classe base e desejada."},
    {"name": "Habilidades", "description": "Consulta das 6 habilidades principais do personagem: Força, Destreza, Constituição, Inteligência, Sabedoria e Carisma. Inclui usos e testes comuns."},
    {"name": "Perícias", "description": "Consulta de todas as perícias do sistema, habilidade associada e descrição. Permite filtro por habilidade."},
    {"name": "Regras", "description": "Regras gerais aplicáveis: testes, CD, vantagem/desvantagem, passivo, ajuda, testes resistidos, grupo e improvisação."},
    {"name": "Viagem", "description": "Ritmos de viagem, marcha forçada, navegação e regras de movimentação durante a exploração."},
    {"name": "Descanso", "description": "Regras de descanso curto, longo, exaustão, fome e sede."},
    {"name": "Ambiente", "description": "Condições ambientais: terreno, visibilidade, clima, obstáculos e ambientes especiais."},
    {"name": "Ações", "description": "Ações de combate disponíveis: atacar, correr, esquivar, usar objeto, ações bônus, reações, etc. Permite filtro por tipo."},
    {"name": "Condições", "description": "Sistema completo de condições de combate com 14 condições do PHB. Inclui filtros por efeito e fonte, busca por nome, e documentação detalhada com exemplos práticos para uso durante o jogo."},
    {"name": "Regras de Combate", "description": "Regras específicas de combate: iniciativa, rodadas, tipos de ataque, acertos críticos, dano, morte, cobertura, combate montado, subaquático e em massa."},
    {"name": "Magias", "description": "Consulta de magias por nível, escola, classe conjuradora, componentes, ritual, concentração e outros critérios. Inclui truques e magias de 1º a 9º nível."},
    {"name": "Divindades", "description": "Sistema de divindades com panteões, alinhamentos, domínios e símbolos sagrados. Inclui divindades Faerûnianas e outras."},
    {"name": "Planos", "description": "Sistema de planos de existência com tipos, alinhamentos, associações e criaturas típicas. Inclui planos Material, Elementais, Exteriores e Transitivos."},
    {"name": "Criaturas", "description": "Sistema de criaturas com estatísticas completas, ataques, sentidos e níveis de desafio. Inclui bestas, mortos-vivos, humanoides e outras criaturas do PHB."},
    {"name": "Leituras Inspiradoras", "description": "Sistema de leituras inspiradoras que influenciaram D&D. Inclui obras literárias, mitologias e suas influências específicas no jogo."}
]

app = FastAPI(
    title="D&D 5e API",
    description="""API RESTful para consulta de dados do Livro do Jogador de Dungeons & Dragons 5ª Edição.

## 📊 **Estatísticas da API**

- **30+ endpoints** organizados por categoria
- **14 condições** de combate documentadas
- **25 magias** com sistema completo
- **85 divindades** de múltiplos panteões
- **30 planos** de existência
- **32 criaturas** com estatísticas completas
- **36 leituras inspiradoras** com influências documentadas
- **100% compatível** com Pydantic V2

## 🎮 **Casos de Uso**

- **Durante o jogo:** Consulta rápida de regras e condições
- **Criação de personagens:** Referência completa de raças, classes e equipamentos
- **Mestres:** Ferramenta de consulta durante sessões
- **Desenvolvedores:** API robusta para aplicações D&D

## 📖 **Documentação**

- **Swagger UI:** `/docs` - Documentação interativa completa
- **ReDoc:** `/redoc` - Documentação alternativa
- **OpenAPI JSON:** `/openapi.json` - Especificação da API
- **Changelog:** `/changelog` - Histórico completo de versões

---""",
    version="2.4.0",
    openapi_tags=openapi_tags
)

@app.get("/", tags=["Root"], summary="Root", description="Endpoint raiz da API. Retorna status, versão e informações sobre a API.")
def root():
    return JSONResponse({
        "status": "ok",
        "version": "2.4.0",
        "mensagem": "🎲 API D&D 5e v2.4 está funcionando! ✨",
        "changelog": {
            "latest_version": "2.4.0",
            "release_date": "2024-12-27",
            "highlights": [
                "Sistema de Leituras Inspiradoras (36 leituras)",
                "Sistema de Criaturas Completo (32 criaturas)",
                "Sistema de Planos de Existência (30 planos)",
                "Sistema de Condições Completo (14 condições)",
                "Sistema de Magias Expandido (25 magias)",
                "Sistema de Divindades (85 divindades)"
            ]
        },
        "statistics": {
            "endpoints": "30+",
            "conditions": "14",
            "spells": "25",
            "deities": "85",
            "planes": "30",
            "creatures": "32",
            "leituras": "36",
            "pydantic_compatibility": "100%"
        },
        "documentation": {
            "swagger": "/docs",
            "redoc": "/redoc",
            "openapi": "/openapi.json"
        }
    })

app.include_router(races_router)
app.include_router(classes_router)
app.include_router(backgrounds_router)
app.include_router(equipment_router)
app.include_router(weapons_router)
app.include_router(armor_router)
app.include_router(tools_router)
app.include_router(mounts_router)
app.include_router(feats_router)
app.include_router(multiclass_router)
app.include_router(abilities_router)
app.include_router(skills_router)
app.include_router(rules_router)
app.include_router(travel_router)
app.include_router(rest_router)
app.include_router(environment_router)
app.include_router(actions_router)
app.include_router(conditions_router)
app.include_router(spells_router)
app.include_router(deities_router)
app.include_router(planes_router)
app.include_router(creatures_router)
app.include_router(leituras_router)
app.include_router(changelog_router) 