from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import *


Base = declarative_base()

class Voluntario(Base):
	__tablename__ = 'voluntario'
	codigo = Column(CHAR(2), primary_key = True)
	tipo = Column(SmallInteger)


class Persona(Base):
	__tablename__ = 'persona'
	dni = Column(CHAR(9), primary_key = True)
	codpersona = Column(CHAR(2), ForeignKey('voluntario.codigo'), unique=True)
	nombre = Column(String(50), nullable=False)
	telefono = Column(Integer)
	correo = Column(String(20))
	edad = Column(Integer)
	localidad = Column(String(20))


class Institucion(Base):
	__tablename__ = 'institucion'
	cif = Column(CHAR(9), primary_key = True)
	codins = Column(CHAR(2), ForeignKey('voluntario.codigo'), unique=True)
	nombre = Column(String(50), nullable = False)
	telefono = Column(Integer)
	razon_social = Column(String(20))

class Establecimiento(Base):
	__tablename__ = 'establecimiento'
	codigo = Column(CHAR(5), primary_key = True)
	nombre = Column(String(20), nullable=False)
	direccion = Column(String(20))
	localidad = Column(String(15))

class Alimento(Base):
	__tablename__ = 'alimento'
	codigo = Column(CHAR(5), primary_key = True)
	descripcion = Column(String(50))
	fechacaducidad = Column(Date)
	establecimiento = Column(CHAR(5), ForeignKey('establecimiento.codigo'))
	fecharecogida = Column(Date, nullable=False)
	codvoluntario = Column(CHAR(2), ForeignKey('voluntario.codigo'))
	entregado = Column(SmallInteger)



