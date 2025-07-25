# D&D 5e API — Equipamentos, Raças, Classes, Antecedentes e Mais!

![D&D 5e](https://img.shields.io/badge/D%26D-5e-red?style=for-the-badge) ![FastAPI](https://img.shields.io/badge/FastAPI-async%20python-green?style=for-the-badge) ![Testes Automatizados](https://img.shields.io/badge/Testes%20Automatizados-Pytest-blue?style=for-the-badge)

> **API RESTful completa para consulta de dados do Livro do Jogador de Dungeons & Dragons 5ª Edição.**

---

## ✨ O que esta API oferece?

- **Raças** e **Sub-raças** (com filtros avançados)
- **Classes** (com níveis, magias e habilidades)
- **Antecedentes** (com traços de personalidade, ideais, vínculos e defeitos)
- **Equipamentos de aventura**
- **Armas** (com propriedades e categorias)
- **Armaduras** (com tipos, CA, força mínima, penalidade)
- **Ferramentas** (kits, instrumentos musicais, artesão, etc.)
- **Montarias e Veículos**
- **Moedas, Serviços e Estilos de Vida**
- **Ações de Combate** (atacar, correr, esquivar, ações bônus, reações, etc.)
- **Condições de Combate** (cego, caído, enfeitiçado, etc.)
- **Regras detalhadas de Combate** (iniciativa, rodadas, tipos de ataque, dano, morte, cobertura, etc.)
- **Filtros inteligentes** em quase todos os endpoints
- **Documentação Swagger interativa e didática**
- **Testes automatizados cobrindo todas as rotas**

---

## 🚀 Como rodar localmente

```bash
# Clone o repositório
$ git clone <repo-url>
$ cd dnd_api

# (Opcional) Crie e ative um ambiente virtual
$ python -m venv venv
$ venv\Scripts\activate  # Windows

# Instale as dependências
$ pip install -r requirements.txt

# Rode o servidor
$ uvicorn main:app --reload
```

Acesse: [http://localhost:8000/docs](http://localhost:8000/docs) para explorar a documentação interativa!

---

## 📚 Endpoints Principais

### Root

```http
GET /
```

- Status e mensagem de boas-vindas.

### Raças

```http
GET /racas?name=elfo&size=médio
GET /racas/{race_id}
GET /racas/{race_id}/subracas
GET /subracas?name=alto
GET /subracas/{subrace_id}
```

- Filtros: nome, tamanho, característica, bônus, ordenação.

### Classes

```http
GET /classes
GET /classes/{class_id}
GET /classes/{class_id}/niveis
GET /classes/{class_id}/magias
```

- Filtros: magia, dado de vida, proficiência em armaduras.

### Antecedentes

```http
GET /backgrounds?name=acólito&prof=religião&ideal=tradição
GET /backgrounds/{id}
GET /backgrounds/{id}/traits
```

### Equipamentos

```http
GET /equipment?cost<=5PO&weight<=1
GET /equipment/{id}
```

### Armas

```http
GET /weapons?type=marcial&property=leve
GET /weapons/{id}
```

### Armaduras

```http
GET /armor?type=leve
GET /armor/{id}
```

### Ferramentas

```http
GET /tools?category=instrumento musical
GET /tools/{id}
```

### Montarias e Veículos

```http
GET /mounts
GET /mounts/{id}
```

### Moedas, Serviços e Estilos de Vida

```http
GET /currency
GET /services
GET /lifestyles
```

### Ações de Combate

```http
GET /actions
GET /actions?type=bônus
```

- Lista todas as ações possíveis no combate (atacar, correr, esquivar, conjurar magia, etc).
- Filtro por tipo: ação, bônus, reação, movimento...

#### Exemplo de resposta

```json
[
  {
    "nome": "Atacar",
    "tipo": "ação",
    "descricao": "Realiza um ataque corpo a corpo ou à distância contra um alvo.",
    "exemplos": ["Atacar com espada", "Atirar com arco"]
  },
  {
    "nome": "Ação Bônus",
    "tipo": "ação bônus",
    "descricao": "Algumas habilidades, magias ou talentos permitem ações bônus.",
    "exemplos": ["Ataque extra do Guerreiro", "Lançar magia de ação bônus"]
  }
]
```

### Condições de Combate

```http
GET /conditions
```

- Lista todas as condições de combate (cego, caído, enfeitiçado, imobilizado, invisível, paralisado, petrificado, surdo, etc).

#### Exemplo de resposta

```json
[
  {
    "nome": "Cego",
    "efeitos_mecanicos": [
      "Falha automaticamente em qualquer teste que dependa de visão.",
      "Testes de ataque contra a criatura têm vantagem.",
      "Testes de ataque da criatura têm desvantagem."
    ],
    "duracao_tipica": "Até curado ou fim do efeito"
  }
]
```

### Regras de Combate

```http
GET /rules/combat
GET /rules/combat?type=iniciativa
```

- Lista regras específicas de combate (iniciativa, rodadas, tipos de ataque, acertos críticos, dano, morte, cobertura, combate montado, subaquático e em massa).
- Filtro por tipo de regra.

#### Exemplo de resposta

```json
[
  {
    "tipo": "iniciativa",
    "descricao": "Cada criatura rola 1d20 + modificador de Destreza. A ordem determina quem age primeiro."
  },
  {
    "tipo": "acerto_critico",
    "descricao": "Um 20 natural no d20 acerta automaticamente e causa dano extra (rola-se o dano duas vezes)."
  }
]
```

---

## 🔎 Exemplos de Filtros Inteligentes

- **/weapons?type=marcial&property=leve** — Todas as armas marciais com propriedade "leve".
- **/armor?type=leve** — Todas as armaduras leves.
- **/equipment?cost<=5PO&weight<=1** — Equipamentos baratos e leves.
- **/tools?category=instrumento musical** — Só instrumentos musicais.
- **/backgrounds?prof=religião&ideal=tradição** — Antecedentes com proficiência em Religião e ideal Tradição.
- **/actions?type=bônus** — Todas as ações bônus.
- **/rules/combat?type=iniciativa** — Apenas regras de iniciativa.

---

## 🧪 Testes Automatizados

- Testes com **pytest** cobrindo todas as rotas, filtros e integridade dos dados.
- Para rodar:

```bash
pytest test_api.py
```

- Todos os testes devem passar sem warnings!

---

## 🖥️ Documentação Interativa

- Acesse `/docs` para explorar todos os endpoints, schemas, exemplos e testar requisições direto do navegador.
- Schemas detalhados, exemplos reais e descrições em português.
- **Novos endpoints de combate** já documentados e organizados por categoria!

---

## 💡 Diferenciais

- **Filtros avançados** em quase todos os recursos
- **Modelos Pydantic** com exemplos e descrições para Swagger
- **Dados fiéis ao Livro do Jogador (PHB)**, traduzidos e organizados
- **Pronto para deploy** (Dockerfile incluso)
- **Código limpo, modular e fácil de expandir**

---

## 📦 Schemas dos Novos Recursos de Combate

### Ações de Combate (`/actions`)

```json
{
  "nome": "Atacar",
  "tipo": "ação",
  "descricao": "Realiza um ataque corpo a corpo ou à distância contra um alvo.",
  "exemplos": ["Atacar com espada", "Atirar com arco"]
}
```

- **nome**: Nome da ação (ex: "Atacar", "Correr").
- **tipo**: Tipo da ação (ação, bônus, reação, movimento).
- **descricao**: Descrição resumida do efeito.
- **exemplos**: Exemplos de uso.

### Condições de Combate (`/conditions`)

```json
{
  "nome": "Cego",
  "efeitos_mecanicos": [
    "Falha automaticamente em qualquer teste que dependa de visão.",
    "Testes de ataque contra a criatura têm vantagem.",
    "Testes de ataque da criatura têm desvantagem."
  ],
  "duracao_tipica": "Até curado ou fim do efeito"
}
```

- **nome**: Nome da condição (ex: "Cego").
- **efeitos_mecanicos**: Lista de efeitos mecânicos.
- **duracao_tipica**: Duração padrão da condição.

### Regras de Combate (`/rules/combat`)

```json
{
  "tipo": "iniciativa",
  "descricao": "Cada criatura rola 1d20 + modificador de Destreza. A ordem determina quem age primeiro."
}
```

- **tipo**: Tipo da regra (ex: "iniciativa", "dano", "acerto_critico").
- **descricao**: Descrição detalhada da regra.

---

## 🤝 Como contribuir com recursos de combate

1. **Adicione novas ações, condições ou regras**

   - Edite os arquivos JSON em `data/actions.json`, `data/conditions.json` ou `data/combat_rules.json`.
   - Siga o formato dos exemplos acima.
   - Mantenha nomes e descrições em português claro e objetivo.

2. **Inclua testes automatizados**

   - Adicione ou edite funções de teste em `test_api.py`.
   - Teste novos endpoints, filtros ou validações de dados.

3. **Documente no README**

   - Se criar um novo tipo de recurso de combate, adicione exemplos de uso, filtros e schemas nesta documentação.

4. **Abra um Pull Request**

   - Descreva claramente o que foi adicionado ou alterado.
   - Se possível, inclua exemplos de resposta e instruções de uso.

5. **Dicas para contribuir com recursos de combate**
   - Use termos do D&D 5e traduzidos fielmente.
   - Prefira listas e descrições objetivas.
   - Sempre rode os testes antes de enviar seu PR.

---

## 📜 Licença

Este projeto é open-source, feito para a comunidade de RPG e sem fins lucrativos.

---

Bons jogos e ótimas aventuras! 🎲🧙‍♂️🐉
