# D&D 5e Races API

API REST para consulta de raças do Dungeons & Dragons 5ª Edição, construída com FastAPI.

## Descrição

Esta API permite consultar todas as raças do Livro do Jogador de D&D 5e, incluindo sub-raças, características, bônus, idiomas e mais. Ideal para ferramentas, sites, bots ou integração com sistemas de RPG.

## Endpoints

### Listar todas as raças

```
GET /races
```

Retorna uma lista de todas as raças disponíveis.

### Buscar por nome

```
GET /races?name=anão
```

Busca raças cujo nome contenha o termo informado (ignora maiúsculas/minúsculas e acentos).

### Filtrar por tamanho

```
GET /races?size=médio
```

Filtra raças pelo campo de tamanho (ex: "médio", "pequeno").

### Combinar filtros

```
GET /races?name=elfo&size=médio
```

### Detalhes de uma raça

```
GET /races/{id}
```

Retorna todos os detalhes de uma raça específica pelo seu ID.

### Exemplo de resposta

```json
[
  {
    "id": 1,
    "nome": "Anão",
    "aumento_habilidade": "+2 Constituição",
    "idade": "Adultos aos 50 anos, vivem cerca de 350 anos",
    "alinhamento": "Tendem ao Leal",
    "tamanho": "Médio, entre 1,20 m e 1,50 m, 70 a 90 kg",
    "deslocamento": "7,5 m",
    "visao_no_escuro": "18 m",
    "proficiencias": ["Machado de batalha", "Machadinha"],
    "resiliencia": "Vantagem contra veneno e resistência a dano de veneno",
    "outras_caracteristicas": [
      "Escolha entre ferramentas de ferreiro, cervejeiro ou pedreiro"
    ],
    "idiomas": ["Comum", "Anão"],
    "subracas": [
      {
        "nome": "Anão da Colina",
        "bonus": "+1 Sabedoria",
        "descricao": "PV máximo aumenta em 1 por nível"
      }
    ]
  }
]
```

## Documentação Interativa

Acesse `/docs` após rodar o servidor para explorar e testar todos os endpoints via Swagger UI.

## Como rodar localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo
   ```
2. **Crie e ative um ambiente virtual (opcional):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Rode o servidor:**
   ```bash
   uvicorn main:app --reload
   ```
5. **Acesse:**
   - http://localhost:8000/races
   - http://localhost:8000/docs

## Testes automatizados

Execute todos os testes com:

```bash
pytest test_races.py
```

Os testes cobrem todos os endpoints, filtros, casos de erro, campos opcionais e busca flexível.

## Deploy com Docker

1. **Build da imagem:**
   ```bash
   docker build -t dnd-api .
   ```
2. **Rode o container:**
   ```bash
   docker run -d -p 8000:8000 dnd-api
   ```
3. **Acesse:** http://localhost:8000

## Deploy na Render

- Suba o projeto para o GitHub.
- Crie um novo Web Service na [Render](https://render.com/), selecione "Docker" e siga as instruções.
- O serviço será exposto em uma URL pública.

## Estrutura dos Dados

Os dados das raças estão em `data/races.json` e seguem o modelo Pydantic definido em `models/race.py`.

## Contribuindo

Pull requests são bem-vindos! Para contribuir:

- Crie uma branch para sua feature/correção.
- Adicione testes para novas funcionalidades.
- Descreva claramente sua proposta no PR.

## Licença

Este projeto é open-source e sem fins lucrativos, feito para a comunidade de RPG.
