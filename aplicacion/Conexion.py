'''Copyright 2016 2017 Almudena García Jurado-Centurión
This file is part of PracticaFinal_DDSI
PracticaFinal_DDSI is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
Practica2_AMC is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with PracticaFinal_DDSI.  If not, see <http://www.gnu.org/licenses/>'''

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

