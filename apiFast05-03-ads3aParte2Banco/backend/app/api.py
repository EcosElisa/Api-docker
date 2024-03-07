from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

tarefas = [
    {
        "id": "1",
        "item": "Escrever matéria revista."
    },
    {
        "id": "2",
        "item": "Revisar artigo jornal."
    }
]
#nome da app
app = FastAPI()
origins = [
    "http://localhost:3000",
    "localhost:3000",
]
app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_methods=["*"]
)
@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your tarefa list."}
@app.get("/tarefa", tags=["tarefas"])
async def get_tarefas() -> dict:
    return { "data": tarefas }
@app.post("/tarefa", tags=["tarefas"])
async def add_tarefa(tarefinha: dict) -> dict:
    tarefas.append(tarefinha)
    return {
        "data": { "Tarefa added." }
    }
@app.put("/tarefa/{id}", tags=["tarefas"])
async def update_tarefa(id: int, body: dict) -> dict:
    for tarefinha in tarefas:
        if int(tarefinha["id"]) == id:
            tarefinha["item"] = body["item"]
            return {
                "data": f"Tarefa com id {id} has been updated."
            }

    return {
        "data": f"Tarefa with id {id} not found."
    }
@app.delete("/tarefa/{id}", tags=["tarefas"])
async def delete_tarefa(id: int) -> dict:
    for tarefinha in tarefas:
        if int(tarefinha["id"]) == id:
            tarefas.remove(tarefinha)
            return {
                "data": f"Tarefa with id {id} has been removed."
            }

    return {
        "data": f"Tarefa com id {id} not found."
    }