# 🤖 Automação de Releases - D&D API

Este documento explica como usar os scripts de automação para criar releases no GitHub usando o GitHub CLI, baseado nos dados do arquivo `routes/changelog.py`.

## 📋 Pré-requisitos

1. **GitHub CLI instalado e configurado**

   ```bash
   # Instalar GitHub CLI (Windows)
   winget install GitHub.cli

   # Ou baixar de: https://cli.github.com/
   ```

2. **Autenticação no GitHub CLI**

   ```bash
   gh auth login
   ```

3. **Python 3.7+ instalado**

## 🚀 Scripts Disponíveis

### 1. `create_releases.py` - Script Interativo

Script completo com menu interativo para gerenciar releases.

**Uso:**

```bash
python create_releases.py
```

**Funcionalidades:**

- ✅ Criar release da versão mais recente
- ✅ Criar release de uma versão específica
- ✅ Criar releases de todas as versões (que não existem)
- ✅ Listar releases existentes
- ✅ Verificação de releases duplicados
- ✅ Opção de sobrescrever releases existentes

### 2. `create_single_release.py` - Script Direto

Script simples para criar um release específico via linha de comando.

**Uso:**

```bash
# Criar release normal
python create_single_release.py 2.4.0

# Criar release como draft
python create_single_release.py 2.4.0 --draft

# Criar release como prerelease
python create_single_release.py 2.4.0 --prerelease

# Combinar flags
python create_single_release.py 2.4.0 --draft --prerelease
```

### 3. `create_all_releases.py` - Script em Lote

Script para criar todos os releases de uma vez. Útil para repositórios novos ou sincronização completa.

**Uso:**

```bash
# Criar todos os releases que não existem
python create_all_releases.py

# Criar todos como drafts
python create_all_releases.py --draft

# Criar todos como prereleases
python create_all_releases.py --prerelease

# Sobrescrever releases existentes
python create_all_releases.py --force

# Combinar flags
python create_all_releases.py --draft --force
```

## 📊 Estrutura dos Releases

Os releases são criados automaticamente com base nos dados do `routes/changelog.py` e incluem:

### 📋 Informações Básicas

- **Versão:** Número da versão (ex: 2.4.0)
- **Nome código:** Nome descritivo da versão
- **Data de lançamento:** Data formatada em português
- **Descrição:** Descrição geral da versão

### 🔄 Mudanças

- **Categorizadas por tipo:**

  - ✨ **feature:** Novos recursos
  - 🚀 **improvement:** Melhorias
  - 🐛 **fix:** Correções
  - 💥 **breaking:** Mudanças que quebram compatibilidade

- **Detalhes específicos:** Lista de itens para cada mudança

### 📊 Estatísticas

- **Endpoints:** Quantidade de endpoints
- **Recursos:** Quantidade de recursos específicos
- **Testes:** Quantidade de testes

### 🎯 Seções Adicionais

- **Como usar:** Links para endpoints da API
- **Documentação:** Referência para documentação

## 🔧 Exemplos de Uso

### Exemplo 1: Criar Release da Versão Mais Recente

```bash
python create_releases.py
# Escolher opção 1
```

### Exemplo 2: Criar Release Específico

```bash
python create_single_release.py 2.4.0
```

### Exemplo 3: Criar Release como Draft

```bash
python create_single_release.py 2.4.0 --draft
```

### Exemplo 4: Criar Todos os Releases

```bash
python create_releases.py
# Escolher opção 3
```

### Exemplo 5: Criar Todos os Releases em Lote

```bash
python create_all_releases.py
```

### Exemplo 6: Criar Todos os Releases como Drafts

```bash
python create_all_releases.py --draft
```

## 📝 Formato do Release

O release criado terá o seguinte formato:

```markdown
# Release v2.4.0 - Apêndice E: Leitura Inspiradora

**Data de Lançamento:** 27 de Dezembro de 2024

## 📋 Descrição

Feature release com sistema completo de leituras inspiradoras...

## 🔄 Mudanças

### ✨ Sistema de Leitura Inspiradora

- 36 leituras inspiradoras com influências documentadas
- Obras literárias, mitologias e suas influências em D&D
- Filtros por categoria, autor e influência
- Endpoints especializados para categorias e autores

### 🚀 Documentação e Estatísticas Atualizadas

- Estatísticas atualizadas para incluir leituras inspiradoras
- Documentação Swagger aprimorada para novo sistema
- Exemplos práticos para todos os novos endpoints
- Guias de uso para mestres e jogadores

## 📊 Estatísticas da Versão

- **Endpoints:** 35+
- **Leituras:** 36
- **Tests:** 385+

## 🎯 Como Usar

Esta versão está disponível através dos endpoints da API:

- **Changelog completo:** `GET /changelog`
- **Versão atual:** `GET /changelog/latest`
- **Detalhes desta versão:** `GET /changelog/2.4.0`

## 📚 Documentação

Para mais informações sobre esta versão, consulte a documentação da API em `/docs`.

---

_Release criado automaticamente via GitHub CLI_
```

## 🛠️ Comandos GitHub CLI Utilizados

Os scripts utilizam os seguintes comandos do GitHub CLI:

### Verificar Autenticação

```bash
gh auth status
```

### Listar Releases Existentes

```bash
gh release list --limit 100
```

### Criar Release

```bash
gh release create v2.4.0 --title "v2.4.0 - Apêndice E: Leitura Inspiradora" --notes-file release_notes.md
```

### Criar Release como Draft

```bash
gh release create v2.4.0 --title "v2.4.0 - Apêndice E: Leitura Inspiradora" --notes-file release_notes.md --draft
```

### Criar Release como Prerelease

```bash
gh release create v2.4.0 --title "v2.4.0 - Apêndice E: Leitura Inspiradora" --notes-file release_notes.md --prerelease
```

## 🔍 Troubleshooting

### Erro: "GitHub CLI não está autenticado"

```bash
gh auth login
```

### Erro: "Versão não encontrada no changelog"

Verifique se a versão existe no arquivo `routes/changelog.py`

### Erro: "Release já existe"

Use a opção de sobrescrever ou escolha uma versão diferente

### Erro: "Comando gh não encontrado"

Instale o GitHub CLI:

```bash
# Windows
winget install GitHub.cli

# macOS
brew install gh

# Linux
sudo apt install gh
```

## 📈 Versões Disponíveis

As seguintes versões estão disponíveis no changelog:

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
- **v1.0.0:** Raças (Fundação da API)

## 🤝 Contribuição

Para adicionar novas versões ao sistema de releases:

1. Atualize o arquivo `routes/changelog.py`
2. Adicione a nova versão na função `get_changelog_data()`
3. Execute o script de automação para criar o release

## 📞 Suporte

Se encontrar problemas com os scripts:

1. Verifique se o GitHub CLI está instalado e autenticado
2. Confirme se a versão existe no changelog
3. Verifique as permissões do repositório
4. Consulte a documentação do GitHub CLI: https://cli.github.com/
