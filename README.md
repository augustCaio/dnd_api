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

---

## 🔎 Exemplos de Filtros Inteligentes

- **/weapons?type=marcial&property=leve** — Todas as armas marciais com propriedade "leve".
- **/armor?type=leve** — Todas as armaduras leves.
- **/equipment?cost<=5PO&weight<=1** — Equipamentos baratos e leves.
- **/tools?category=instrumento musical** — Só instrumentos musicais.
- **/backgrounds?prof=religião&ideal=tradição** — Antecedentes com proficiência em Religião e ideal Tradição.

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

---

## 💡 Diferenciais

- **Filtros avançados** em quase todos os recursos
- **Modelos Pydantic** com exemplos e descrições para Swagger
- **Dados fiéis ao Livro do Jogador (PHB)**, traduzidos e organizados
- **Pronto para deploy** (Dockerfile incluso)
- **Código limpo, modular e fácil de expandir**

---

## 🤝 Contribua!

Pull requests são bem-vindos! Sugestões, correções e novas features são sempre apreciadas.

1. Crie uma branch para sua feature/correção
2. Adicione testes para novas funcionalidades
3. Descreva claramente sua proposta no PR

---

## 📜 Licença

Este projeto é open-source, feito para a comunidade de RPG e sem fins lucrativos.

---

Bons jogos e ótimas aventuras! 🎲🧙‍♂️🐉
