import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# ROOT

def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"

# RACES

def test_get_races():
    resp = client.get("/racas")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_get_race_by_id():
    resp = client.get("/racas/1")
    assert resp.status_code == 200
    assert "nome" in resp.json()

def test_race_filter_name():
    resp = client.get("/racas?name=elfo")
    assert resp.status_code == 200
    for race in resp.json():
        assert "elfo" in race["nome"].lower()

# CLASSES

def test_get_classes():
    resp = client.get("/classes")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_get_class_by_id():
    resp = client.get("/classes/1")
    assert resp.status_code == 200
    assert "nome" in resp.json()

# BACKGROUNDS

def test_get_backgrounds():
    resp = client.get("/backgrounds")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_get_background_by_id():
    resp = client.get("/backgrounds/0")
    assert resp.status_code == 200
    assert "nome" in resp.json()

def test_get_background_traits():
    resp = client.get("/backgrounds/0/traits")
    assert resp.status_code == 200
    assert "tracos" in resp.json()

# EQUIPMENT

def test_get_equipment():
    resp = client.get("/equipment")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_get_equipment_by_id():
    resp = client.get("/equipment/0")
    assert resp.status_code == 200
    assert "nome" in resp.json()

# WEAPONS

def test_get_weapons():
    resp = client.get("/weapons")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_get_weapon_by_id():
    resp = client.get("/weapons/0")
    assert resp.status_code == 200
    assert "nome" in resp.json()

def test_weapons_filter_type():
    resp = client.get("/weapons?type=marcial")
    assert resp.status_code == 200
    for w in resp.json():
        assert "marcial" in w["categoria"].lower()

def test_weapons_filter_property():
    resp = client.get("/weapons?property=leve")
    assert resp.status_code == 200
    for w in resp.json():
        assert any("leve" in p.lower() for p in w["propriedades"])

# ARMOR

def test_get_armor():
    resp = client.get("/armor")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_get_armor_by_id():
    resp = client.get("/armor/0")
    assert resp.status_code == 200
    assert "nome" in resp.json()

# TOOLS

def test_get_tools():
    resp = client.get("/tools")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_get_tool_by_id():
    resp = client.get("/tools/0")
    assert resp.status_code == 200
    assert "nome" in resp.json()

# MOUNTS

def test_get_mounts():
    resp = client.get("/mounts")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_get_mount_by_id():
    resp = client.get("/mounts/0")
    assert resp.status_code == 200
    assert "nome" in resp.json()

# CURRENCY, SERVICES, LIFESTYLES

def test_get_currency():
    resp = client.get("/currency")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_get_services():
    resp = client.get("/services")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_get_lifestyles():
    resp = client.get("/lifestyles")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list) 