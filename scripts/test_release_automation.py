#!/usr/bin/env python3
"""
Script de teste para verificar se a automação de releases está funcionando corretamente.
"""

import sys
import os
import subprocess
from datetime import datetime

# Importar os dados do changelog
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from routes.changelog import get_changelog_data

def test_gh_cli_installation():
    """Testa se o GitHub CLI está instalado."""
    print("🔍 Testando instalação do GitHub CLI...")
    
    try:
        result = subprocess.run(
            ["gh", "--version"],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"✅ GitHub CLI instalado: {result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ GitHub CLI não está instalado!")
        print("💡 Instale com: winget install GitHub.cli")
        return False

def test_gh_cli_auth():
    """Testa se o GitHub CLI está autenticado."""
    print("🔍 Testando autenticação do GitHub CLI...")
    
    try:
        result = subprocess.run(
            ["gh", "auth", "status"],
            capture_output=True,
            text=True,
            check=True
        )
        print("✅ GitHub CLI autenticado!")
        return True
    except subprocess.CalledProcessError:
        print("❌ GitHub CLI não está autenticado!")
        print("💡 Execute: gh auth login")
        return False

def test_changelog_data():
    """Testa se os dados do changelog estão acessíveis."""
    print("🔍 Testando dados do changelog...")
    
    try:
        versions = get_changelog_data()
        print(f"✅ {len(versions)} versões carregadas do changelog")
        
        # Mostrar as 3 versões mais recentes
        print("📋 Versões mais recentes:")
        for i, version in enumerate(versions[:3], 1):
            print(f"  {i}. v{version.version} - {version.codename}")
        
        return True
    except Exception as e:
        print(f"❌ Erro ao carregar dados do changelog: {e}")
        return False

def test_release_notes_generation():
    """Testa a geração de notas de release."""
    print("🔍 Testando geração de notas de release...")
    
    try:
        versions = get_changelog_data()
        if not versions:
            print("❌ Nenhuma versão encontrada no changelog")
            return False
        
        # Testar com a versão mais recente
        latest_version = versions[0]
        
        # Importar funções dos scripts de release
        from create_single_release import create_release_notes
        
        notes = create_release_notes(latest_version)
        
        if notes and len(notes) > 100:
            print(f"✅ Notas de release geradas com sucesso ({len(notes)} caracteres)")
            print("📝 Preview das notas:")
            print("-" * 50)
            print(notes[:500] + "..." if len(notes) > 500 else notes)
            print("-" * 50)
            return True
        else:
            print("❌ Notas de release vazias ou muito curtas")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao gerar notas de release: {e}")
        return False

def test_gh_repo_access():
    """Testa se tem acesso ao repositório."""
    print("🔍 Testando acesso ao repositório...")
    
    try:
        result = subprocess.run(
            ["gh", "repo", "view"],
            capture_output=True,
            text=True,
            check=True
        )
        print("✅ Acesso ao repositório confirmado!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao acessar repositório: {e}")
        print("💡 Verifique se está no diretório correto e tem permissões")
        return False

def test_existing_releases():
    """Testa a listagem de releases existentes."""
    print("🔍 Testando listagem de releases existentes...")
    
    try:
        result = subprocess.run(
            ["gh", "release", "list", "--limit", "5"],
            capture_output=True,
            text=True,
            check=True
        )
        
        releases = result.stdout.strip().split('\n')
        if releases and releases[0]:
            print(f"✅ {len(releases)} releases encontrados")
            print("📋 Releases existentes:")
            for release in releases[:3]:  # Mostrar apenas os 3 primeiros
                print(f"  - {release}")
        else:
            print("ℹ️  Nenhum release encontrado (normal para repositório novo)")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao listar releases: {e}")
        return False

def run_all_tests():
    """Executa todos os testes."""
    print("🚀 Iniciando testes de automação de releases...")
    print("=" * 60)
    
    tests = [
        ("GitHub CLI Installation", test_gh_cli_installation),
        ("GitHub CLI Authentication", test_gh_cli_auth),
        ("Changelog Data", test_changelog_data),
        ("Release Notes Generation", test_release_notes_generation),
        ("Repository Access", test_gh_repo_access),
        ("Existing Releases", test_existing_releases),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🧪 {test_name}")
        print("-" * 40)
        
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name}: PASSOU")
            else:
                print(f"❌ {test_name}: FALHOU")
        except Exception as e:
            print(f"❌ {test_name}: ERRO - {e}")
    
    print("\n" + "=" * 60)
    print(f"📊 Resultado dos testes: {passed}/{total} passaram")
    
    if passed == total:
        print("🎉 Todos os testes passaram! A automação está pronta para uso.")
        print("\n💡 Próximos passos:")
        print("   1. Execute: python create_releases.py")
        print("   2. Ou execute: python create_single_release.py 2.4.0")
    else:
        print("⚠️  Alguns testes falharam. Verifique os problemas acima.")
        print("\n💡 Soluções comuns:")
        print("   1. Instale o GitHub CLI: winget install GitHub.cli")
        print("   2. Autentique-se: gh auth login")
        print("   3. Verifique se está no diretório correto do repositório")
    
    return passed == total

def main():
    """Função principal."""
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("""
Script de teste para automação de releases - D&D API

Uso:
  python test_release_automation.py          # Executar todos os testes
  python test_release_automation.py --help   # Mostrar esta ajuda

Testes executados:
  ✅ GitHub CLI Installation
  ✅ GitHub CLI Authentication  
  ✅ Changelog Data
  ✅ Release Notes Generation
  ✅ Repository Access
  ✅ Existing Releases

Para mais informações, consulte RELEASE_AUTOMATION.md
        """)
        return
    
    success = run_all_tests()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main() 