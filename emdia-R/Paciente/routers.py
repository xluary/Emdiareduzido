from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from shared.dependencies import get_db
from Paciente.models import Paciente
from Paciente.schemas import PacienteCreate, PacienteOut  # Import appropriate schemas

router = APIRouter()

@router.post("/create/", response_model=PacienteOut)
def create_paciente(paciente_create: PacienteCreate, db: Session = Depends(get_db)):
    db_paciente = Paciente(**paciente_create.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

@router.get("/read/{numeroSUS}", response_model=PacienteOut)
def read_paciente(numeroSUS: int, db: Session = Depends(get_db)):
    paciente = db.query(Paciente).filter(Paciente.numeroSUS == numeroSUS).first()
    if paciente is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return paciente

@router.put("/update/{numeroSUS}", response_model=PacienteOut)
def update_paciente(numeroSUS: int, paciente_update: PacienteCreate, db: Session = Depends(get_db)):
    db_paciente = db.query(Paciente).filter(Paciente.numeroSUS == numeroSUS).first()
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    for field, value in paciente_update.dict(exclude_unset=True).items():
        setattr(db_paciente, field, value)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

@router.delete("/delete/{numeroSUS}", response_model=PacienteOut)
def delete_paciente(numeroSUS: int, db: Session = Depends(get_db)):
    db_paciente = db.query(Paciente).filter(Paciente.numeroSUS == numeroSUS).first()
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    db.delete(db_paciente)
    db.commit()
    return db_paciente
