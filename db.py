# INSERT INTO user (nombre, edad, genero) VALUES ('Rafael','10', 'masculino)
# UPDATE users (nombre, edad, gereno) VALUES ('Rafael', '10','masculino') WHERE name = 'rafel'
# SELECT * FROM users WHERE edad = 10 

from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()

class Alumno(Base):
    __tablename__ = 'alumnos'

    id = Column(Integer, primary_key=True)
    nombres = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    carnet = Column(Integer)
    notas = relationship('Nota', back_populates='alumno')

    @hybrid_property
    def nombre_completo(self):
        return f'{self.nombres} {self.apellidos}'

class Nota(Base):
    __tablename__ = 'notas'

    id = Column(Integer, primary_key=True)
    curso = Column(String)
    nota = Column(Integer)
    alumno_id = Column(Integer,ForeignKey('alumnos.id'))
    alumno = relationship('Alumno', back_populates='notas')

engine = create_engine('sqlite:///:memory:')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

lucia = Alumno (
    nombres = 'Lucia',
    apellidos = 'Gomez',
    carnet = 1234,
)
print(lucia.id)
#Insert
session.add(lucia)
session.commit()
session.refresh(lucia)
print(lucia.id)

#Query
lucia_from_db = session.query(Alumno).where(Alumno.nombres== 'Lucia').first()
print(lucia_from_db)
print(lucia_from_db.apellidos)
#Update
lucia_from_db.carnet = 5678
session.add(lucia_from_db)
session.commit()

#Delete
#print(lucia_from_db.carnet)
#session.commit()

luis = Alumno (
    nombres = 'Luis',
    apellidos = 'Perez',
    carnet = 9999,
)
session.add(luis)
session.commit()

alumnos = session.query(Alumno).all()
print(alumnos)
print(alumnos[0].nombres)
print(alumnos[1].nombres)

print(luis.nombre_completo)

nota = Nota(
    curso = 'matematicas',
    nota = 89,
    alumno_id=luis.id
)
session.add(nota)
session.commit()

session.refresh(nota)
print(nota.alumno.nombres)
session.refresh(luis)
print(luis.notas[0].nota)
print(luis.notas[0].curso)
print(nota.alumno.notas[0].alumno.nombre_completo)