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

