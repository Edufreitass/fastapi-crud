from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session

from app.src import engine, Base, get_db
from app.src import schemas, repositories, models

Base.metadata.create_all(engine)

app = FastAPI()


@app.post("/api/cursos",
          response_model=schemas.CursoResponse,
          status_code=status.HTTP_201_CREATED)
def create(request: schemas.CursoRequest, db: Session = Depends(get_db)):
    curso = repositories.CursoRepository.save(
        db, models.Curso(**request.model_dump()))
    return schemas.CursoResponse.model_validate(curso)
