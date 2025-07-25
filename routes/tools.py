from fastapi import APIRouter, HTTPException
from typing import List
import json
from models.tool import Tool

router = APIRouter()

with open('data/tools.json', encoding='utf-8') as f:
    tools_data = json.load(f)

def get_tool_by_id(idx: int):
    if 0 <= idx < len(tools_data):
        return tools_data[idx]
    return None

@router.get('/tools', response_model=List[Tool], tags=["Ferramentas"], summary="Listar todas as ferramentas", description="Retorna uma lista de todas as ferramentas e instrumentos disponíveis.")
def list_tools():
    """Lista todas as ferramentas e instrumentos do PHB."""
    return tools_data

@router.get('/tools/{id}', response_model=Tool, tags=["Ferramentas"], summary="Detalhes de uma ferramenta", description="Retorna os detalhes de uma ferramenta específica pelo índice.")
def get_tool(id: int):
    """Detalhes de uma ferramenta ou instrumento pelo índice."""
    item = get_tool_by_id(id)
    if not item:
        raise HTTPException(status_code=404, detail='Ferramenta não encontrada')
    return item 