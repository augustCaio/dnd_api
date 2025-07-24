import pytest
from fastapi.testclient import TestClient
from main import app
import os
import json

client = TestClient(app)

def test_get_all_races():
    response = client.get("/races")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "nome" in data[0]
    assert "id" in data[0]

def test_get_race_by_id():
    response = client.get("/races/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "nome" in data

def test_get_race_not_found():
    response = client.get("/races/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Raça não encontrada"

def test_search_race_by_name():
    response = client.get("/races?name=anão")
    assert response.status_code == 200
    data = response.json()
    assert any("anão" in r["nome"].lower() for r in data)

def test_filter_race_by_size():
    response = client.get("/races?size=médio")
    assert response.status_code == 200
    data = response.json()
    assert all("médio" in r["tamanho"].lower() for r in data)

def test_combined_filter():
    response = client.get("/races?name=elfo&size=médio")
    assert response.status_code == 200
    data = response.json()
    assert all("elfo" in r["nome"].lower() and "médio" in r["tamanho"].lower() for r in data) 

def test_race_without_subraces():
    response = client.get("/races/4")  # Humano não tem sub-raças
    assert response.status_code == 200
    data = response.json()
    assert data["nome"].lower() == "humano"
    assert data.get("subracas") is None

def test_race_without_proficiencies():
    response = client.get("/races/5")  # Draconato não tem proficiências
    assert response.status_code == 200
    data = response.json()
    assert data["nome"].lower() == "draconato"
    assert data.get("proficiencias") is None

def test_race_optional_fields_absent():
    response = client.get("/races/4")  # Humano não tem visao_no_escuro
    assert response.status_code == 200
    data = response.json()
    assert data.get("visao_no_escuro") is None 

def test_search_case_insensitive():
    response = client.get("/races?name=ANÃO")
    assert response.status_code == 200
    data = response.json()
    assert any("anão" in r["nome"].lower() for r in data)

def test_search_with_accent():
    response = client.get("/races?name=anao")  # sem acento
    assert response.status_code == 200
    data = response.json()
    # Aceita tanto "anão" quanto "anao" (se houver)
    assert any("anão" in r["nome"].lower() or "anao" in r["nome"].lower() for r in data)

def test_filter_case_insensitive():
    response = client.get("/races?size=MÉDIO")
    assert response.status_code == 200
    data = response.json()
    assert all("médio" in r["tamanho"].lower() for r in data)

def test_combined_filter_case_accent():
    response = client.get("/races?name=ELFO&size=MEDIO")
    assert response.status_code == 200
    data = response.json()
    assert all("elfo" in r["nome"].lower() and "médio" in r["tamanho"].lower() for r in data) 

def test_empty_races_file(tmp_path, monkeypatch):
    # Copia races.json vazio para um diretório temporário e faz monkeypatch do caminho
    empty_file = tmp_path / "races.json"
    empty_file.write_text("[]", encoding="utf-8")
    monkeypatch.setattr("routes.races.DATA_PATH", str(empty_file))
    from routes import races as races_module
    client = TestClient(races_module.router)
    response = client.get("/races")
    assert response.status_code == 200
    assert response.json() == [] 