# 🤖 Scripts de Automação - D&D API

Esta pasta contém scripts para automatizar tarefas relacionadas ao desenvolvimento e manutenção da API D&D.

## 📁 Arquivos Disponíveis

### 🚀 Scripts de Release

| Script                       | Descrição                                 | Uso                                     |
| ---------------------------- | ----------------------------------------- | --------------------------------------- |
| `create_releases.py`         | Script interativo para gerenciar releases | `python create_releases.py`             |
| `create_single_release.py`   | Criar um release específico               | `python create_single_release.py 2.4.0` |
| `create_all_releases.py`     | Criar todos os releases de uma vez        | `python create_all_releases.py`         |
| `test_release_automation.py` | Testar a automação de releases            | `python test_release_automation.py`     |

### 📋 Scripts de Teste

| Script        | Descrição     | Uso                  |
| ------------- | ------------- | -------------------- |
| `test_api.py` | Testes da API | `python test_api.py` |

## 🚀 Quick Start

### 1. Testar a Automação

```bash
python test_release_automation.py
```

### 2. Criar Release da Versão Mais Recente

```bash
python create_single_release.py 2.4.0
```

### 3. Criar Todos os Releases

```bash
python create_all_releases.py
```

## 📚 Documentação Completa

Para informações detalhadas sobre os scripts de automação de releases, consulte:

- [RELEASE_AUTOMATION.md](../RELEASE_AUTOMATION.md)

## 🔧 Pré-requisitos

- Python 3.7+
- GitHub CLI instalado e autenticado
- Acesso ao repositório

## 🛠️ Instalação

1. **Instalar GitHub CLI:**

   ```bash
   winget install GitHub.cli
   ```

2. **Autenticar no GitHub:**

   ```bash
   gh auth login
   ```

3. **Verificar instalação:**
   ```bash
   python test_release_automation.py
   ```

## 📊 Status dos Scripts

| Script                       | Status         | Testes      |
| ---------------------------- | -------------- | ----------- |
| `create_releases.py`         | ✅ Funcionando | ✅ Passando |
| `create_single_release.py`   | ✅ Funcionando | ✅ Passando |
| `create_all_releases.py`     | ✅ Funcionando | ✅ Passando |
| `test_release_automation.py` | ✅ Funcionando | ✅ Passando |

## 🤝 Contribuição

Para adicionar novos scripts:

1. Crie o script na pasta `scripts/`
2. Adicione documentação no README
3. Teste o script antes de commitar
4. Atualize esta documentação

## 📞 Suporte

Se encontrar problemas:

1. Execute `python test_release_automation.py` para diagnosticar
2. Verifique se o GitHub CLI está autenticado
3. Consulte a documentação completa em `RELEASE_AUTOMATION.md`
4. Abra uma issue no repositório
