from fastapi import FastAPI
from routes.races import router as races_router
from routes.classes import router as classes_router
from routes.backgrounds import router as backgrounds_router
from routes.equipment import router as equipment_router
from routes.weapons import router as weapons_router
from routes.armor import router as armor_router
from routes.tools import router as tools_router
from routes.mounts import router as mounts_router
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/", tags=["Root"], summary="Root", description="Endpoint raiz da API. Retorna status e mensagem de boas-vindas.")
def root():
    return JSONResponse({
        "status": "ok",
        "mensagem": "API D&D 5e está funcionando e pronta para uso! Veja /docs para documentação."
    })

app.include_router(races_router)
app.include_router(classes_router)
app.include_router(backgrounds_router)
app.include_router(equipment_router)
app.include_router(weapons_router)
app.include_router(armor_router)
app.include_router(tools_router)
app.include_router(mounts_router) 