# 🎲 D&D 5e API - Versão 2.0

API RESTful completa para consulta de dados do Livro do Jogador de Dungeons & Dragons 5ª Edição.

## 🚀 Novidades da Versão 2.0

### ✨ Sistema de Condições Completo

- **14 condições** do PHB com efeitos detalhados
- **Filtros avançados** por efeito e fonte
- **Busca inteligente** por nome
- **Documentação completa** com exemplos práticos

### 🔮 Sistema de Magias Aprimorado

- **25 magias** traduzidas do PHB
- **Filtros múltiplos** por nível, escola, classe
- **Endpoints especializados** para rituais e concentração
- **Regras de conjuração** detalhadas

### 📚 Documentação Swagger Melhorada

- **Exemplos práticos** para cada endpoint
- **Categorização** por tipo de funcionalidade
- **Guias de uso** para jogadores e mestres
- **Casos de teste** comuns

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

### 🎭 Condições (NOVO!)

- **14 condições** do PHB
- **Filtros por efeito:** desvantagem, vantagem, ataque, movimento
- **Filtros por fonte:** magia, veneno, trauma
- **Busca por nome:** case-insensitive com suporte a acentos

### 🔮 Magias (APRIMORADO!)

- **25 magias** traduzidas
- **Filtros múltiplos:** nível, escola, classe, componentes
- **Endpoints especializados:** rituais, concentração, por classe
- **Regras de conjuração:** componentes, espaços, CD

## 🛠️ Tecnologias

- **FastAPI** - Framework web moderno
- **Pydantic** - Validação de dados
- **Python 3.13** - Linguagem principal
- **JSON** - Armazenamento de dados

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

#### 🎭 Condições (NOVO!)

```http
GET /conditions                    # Lista todas as condições
GET /conditions?effect=desvantagem # Filtra por efeito
GET /conditions?source=magia       # Filtra por fonte
GET /conditions/1                  # Detalhes da condição
GET /conditions/busca/cego         # Busca por nome
```

#### 🔮 Magias

```http
GET /spells                        # Lista todas as magias
GET /spells?level=3&class=mago     # Filtros múltiplos
GET /spells/ritual                 # Magias rituais
GET /spells/concentracao           # Magias de concentração
GET /spells/classes/mago           # Magias por classe
```

#### 🏃‍♂️ Raças e Classes

```http
GET /racas                         # Lista todas as raças
GET /classes                       # Lista todas as classes
GET /backgrounds                   # Lista todos os antecedentes
```

#### ⚔️ Equipamentos

```http
GET /weapons                       # Lista todas as armas
GET /armor                         # Lista todas as armaduras
GET /equipment                     # Lista todos os equipamentos
```

### Exemplos de Uso

#### Buscar condições que causam desvantagem

```bash
curl "http://localhost:8000/conditions?effect=desvantagem"
```

#### Buscar magias de evocação do mago

```bash
curl "http://localhost:8000/spells?school=Evocação&class=mago"
```

#### Buscar armas corpo a corpo

```bash
curl "http://localhost:8000/weapons?type=Corpo a Corpo"
```

## 🧪 Testes

Execute os testes automatizados:

```bash
pytest test_api.py -v
```

## 📊 Estrutura do Projeto

```
dnd_api/
├── data/                 # Dados JSON
│   ├── conditions.json   # 14 condições do PHB
│   ├── spells.json       # 25 magias traduzidas
│   ├── races.json        # Raças e sub-raças
│   └── ...
├── models/               # Modelos Pydantic
│   ├── condition.py      # Modelo de condições
│   ├── spell.py          # Modelo de magias
│   └── ...
├── routes/               # Endpoints da API
│   ├── conditions.py     # Rotas de condições
│   ├── spells.py         # Rotas de magias
│   └── ...
├── main.py              # Aplicação principal
├── test_api.py          # Testes automatizados
└── requirements.txt     # Dependências
```

## 🎮 Casos de Uso

### Para Jogadores

- **Durante o combate:** Consulta rápida de condições e efeitos
- **Criação de personagens:** Referência completa de raças, classes e equipamentos
- **Preparação de magias:** Sistema completo de magias com filtros

### Para Mestres

- **Consultas rápidas:** Regras de combate, viagem, descanso
- **Referência:** Condições, magias, equipamentos
- **Ferramenta de jogo:** API para aplicações D&D

### Para Desenvolvedores

- **API RESTful:** Endpoints bem documentados
- **Dados estruturados:** JSON com validação Pydantic
- **Documentação interativa:** Swagger/OpenAPI

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

**🎯 Versão 2.0 - Sistema completo de condições e magias aprimorado!** ✨
