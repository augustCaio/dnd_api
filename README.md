# 🎲 D&D 5e API - Versão 2.4.0

API RESTful completa para consulta de dados do Livro do Jogador de Dungeons & Dragons 5ª Edição.

## 🚀 Novidades da Versão 2.4.0

### 📚 Sistema de Leituras Inspiradoras (NOVO!)

- **36 leituras inspiradoras** que influenciaram D&D
- **Obras literárias, mitologias** e suas influências específicas
- **Filtros por categoria, autor e influência**
- **Endpoints especializados** para categorias e autores

### 👹 Sistema de Criaturas Completo

- **32 criaturas** do PHB com estatísticas completas
- **Filtros por tipo, tamanho e nível de desafio**
- **Dados estruturados** com ataques, sentidos e atributos
- **Endpoints especializados** para categorias de criaturas

### 🌍 Sistema de Planos de Existência

- **30 planos** de existência com tipos e alinhamentos
- **Filtros por tipo** (Material, Interior, Exterior, Transitivo)
- **Busca por alinhamento** e associações divinas
- **Criaturas típicas** de cada plano documentadas

### 🛐 Sistema de Divindades Expandido

- **85 divindades** de múltiplos panteões
- **Filtros por panteão, domínio e alinhamento**
- **Endpoints especializados** para busca de divindades
- **Dados estruturados** com símbolos e esferas de influência

### 📋 Sistema de Changelog Completo

- **Histórico completo** de todas as versões (1.0.0 a 2.4.0)
- **15 versões documentadas** com detalhes específicos
- **Estatísticas por versão** e categorização por tipo de mudança
- **Documentação de evolução** da API

## 🎯 Funcionalidades Principais

### 🏃‍♂️ Raças e Classes

- Consulta completa de raças e sub-raças
- Classes com habilidades e progressão
- Filtros avançados por características
- Sistema de multiclasse

### ⚔️ Equipamentos

- **Armas:** Simples, marciais, propriedades especiais
- **Armaduras:** Leves, médias, pesadas, escudos
- **Ferramentas:** Kits, instrumentos, ferramentas especializadas
- **Montarias:** Cavalos, carroças, barcos

### 📖 Regras e Mecânicas

- **Combate:** Iniciativa, ações, cobertura
- **Viagem:** Ritmos, navegação, marcha forçada
- **Descanso:** Curto, longo, exaustão
- **Ambiente:** Terreno, clima, visibilidade

### 🎭 Condições

- **14 condições** do PHB
- **Filtros por efeito:** desvantagem, vantagem, ataque, movimento
- **Filtros por fonte:** magia, veneno, trauma
- **Busca por nome:** case-insensitive com suporte a acentos

### 🔮 Magias

- **25 magias** traduzidas
- **Filtros múltiplos:** nível, escola, classe, componentes
- **Endpoints especializados:** rituais, concentração, por classe
- **Regras de conjuração:** componentes, espaços, CD

### 📚 Leituras Inspiradoras (NOVO!)

- **36 leituras** que influenciaram D&D
- **Categorias:** Fantasia, Mitologia, Espada e Feitiçaria, Terror
- **Autores:** Tolkien, Lovecraft, Howard, Herbert e outros
- **Influências específicas:** Forgotten Realms, Ravenloft, etc.

### 👹 Criaturas (NOVO!)

- **32 criaturas** do PHB com estatísticas completas
- **Tipos:** Bestas, Mortos-vivos, Humanoides
- **Tamanhos:** Miúdo, Médio, Grande
- **Níveis de desafio:** 0 a 1/2

### 🌍 Planos de Existência (NOVO!)

- **30 planos** organizados por tipo
- **Tipos:** Material, Interior, Exterior, Transitivo
- **Alinhamentos:** Leal, Neutro, Caótico
- **Associações divinas** e criaturas típicas

### 🛐 Divindades (EXPANDIDO!)

- **85 divindades** de múltiplos panteões
- **Panteões:** Faerûn, Greyhawk, Nórdico, Grego, etc.
- **Domínios:** Vida, Morte, Guerra, Magia, etc.
- **Alinhamentos** e símbolos sagrados

## 🛠️ Tecnologias

- **FastAPI** - Framework web moderno
- **Pydantic V2** - Validação de dados otimizada
- **Python 3.13** - Linguagem principal
- **JSON** - Armazenamento de dados
- **Pytest** - Testes automatizados

## 🚀 Instalação e Uso

### Pré-requisitos

- Python 3.13+
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/augustCaio/dnd_api.git
cd dnd_api

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### Execução

```bash
# Inicie o servidor
python main.py

# Acesse a documentação
# http://localhost:8000/docs
# http://localhost:8000/redoc
```

## 📚 Documentação da API

### Endpoints Principais

#### 📚 Leituras Inspiradoras (NOVO!)

```http
GET /leituras                                    # Lista todas as leituras
GET /leituras?categoria=Fantasia                # Filtra por categoria
GET /leituras?autor=J.R.R. Tolkien              # Filtra por autor
GET /leituras?influencia=Forgotten Realms       # Filtra por influência
GET /leituras/senhor-dos-aneis                  # Detalhes específicos
GET /leituras/categorias/Mitologia              # Por categoria
GET /leituras/autores/H.P. Lovecraft            # Por autor
```

#### 👹 Criaturas (NOVO!)

```http
GET /criaturas                                  # Lista todas as criaturas
GET /criaturas?tipo=Besta                       # Filtra por tipo
GET /criaturas?tamanho=Miúdo                    # Filtra por tamanho
GET /criaturas?nd=1_4                           # Filtra por nível de desafio
GET /criaturas/gato                             # Detalhes específicos
GET /criaturas/tipos/Besta                      # Por tipo
GET /criaturas/tamanhos/Miúdo                   # Por tamanho
GET /criaturas/niveis/1_4                       # Por nível de desafio
```

#### 🌍 Planos de Existência (NOVO!)

```http
GET /planos                                     # Lista todos os planos
GET /planos?tipo=Material                       # Filtra por tipo
GET /planos?alinhamento=Neutro                  # Filtra por alinhamento
GET /planos?associado_a=Elementais              # Filtra por associação
GET /planos/plano-material                      # Detalhes específicos
GET /planos/tipos/Material                      # Por tipo
GET /planos/alinhamentos/Neutro                 # Por alinhamento
```

#### 🛐 Divindades

```http
GET /deuses                                     # Lista todas as divindades
GET /deuses?panteao=Faerûn                      # Filtra por panteão
GET /deuses?dominio=Vida                        # Filtra por domínio
GET /deuses?alinhamento=NB                      # Filtra por alinhamento
GET /deuses/lathander                           # Detalhes específicos
```

#### 🎭 Condições

```http
GET /conditions                                 # Lista todas as condições
GET /conditions?effect=desvantagem              # Filtra por efeito
GET /conditions?source=magia                    # Filtra por fonte
GET /conditions/1                               # Detalhes da condição
GET /conditions/busca/cego                      # Busca por nome
```

#### 🔮 Magias

```http
GET /spells                                     # Lista todas as magias
GET /spells?level=3&class=mago                  # Filtros múltiplos
GET /spells/ritual                              # Magias rituais
GET /spells/concentracao                        # Magias de concentração
GET /spells/classes/mago                        # Magias por classe
```

#### 🏃‍♂️ Raças e Classes

```http
GET /racas                                      # Lista todas as raças
GET /classes                                    # Lista todas as classes
GET /backgrounds                                # Lista todos os antecedentes
```

#### ⚔️ Equipamentos

```http
GET /weapons                                    # Lista todas as armas
GET /armor                                      # Lista todas as armaduras
GET /equipment                                  # Lista todos os equipamentos
```

#### 📋 Changelog (NOVO!)

```http
GET /changelog                                  # Histórico completo
GET /changelog/latest                           # Versão mais recente
GET /changelog/2.4.0                            # Detalhes específicos
```

### Exemplos de Uso

#### Buscar leituras de fantasia

```bash
curl "http://localhost:8000/leituras?categoria=Fantasia"
```

#### Buscar criaturas miúdas

```bash
curl "http://localhost:8000/criaturas?tamanho=Miúdo"
```

#### Buscar planos materiais

```bash
curl "http://localhost:8000/planos?tipo=Material"
```

#### Buscar divindades de vida

```bash
curl "http://localhost:8000/deuses?dominio=Vida"
```

#### Buscar condições que causam desvantagem

```bash
curl "http://localhost:8000/conditions?effect=desvantagem"
```

#### Buscar magias de evocação do mago

```bash
curl "http://localhost:8000/spells?school=Evocação&class=mago"
```

## 🧪 Testes

Execute os testes automatizados:

```bash
pytest test_api.py -v
```

**385+ testes** cobrindo todos os sistemas da API!

## 📊 Estrutura do Projeto

```
dnd_api/
├── data/                     # Dados JSON
│   ├── leituras.json        # 36 leituras inspiradoras
│   ├── criaturas.json       # 32 criaturas do PHB
│   ├── planos.json          # 30 planos de existência
│   ├── deuses.json          # 85 divindades
│   ├── conditions.json      # 14 condições do PHB
│   ├── spells.json          # 25 magias traduzidas
│   ├── races.json           # Raças e sub-raças
│   └── ...
├── models/                   # Modelos Pydantic
│   ├── leitura.py           # Modelo de leituras
│   ├── creature.py          # Modelo de criaturas
│   ├── plane.py             # Modelo de planos
│   ├── condition.py         # Modelo de condições
│   ├── spell.py             # Modelo de magias
│   └── ...
├── routes/                   # Endpoints da API
│   ├── leituras.py          # Rotas de leituras
│   ├── creatures.py         # Rotas de criaturas
│   ├── planes.py            # Rotas de planos
│   ├── changelog.py         # Sistema de changelog
│   ├── conditions.py        # Rotas de condições
│   ├── spells.py            # Rotas de magias
│   └── ...
├── main.py                  # Aplicação principal
├── test_api.py              # 385+ testes automatizados
└── requirements.txt         # Dependências
```

## 🎮 Casos de Uso

### Para Jogadores

- **Durante o combate:** Consulta rápida de condições e efeitos
- **Criação de personagens:** Referência completa de raças, classes e equipamentos
- **Preparação de magias:** Sistema completo de magias com filtros
- **Inspiração literária:** Leituras que influenciaram D&D

### Para Mestres

- **Consultas rápidas:** Regras de combate, viagem, descanso
- **Referência:** Condições, magias, equipamentos, criaturas
- **Mundo:** Planos de existência e divindades
- **Inspiração:** Leituras que moldaram o universo D&D
- **Ferramenta de jogo:** API para aplicações D&D

### Para Desenvolvedores

- **API RESTful:** 35+ endpoints bem documentados
- **Dados estruturados:** JSON com validação Pydantic V2
- **Documentação interativa:** Swagger/OpenAPI
- **Testes completos:** 385+ testes automatizados
- **Changelog detalhado:** Histórico completo de desenvolvimento

## 📈 Estatísticas da API

- **35+ endpoints** organizados por categoria
- **14 condições** de combate documentadas
- **25 magias** com sistema completo
- **85 divindades** de múltiplos panteões
- **30 planos** de existência
- **32 criaturas** com estatísticas completas
- **36 leituras inspiradoras** com influências documentadas
- **385+ testes** automatizados
- **100% compatível** com Pydantic V2

## 📋 Histórico de Versões

### v2.4.0 - Apêndice E: Leitura Inspiradora

- Sistema completo de leituras inspiradoras
- 36 obras literárias e mitologias
- Filtros por categoria, autor e influência

### v2.3.0 - Apêndice D: Estatísticas de Criaturas

- Sistema completo de criaturas do PHB
- 32 criaturas com estatísticas detalhadas
- Filtros por tipo, tamanho e nível de desafio

### v2.2.0 - Apêndice C: Planos de Existência

- Sistema de planos de existência
- 30 planos com tipos e alinhamentos
- Criaturas típicas de cada plano

### v2.1.0 - Deuses do Multiverso

- Sistema de divindades expandido
- 85 divindades de múltiplos panteões
- Filtros por panteão, domínio e alinhamento

### v2.0.0 - Apêndice A: Condições

- Sistema completo de condições de combate
- 14 condições oficiais do PHB
- Efeitos mecânicos e interações detalhadas

### v1.9.0 - Capítulo 10: Conjuração

- Sistema de magias e conjuração
- 25 magias do Livro do Jogador
- Filtros por classe, nível, escola

### v1.8.0 - Capítulo 9: Combate

- Sistema de regras de combate
- Estrutura de turnos, iniciativa e ações
- Regras de ataque, cobertura, invisibilidade

### v1.7.0 - Capítulo 8: Aventurando-se

- Sistema de regras de aventura
- Viagem, descanso, nutrição, clima
- Regras de peso, carga e exaustão

### v1.6.0 - Capítulo 7: Utilizando Habilidades

- Sistema de perícias e testes
- Modelo de Perícias com atributos associados
- Regras de testes de habilidade

### v1.5.0 - Capítulo 6: Opções de Personalização

- Sistema de personalização de personagens
- Ajustes de Atributo e variantes
- Sistema de talentos e feats

### v1.4.0 - Capítulo 5: Equipamento

- Sistema completo de equipamentos
- Armas, armaduras, ferramentas, montarias
- Filtros por tipo, custo, peso

### v1.3.0 - Personalidades e Antecedentes

- Sistema de antecedentes e personalidades
- Modelos de Personalidade, Ideal, Vínculo, Defeito
- Relacionamento entre Antecedentes e Personalidades

### v1.2.0 - Ordenação, Filtros e Testes

- Sistema de filtros e ordenação
- Testes automatizados (Pytest)
- Melhorias na documentação Swagger

### v1.1.0 - Sub-raças

- Sistema de sub-raças e relacionamentos
- Modelo para Sub-raças
- Filtros por raça-mãe

### v1.0.0 - Raças

- Estrutura base da API (FastAPI)
- Sistema completo de raças
- 9 raças principais implementadas

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🎲 Sobre D&D 5e

Esta API é baseada no Livro do Jogador de Dungeons & Dragons 5ª Edição. Todos os dados são traduzidos e adaptados para uso em aplicações D&D.

---

**🎯 Versão 2.4.0 - Sistema completo com leituras inspiradoras, criaturas, planos e divindades!** ✨
