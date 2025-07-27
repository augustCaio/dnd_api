#!/usr/bin/env python3
"""
Script para criar todos os releases de uma vez.
Útil para repositórios novos ou quando você quer sincronizar todos os releases.
"""

import sys
import os
import subprocess
import time
from datetime import datetime

# Importar os dados do changelog
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from routes.changelog import get_changelog_data
from .create_single_release import create_release_notes, run_gh_command

def list_existing_releases():
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

def create_release(version_data, draft=False, prerelease=False):
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
            return True
        else:
            print(f"❌ Erro ao criar release v{version}")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao criar release v{version}: {e}")
        return False
    finally:
        # Limpar arquivo temporário
        if os.path.exists(notes_file):
            os.remove(notes_file)

def main():
    """Função principal."""
    print("🚀 Script de Criação de Todos os Releases - D&D API")
    print("=" * 60)
    
    # Verificar argumentos
    draft = "--draft" in sys.argv
    prerelease = "--prerelease" in sys.argv
    force = "--force" in sys.argv
    
    if draft:
        print("📝 Modo: Draft (releases serão criados como rascunhos)")
    if prerelease:
        print("🔬 Modo: Prerelease (releases serão marcados como pré-lançamento)")
    if force:
        print("💥 Modo: Force (releases existentes serão sobrescritos)")
    
    print()
    
    # Verificar se o GitHub CLI está autenticado
    print("🔍 Verificando GitHub CLI...")
    auth_result = run_gh_command(["auth", "status"])
    if not auth_result:
        print("❌ GitHub CLI não está autenticado. Execute 'gh auth login' primeiro.")
        sys.exit(1)
    
    print("✅ GitHub CLI autenticado!")
    
    # Obter releases existentes
    print("📋 Verificando releases existentes...")
    existing_releases = list_existing_releases()
    print(f"📊 Releases existentes: {len(existing_releases)}")
    
    # Obter dados do changelog
    print("📖 Carregando dados do changelog...")
    versions = get_changelog_data()
    print(f"📊 Versões no changelog: {len(versions)}")
    
    # Filtrar versões que precisam ser criadas
    versions_to_create = []
    versions_to_skip = []
    
    for version in versions:
        tag_name = f"v{version.version}"
        if tag_name in existing_releases:
            if force:
                versions_to_create.append(version)
                print(f"⚠️  Release {tag_name} será sobrescrito (modo force)")
            else:
                versions_to_skip.append(version)
                print(f"⏭️  Release {tag_name} já existe, pulando...")
        else:
            versions_to_create.append(version)
            print(f"✅ Release {tag_name} será criado")
    
    print(f"\n📊 Resumo:")
    print(f"  - Releases a criar: {len(versions_to_create)}")
    print(f"  - Releases a pular: {len(versions_to_create)}")
    
    if not versions_to_create:
        print("\n🎉 Todos os releases já existem!")
        if not force:
            print("💡 Use --force para sobrescrever releases existentes")
        return
    
    # Confirmar criação
    print(f"\n🤔 Deseja criar {len(versions_to_create)} releases?")
    if draft:
        print("📝 Os releases serão criados como drafts")
    if prerelease:
        print("🔬 Os releases serão marcados como prereleases")
    
    confirm = input("Digite 'sim' para confirmar: ").strip().lower()
    if confirm not in ['sim', 's', 'yes', 'y']:
        print("❌ Operação cancelada.")
        return
    
    # Criar releases
    print(f"\n🚀 Iniciando criação de {len(versions_to_create)} releases...")
    print("=" * 60)
    
    successful = 0
    failed = 0
    
    for i, version in enumerate(versions_to_create, 1):
        print(f"\n📦 [{i}/{len(versions_to_create)}] Processando v{version.version}...")
        
        if create_release(version, draft, prerelease):
            successful += 1
        else:
            failed += 1
        
        # Pequena pausa entre releases para evitar rate limiting
        if i < len(versions_to_create):
            print("⏳ Aguardando 2 segundos...")
            time.sleep(2)
    
    # Resumo final
    print("\n" + "=" * 60)
    print("📊 Resumo da Operação:")
    print(f"  ✅ Releases criados com sucesso: {successful}")
    print(f"  ❌ Releases que falharam: {failed}")
    print(f"  ⏭️  Releases pulados: {len(versions_to_skip)}")
    
    if successful > 0:
        print(f"\n🎉 {successful} releases criados com sucesso!")
        print("🔗 Acesse: https://github.com/[seu-usuario]/[seu-repo]/releases")
    
    if failed > 0:
        print(f"\n⚠️  {failed} releases falharam. Verifique os erros acima.")
    
    print("\n💡 Dicas:")
    print("  - Use 'gh release list' para ver todos os releases")
    print("  - Use 'gh release view v2.4.0' para ver um release específico")
    print("  - Use 'gh release delete v2.4.0' para deletar um release")

if __name__ == "__main__":
    main() 