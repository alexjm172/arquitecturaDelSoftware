from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI()

class Articulo(BaseModel):
    id: int
    titulo: str
    contenido: str

articulos: List[Articulo] = []

@app.post("/articulos/", response_model=Articulo)
def crear_articulo(articulo: Articulo):
    articulos.append(articulo)
    return articulo

@app.get("/articulos/", response_model=List[Articulo])
def leer_articulos():
    return articulos

@app.get("/articulos/{articulo_id}", response_model=Articulo)
def leer_articulo(articulo_id: int):
    for articulo in articulos:
        if articulo.id == articulo_id:
            return articulo
    raise HTTPException(status_code=404, detail="Artículo no encontrado")

@app.put("/articulos/{articulo_id}", response_model=Articulo)
def actualizar_articulo(articulo_id: int, articulo: Articulo):
    for idx, a in enumerate(articulos):
        if a.id == articulo_id:
            articulos[idx] = articulo
            return articulo
    raise HTTPException(status_code=404, detail="Artículo no encontrado")

@app.delete("/articulos/{articulo_id}", response_model=Articulo)
def borrar_articulo(articulo_id: int):
    for idx, a in enumerate(articulos):
        if a.id == articulo_id:
            return articulos.pop(idx)
    raise HTTPException(status_code=404, detail="Artículo no encontrado")


if __name__ == "__main__":
    
    uvicorn.run(app, host="127.0.0.1", port=8000)