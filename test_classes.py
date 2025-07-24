import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_filter_classes_with_magic():
    response = client.get("/classes?magic=true")
    assert response.status_code == 200
    data = response.json()
    assert all(any('magias' in nivel or 'magias' in nivel.get('habilidades', [{}])[0].get('nome', '').lower() for nivel in cls['niveis'] if 'magias' in nivel or any('magia' in h.get('nome', '').lower() for h in nivel.get('habilidades', []))) for cls in data)
    assert len(data) > 0

def test_filter_classes_without_magic():
    response = client.get("/classes?magic=false")
    assert response.status_code == 200
    data = response.json()
    assert all(not any('magias' in nivel or 'magias' in nivel.get('habilidades', [{}])[0].get('nome', '').lower() for nivel in cls['niveis'] if 'magias' in nivel or any('magia' in h.get('nome', '').lower() for h in nivel.get('habilidades', []))) for cls in data)
    assert len(data) > 0

def test_filter_classes_by_hit_die():
    response = client.get("/classes?hit_die=1d10")
    assert response.status_code == 200
    data = response.json()
    assert all("1d10" in cls["dado_vida"].lower() for cls in data)
    assert len(data) > 0

def test_filter_classes_by_armor():
    response = client.get("/classes?armor=leve")
    assert response.status_code == 200
    data = response.json()
    assert all(any("leve" in prof.lower() for prof in cls["proficiencias"] if "armadura" in prof.lower() or "armaduras" in prof.lower()) for cls in data)
    assert len(data) > 0

def test_filter_classes_combined():
    response = client.get("/classes?magic=true&hit_die=1d8&armor=leve")
    assert response.status_code == 200
    data = response.json()
    for cls in data:
        assert any('magias' in nivel or 'magias' in nivel.get('habilidades', [{}])[0].get('nome', '').lower() for nivel in cls['niveis'] if 'magias' in nivel or any('magia' in h.get('nome', '').lower() for h in nivel.get('habilidades', [])))
        assert "1d8" in cls["dado_vida"].lower()
        assert any("leve" in prof.lower() for prof in cls["proficiencias"] if "armadura" in prof.lower() or "armaduras" in prof.lower()) 