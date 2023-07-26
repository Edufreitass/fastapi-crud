from fastapi import FastAPI, Depends, status
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
