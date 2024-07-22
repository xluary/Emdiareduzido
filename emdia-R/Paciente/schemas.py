from pydantic import BaseModel

class PacienteCreate(BaseModel):
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
