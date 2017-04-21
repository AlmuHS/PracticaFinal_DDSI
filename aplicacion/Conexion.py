from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import *

class conexion:
	
	def conectar(self, usuario, clave):
		self.engine = create_engine('oracle+cx_oracle://' + usuario + ':' + clave + '@XXX.YYY.ZZZ.TTT/mydb', echo=False)
		self.connection = self.engine.connect()

	def desconectar(self):
		self.connection.close()	
	
	def get_session(self):
		session = sessionmaker()
		session.configure(bind=self.engine)

		return session()

	def get_conexion(self):
		return self.connection

