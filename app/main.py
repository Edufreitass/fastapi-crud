from fastapi import FastAPI, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

from app.src.database import Base, engine, get_db
from app.src.models import Curso
from app.src.repositories import CursoRepository
from app.src.schemas import CursoResponse, CursoRequest

Base.metadata.create_all(engine)

app = FastAPI()


@app.post("/api/cursos",
          response_model=CursoResponse,
          status_code=status.HTTP_201_CREATED)
def create(request: CursoRequest, db: Session = Depends(get_db)):
    curso = CursoRepository.save(
        db, Curso(**request.model_dump()))
    return CursoResponse.model_validate(curso)


@app.get("/api/cursos", response_model=list[CursoResponse])
def find_all(db: Session = Depends(get_db)):
    cursos = CursoRepository.find_all(db)
    return [CursoResponse.model_validate(curso) for curso in cursos]


@app.get("/api/cursos/{id}", response_model=CursoResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    curso = CursoRepository.find_by_id(db, id)
    if not curso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso não encontrado"
        )
    return CursoResponse.model_validate(curso)


@app.delete("/api/cursos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not CursoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso não encontrado"
        )
    CursoRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
