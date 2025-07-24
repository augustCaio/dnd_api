from fastapi import FastAPI
from routes.races import router as races_router
from routes.classes import router as classes_router
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return JSONResponse({
        "status": "ok",
        "mensagem": "API D&D 5e está funcionando e pronta para uso! Veja /docs para documentação."
    })

app.include_router(races_router)
app.include_router(classes_router) 