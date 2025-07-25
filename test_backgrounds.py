import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_backgrounds():
    resp = client.get('/backgrounds')
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    assert len(resp.json()) > 0

def test_get_background_by_id():
    resp = client.get('/backgrounds/0')
    assert resp.status_code == 200
    data = resp.json()
    assert 'nome' in data
    assert 'personalidade' in data

def test_get_background_traits():
    resp = client.get('/backgrounds/0/traits')
    assert resp.status_code == 200
    data = resp.json()
    assert 'tracos' in data
    assert 'ideais' in data
    assert 'vinculos' in data
    assert 'defeitos' in data

def test_get_background_404():
    resp = client.get('/backgrounds/9999')
    assert resp.status_code == 404
    resp = client.get('/backgrounds/9999/traits')
    assert resp.status_code == 404

def test_filter_by_name():
    resp = client.get('/backgrounds?name=acólito')
    assert resp.status_code == 200
    data = resp.json()
    assert any('acólito' in bg['nome'].lower() for bg in data)

def test_filter_by_prof():
    resp = client.get('/backgrounds?prof=religião')
    assert resp.status_code == 200
    data = resp.json()
    assert any(any('religião' in p.lower() for p in bg['proficiencias']) for bg in data)

def test_filter_by_ideal():
    resp = client.get('/backgrounds?ideal=tradição')
    assert resp.status_code == 200
    data = resp.json()
    assert any(any('tradição' in i.lower() for i in bg['personalidade']['ideais']) for bg in data) 