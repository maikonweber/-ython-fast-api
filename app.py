# Importando as bibliotecas necessárias
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Criando uma instância do FastAPI
app = FastAPI()

# Criando uma classe modelo para representar uma tarefa
class Task(BaseModel):
    title: str
    description: str = None

# Criando uma lista para armazenar as tarefas
tasks = []

# Definindo uma rota para listar todas as tarefas
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

# Definindo uma rota para obter uma tarefa específica
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tasks[task_id]

# Definindo uma rota para criar uma nova tarefa
@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

# Definindo uma rota para atualizar uma tarefa existente
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tasks[task_id] = updated_task
    return updated_task

# Definindo uma rota para excluir uma tarefa
@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    deleted_task = tasks.pop(task_id)
    return deleted_task
