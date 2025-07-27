#!/usr/bin/env python3
"""
Script simples para criar um release específico via linha de comando.
Uso: python create_single_release.py <versão> [--draft] [--prerelease]
"""

import sys
import subprocess
import os
from datetime import datetime

# Importar os dados do changelog
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from routes.changelog import get_changelog_data

def run_gh_command(command):
    """Executa um comando do GitHub CLI."""
    try:
        result = subprocess.run(
            ["gh"] + command,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar comando gh: {e}")
        print(f"Stderr: {e.stderr}")
        return None

def format_changes_for_markdown(changes):
    """Formata as mudanças para markdown."""
    markdown = ""
    
    for change in changes:
        change_type = change.type
        description = change.description
        details = change.details
        
        # Emoji baseado no tipo de mudança
        emoji_map = {
            "feature": "✨",
            "improvement": "🚀",
            "fix": "🐛",
            "breaking": "💥"
        }
        emoji = emoji_map.get(change_type, "📝")
        
        markdown += f"\n### {emoji} {description}\n\n"
        
        for detail in details:
            markdown += f"- {detail}\n"
    
    return markdown

def format_statistics(statistics):
    """Formata as estatísticas para markdown."""
    if not statistics:
        return ""
    
    markdown = "\n### 📊 Estatísticas da Versão\n\n"
    for key, value in statistics.items():
        markdown += f"- **{key.title()}:** {value}\n"
    
    return markdown

def create_release_notes(version_data):
    """Cria as notas de release em markdown."""
    version = version_data.version
    codename = version_data.codename
    description = version_data.description
    release_date = version_data.release_date
    changes = version_data.changes
    statistics = version_data.statistics
    
    # Formatar a data
    try:
        date_obj = datetime.strptime(release_date, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%d de %B de %Y")
    except:
        formatted_date = release_date
    
    markdown = f"""# Release v{version} - {codename}

**Data de Lançamento:** {formatted_date}

## 📋 Descrição

{description}

## 🔄 Mudanças

{format_changes_for_markdown(changes)}

{format_statistics(statistics)}

## 🎯 Como Usar

Esta versão está disponível através dos endpoints da API:

- **Changelog completo:** `GET /changelog`
- **Versão atual:** `GET /changelog/latest`
- **Detalhes desta versão:** `GET /changelog/{version}`

## 📚 Documentação

Para mais informações sobre esta versão, consulte a documentação da API em `/docs`.

---
*Release criado automaticamente via GitHub CLI*
"""
    
    return markdown

def main():
    """Função principal."""
    if len(sys.argv) < 2:
        print("Uso: python create_single_release.py <versão> [--draft] [--prerelease]")
        print("Exemplo: python create_single_release.py 2.4.0")
        print("Exemplo: python create_single_release.py 2.4.0 --draft")
        sys.exit(1)
    
    version = sys.argv[1]
    draft = "--draft" in sys.argv
    prerelease = "--prerelease" in sys.argv
    
    print(f"🚀 Criando release v{version}...")
    
    # Verificar se o GitHub CLI está autenticado
    auth_result = run_gh_command(["auth", "status"])
    if not auth_result:
        print("❌ GitHub CLI não está autenticado. Execute 'gh auth login' primeiro.")
        sys.exit(1)
    
    # Obter dados do changelog
    versions = get_changelog_data()
    
    # Encontrar a versão especificada
    version_data = None
    for v in versions:
        if v.version == version:
            version_data = v
            break
    
    if not version_data:
        print(f"❌ Versão {version} não encontrada no changelog!")
        print("Versões disponíveis:")
        for v in versions:
            print(f"  - v{v.version} - {v.codename}")
        sys.exit(1)
    
    # Criar arquivo temporário com as notas de release
    release_notes = create_release_notes(version_data)
    notes_file = f"release_notes_{version}.md"
    
    try:
        with open(notes_file, "w", encoding="utf-8") as f:
            f.write(release_notes)
        
        # Comando base do GitHub CLI
        command = [
            "release", "create",
            f"v{version}",
            "--title", f"v{version} - {version_data.codename}",
            "--notes-file", notes_file
        ]
        
        # Adicionar flags opcionais
        if draft:
            command.append("--draft")
        if prerelease:
            command.append("--prerelease")
        
        # Executar o comando
        result = run_gh_command(command)
        
        if result:
            print(f"✅ Release v{version} criado com sucesso!")
            print(f"🔗 URL: {result}")
        else:
            print(f"❌ Erro ao criar release v{version}")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ Erro ao criar release v{version}: {e}")
        sys.exit(1)
    finally:
        # Limpar arquivo temporário
        if os.path.exists(notes_file):
            os.remove(notes_file)

if __name__ == "__main__":
    main() 