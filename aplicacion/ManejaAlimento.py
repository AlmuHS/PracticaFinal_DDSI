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

import clases
import Conexion
import pprint
from sqlalchemy import *
from datetime import datetime, date, time, timedelta

class ManejaAlimento:
	
	def get_RecogidaAlimentos(self, miconexion, fechaMin, fechaMax, establecimiento):
		miconexion.conectar('user', 'user')
		sesion = miconexion.get_session()
		

		lista = sesion.query(clases.Alimento).filter(clases.Alimento.fecharecogida >= fechaMin,
								clases.Alimento.fecharecogida <= fechaMax, 
								clases.Alimento.establecimiento == establecimiento).all()

		for row in lista:
   			pprint.pprint(row.__dict__)

		miconexion.desconectar()

	def get_Caducados(self, miconexion):
		miconexion.conectar('user', 'user')
		sesion = miconexion.get_session()

		FechaActual = datetime.now()
	
		listaCaducados = sesion.query(clases.Alimento).filter(clases.Alimento.fechacaducidad < FechaActual).all()
		
		filas = 0

		for row in listaCaducados:
			sesion.delete(row)   			
			pprint.pprint(row.__dict__)
			filas=filas+1

		print(str(filas) + " alimentos eliminados")
			

		sesion.commit()
		miconexion.desconectar()

	def AnadeRecogida(self, miconexion, nuevoAlimento):
		miconexion.conectar('user', 'user')
		sesion = miconexion.get_session()		

		sesion.add(nuevoAlimento)
		sesion.commit()

		miconexion.desconectar()

