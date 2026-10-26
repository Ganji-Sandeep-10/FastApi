from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import engine,Base,get_db
from app import models
from app import schemas

Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.post("/tasks",response_model=schemas.TaskResponse,status_code=201)
def create_task(task:schemas.TaskCreate,db:Session=Depends(get_db)):
    new_task=models.Task(**task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.get("/tasks",response_model=list[schemas.TaskResponse])
def get_tasks(db:Session=Depends(get_db)):
    return db.query(models.Task).all()

@app.get("/tasks/{task_id}",response_model=schemas.TaskResponse)
def get_task(task_id:int,db:Session=Depends(get_db)):
    task=db.get(models.Task,task_id)
    if task is None:
        raise HTTPException(status_code=404,detail=f"Task with {task_id} not found")
    return task

@app.patch("/tasks/{task_id}",response_model=schemas.TaskResponse)
def update_task(task_id:int,update:schemas.TaskUpdate,db:Session=Depends(get_db)):
    task=db.get(models.Task,task_id)
    if(task is None):
        raise HTTPException(status_code=404,detail=f"Task with {task_id} not found")

    for field,value in update.model_dump(exclude_unset=True).items():
        setattr(task,field,value)

    db.commit()
    db.refresh(task)
    return task

@app.delete("/tasks/{task_id}",status_code=204)
def delete_task(task_id:int,db:Session=Depends(get_db)):
    task=db.get(models.Task,task_id)

    if(task is None):
        raise HTTPException(status_code=404,detail=f"Task with {task_id} not found")

    db.delete(task)
    db.commit()
