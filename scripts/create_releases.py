#!/usr/bin/env python3
"""
Script para automatizar a criação de releases no GitHub usando GitHub CLI.
Baseado nos dados do arquivo routes/changelog.py
"""

import json
import subprocess
import sys
import os
from typing import List, Dict, Any
from datetime import datetime

# Importar os dados do changelog
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from routes.changelog import get_changelog_data

def run_gh_command(command: List[str]) -> str:
    """Executa um comando do GitHub CLI e retorna a saída."""
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

def format_changes_for_markdown(changes: List[Dict]) -> str:
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

def format_statistics(statistics: Dict[str, Any]) -> str:
    """Formata as estatísticas para markdown."""
    if not statistics:
        return ""
    
    markdown = "\n### 📊 Estatísticas da Versão\n\n"
    for key, value in statistics.items():
        markdown += f"- **{key.title()}:** {value}\n"
    
    return markdown

def create_release_notes(version_data) -> str:
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

def create_release(version_data, draft: bool = False, prerelease: bool = False):
    """Cria um release no GitHub."""
    version = version_data.version
    codename = version_data.codename
    
    print(f"🔄 Criando release v{version} - {codename}...")
    
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
            "--title", f"v{version} - {codename}",
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
            
    except Exception as e:
        print(f"❌ Erro ao criar release v{version}: {e}")
    finally:
        # Limpar arquivo temporário
        if os.path.exists(notes_file):
            os.remove(notes_file)

def list_existing_releases() -> List[str]:
    """Lista os releases existentes no GitHub."""
    result = run_gh_command(["release", "list", "--limit", "100"])
    if result:
        # Extrair tags dos releases existentes
        existing_tags = []
        for line in result.split('\n'):
            if line.strip():
                parts = line.split('\t')
                if len(parts) >= 1:
                    tag = parts[0].strip()
                    existing_tags.append(tag)
        return existing_tags
    return []

def main():
    """Função principal."""
    print("🚀 Script de Automação de Releases - D&D API")
    print("=" * 50)
    
    # Verificar se o GitHub CLI está instalado e autenticado
    print("🔍 Verificando GitHub CLI...")
    auth_result = run_gh_command(["auth", "status"])
    if not auth_result:
        print("❌ GitHub CLI não está autenticado. Execute 'gh auth login' primeiro.")
        return
    
    print("✅ GitHub CLI autenticado!")
    
    # Obter releases existentes
    print("📋 Verificando releases existentes...")
    existing_releases = list_existing_releases()
    print(f"📊 Releases existentes: {len(existing_releases)}")
    
    # Obter dados do changelog
    print("📖 Carregando dados do changelog...")
    versions = get_changelog_data()
    print(f"📊 Versões no changelog: {len(versions)}")
    
    # Mostrar menu de opções
    print("\n🎯 Opções disponíveis:")
    print("1. Criar release da versão mais recente")
    print("2. Criar release de uma versão específica")
    print("3. Criar releases de todas as versões (que não existem)")
    print("4. Listar releases existentes")
    print("5. Sair")
    
    while True:
        try:
            choice = input("\nEscolha uma opção (1-5): ").strip()
            
            if choice == "1":
                # Criar release da versão mais recente
                latest_version = versions[0]
                tag_name = f"v{latest_version.version}"
                
                if tag_name in existing_releases:
                    print(f"⚠️  Release {tag_name} já existe!")
                    overwrite = input("Deseja sobrescrever? (s/N): ").strip().lower()
                    if overwrite != 's':
                        continue
                
                create_release(latest_version)
                break
                
            elif choice == "2":
                # Criar release de uma versão específica
                print("\n📋 Versões disponíveis:")
                for i, version in enumerate(versions, 1):
                    tag_name = f"v{version.version}"
                    status = "✅" if tag_name in existing_releases else "❌"
                    print(f"{i}. {status} v{version.version} - {version.codename}")
                
                try:
                    version_choice = int(input("\nEscolha o número da versão: ")) - 1
                    if 0 <= version_choice < len(versions):
                        selected_version = versions[version_choice]
                        tag_name = f"v{selected_version.version}"
                        
                        if tag_name in existing_releases:
                            print(f"⚠️  Release {tag_name} já existe!")
                            overwrite = input("Deseja sobrescrever? (s/N): ").strip().lower()
                            if overwrite != 's':
                                continue
                        
                        create_release(selected_version)
                    else:
                        print("❌ Opção inválida!")
                except ValueError:
                    print("❌ Entrada inválida!")
                break
                
            elif choice == "3":
                # Criar releases de todas as versões que não existem
                print("\n🔄 Criando releases para versões que não existem...")
                created_count = 0
                
                for version in versions:
                    tag_name = f"v{version.version}"
                    if tag_name not in existing_releases:
                        create_release(version)
                        created_count += 1
                    else:
                        print(f"⏭️  Release {tag_name} já existe, pulando...")
                
                print(f"\n✅ Processo concluído! {created_count} releases criados.")
                break
                
            elif choice == "4":
                # Listar releases existentes
                print("\n📋 Releases existentes:")
                if existing_releases:
                    for tag in existing_releases:
                        print(f"  - {tag}")
                else:
                    print("  Nenhum release encontrado.")
                break
                
            elif choice == "5":
                print("👋 Saindo...")
                break
                
            else:
                print("❌ Opção inválida! Escolha 1-5.")
                
        except KeyboardInterrupt:
            print("\n👋 Operação cancelada pelo usuário.")
            break
        except Exception as e:
            print(f"❌ Erro: {e}")

if __name__ == "__main__":
    main() 