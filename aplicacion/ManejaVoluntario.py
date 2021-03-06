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

import Conexion
import clases
import pprint
from sqlalchemy import *
from sqlalchemy.exc import *


class ManejaVoluntario:
	
	def anadeVoluntarioPersona(self, miconexion, NuevaPersona):
		miconexion.conectar('user', 'user')
		sesion = miconexion.get_session()

		NuevoVoluntario = clases.Voluntario()

		NuevoVoluntario.codigo = NuevaPersona.codpersona
		NuevoVoluntario.tipo = 1
		
		sesion.add(NuevoVoluntario)
		sesion.add(NuevaPersona)

		try:
			sesion.commit()
		except SQLAlchemyError:
			sesion.rollback()
			print("Error al introducir voluntario")

		miconexion.desconectar()

	def anadeVoluntarioInstitucion(self, miconexion, NuevaInstitucion):
		miconexion.conectar('user', 'user')
		sesion = miconexion.get_session()		

		NuevoVoluntario = clases.Voluntario(codigo = NuevaInstitucion.codins, tipo = 0)	

		
		sesion.add(NuevaInstitucion)		
		sesion.add(NuevoVoluntario)
		
		try:		
			sesion.commit()
		except SQLAlchemyError:
			sesion.rollback()
			print("Error al introducir institucion")		

		miconexion.desconectar()
		
	def eliminaVoluntarioInstitucion(self, miconexion, inst):	
		miconexion.conectar('user', 'user')
		sesion = miconexion.get_session()

		sesion.query(clases.Institucion).filter(clases.Institucion.cif == inst.cif).\
    			delete(synchronize_session='evaluate')
				
		sesion.query(clases.Voluntario).filter(clases.Voluntario.codigo == inst.codins).\
    			delete(synchronize_session='evaluate')

		try:
			sesion.commit()
		except SQLAlchemyError:
			sesion.rollback()
			print("Error al eliminar institucion")
		
		miconexion.desconectar()


	def eliminaVoluntarioPersona(self, miconexion, per):	
		miconexion.conectar('user', 'user')
		sesion = miconexion.get_session()		

		sesion.query(clases.Persona).filter(clases.Persona.cif == per.dni).\
    			delete()
				
		sesion.query(clases.Voluntario).filter(clases.Voluntario.codigo == per.codpersona).\
    			delete()

		miconexion.desconectar()


	def actualiza_cifInstitucion(self, miconexion, cif, nuevocif):
		miconexion.conectar('user', 'user')
		sesion = miconexion.get_session()
		conexion = miconexion.get_conexion()
		
		updatecif = update(clases.Institucion).where(clases.Institucion.cif == cif).\
        		values(cif = nuevocif)

		conexion.execute(updatecif)
		
		sesion.commit()
		miconexion.desconectar()

	
	def Mostrar_RecogidosVoluntario(self, miconexion, vol):
		miconexion.conectar('user', 'user')
		sesion = miconexion.get_session()
		
		numero = sesion.query(clases.Alimento.codigo).filter(clases.Alimento.codvoluntario == vol).count()

		print("El voluntario con codigo " + vol + " ha recogido " + str(numero) + " alimentos")

		if numero > 5:
			lista = sesion.query(clases.Alimento).filter(clases.Alimento.codvoluntario == vol)

			for row in lista:
				pprint.pprint(row.__dict__)

		sesion.commit()
		miconexion.desconectar()




