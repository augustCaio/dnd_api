# Versão 1.3.0 — "Antecedentes & Personalidades"

Esta versão traz uma grande atualização focada na riqueza narrativa dos personagens, permitindo explorar e integrar os **Antecedentes** (Backgrounds) e suas **Personalidades** de forma estruturada e flexível.

## Novidades

- **Modelos completos de Antecedentes**: Todos os backgrounds do Livro do Jogador, com campos detalhados de proficiências, equipamentos, idiomas, habilidade especial e blocos de personalidade (traços, ideais, vínculos e defeitos).
- **Arquivo backgrounds.json**: Base de dados estruturada e pronta para uso, facilitando consultas e integrações.
- **Endpoints RESTful**:
  - `GET /backgrounds`: Lista todos os antecedentes, com filtros por nome, proficiência e ideal.
  - `GET /backgrounds/{id}`: Detalhes completos de um antecedente.
  - `GET /backgrounds/{id}/traits`: Apenas os traços de personalidade do antecedente.
- **Filtros inteligentes**: Busque backgrounds por nome, proficiência ou ideal de forma simples e eficiente.
- **Documentação aprimorada**: Swagger UI com exemplos reais, descrições detalhadas e modelos claros para facilitar o uso da API.
- **Testes automáticos**: Cobertura dos principais endpoints e filtros, garantindo robustez e confiabilidade.

## Objetivo

Facilitar a criação, consulta e integração de antecedentes e personalidades de personagens de D&D 5e em sistemas, aplicativos e ferramentas de apoio ao mestre e jogadores.
