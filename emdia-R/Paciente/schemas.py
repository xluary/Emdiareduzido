from pydantic import BaseModel
from datetime import date

class PacienteCreate(BaseModel):
    data_nascimento:  date
    numeroSUS: int
    id_paciente: str  
    sexo : str
    info: str

    class Config:
        orm_mode = True

class PacienteOut(BaseModel):
    numeroSUS: int
    id_paciente: str  
    sexo : str
    info: str

    class Config:
        orm_mode = True
