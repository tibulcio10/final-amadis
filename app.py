from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4 as ID
from typing import Optional

app = FastAPI()

pelis = []

class post(BaseModel):
    id: Optional[str]
    nombre: str
    fecha: datetime = datetime.now()
    comentario: str

@app.get('/')
def read_roof():
    return{"mensaje":"hola al api"}

@app.get('/listas')
def read_roof():
    return pelis

@app.post('/guardar')
def save_peli(post: post):
    post.id = str(ID())
    pelis.append(post.dict())
    return pelis[-1]

@app.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in pelis:
        if post["id"] == post_id:
            return post
        return "No encontrado"

@app.delete('/eliminar/{post_id}')
def delete_post(post_id: str):
    for index, post in enumerate(pelis):
        if post["id"] == post_id:
            pelis.pop(index)
            return{"mensaje":"eliminado correctamente"}

@app.put('/editar{post_id}')
def update_post(post_id: str, updatePost: post):
    for index, post in enumerate(pelis):
        if post["id"] == post_id:
            pelis[index]["nombre"] = updatePost.nombre
            pelis[index]["fecha"] = updatePost.fecha
            pelis[index]["comentario"] = updatePost.comentario
            return{"mensaje": "datos actualizados"}