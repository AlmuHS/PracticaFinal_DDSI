import ManejaVoluntario
import ManejaAlimento
import Conexion
import clases
from sqlalchemy import *
from sqlalchemy.orm import *
from datetime import *


conn = Conexion.conexion()

def InsertarPersona():
	MVol = ManejaVoluntario.ManejaVoluntario()
	nuevaper = clases.Persona()
	
	nuevaper.dni = input("Introduce DNI: ")
	nuevaper.codpersona = input("Introduce codigo de voluntario: ")
	nuevaper.nombre = input("Introduce nombre: ")
	nuevaper.telefono = input("Introduce telefono: ")
	nuevaper.correo = input("Introduce correo: ")
	nuevaper.edad = input("Introduce edad: ")
	nuevaper.localidad = input("Introduce localidad: ")

	MVol.anadeVoluntarioPersona(conn, nuevaper)

def EliminarInstitucion():
	MVol = ManejaVoluntario.ManejaVoluntario()
	inst = clases.Institucion()

	inst.cif = input("Introduce cif: ")
	inst.codins = input("Introduce codigo: ")
	MVol.eliminaVoluntarioInstitucion(conn, inst)

	

def InsertarRecogida():
	MAl = ManejaAlimento.ManejaAlimento()
	NuevoAlimento = clases.Alimento()

	NuevoAlimento.codigo = input("Inserta codigo del alimento: ")
	NuevoAlimento.establecimiento = input("Codigo del establecimiento: ")
	NuevoAlimento.fecharecogida = datetime.strptime(input("Fecha de recogida: "), "%d/%m/%Y")
	NuevoAlimento.fechacaducidad = datetime.strptime(input("Fecha de caducidad: "), "%d/%m/%Y")
	NuevoAlimento.codvoluntario = input("Codigo del voluntario que recogio el alimento: ")
	NuevoAlimento.entregado = input("El alimento ha sido entregado? si=1, no=0: ")

	MAl.AnadeRecogida(conn, NuevoAlimento)

def VerAlimentosRecogida():
	MAl = ManejaAlimento.ManejaAlimento()
	fechaIni = datetime.strptime(input("Introduce fecha de inicio: "), "%d/%m/%Y")
	fechaFin = datetime.strptime(input("Introduce fecha de fin: "), "%d/%m/%Y")
	establecimiento = input("Introduce codigo del establecimiento: ")
	MAl.get_RecogidaAlimentos(conn, fechaIni, fechaFin, establecimiento)


def ActualizarCif():
	MVol = ManejaVoluntario.ManejaVoluntario()
	cif = input("Introduce cif actual: ")
	nuevocif = input("Introduce nuevo cif: ")

	MVol.actualiza_cifInstitucion(conn, cif, nuevocif)

def VerAlimentosCaducados():
	MAl = ManejaAlimento.ManejaAlimento()
	MAl.get_Caducados(conn)

def MostrarRecogidaVoluntario():
	MVol = ManejaVoluntario.ManejaVoluntario()
	codvol = input("Introduce codigo del voluntario: ")
	
	MVol.Mostrar_RecogidosVoluntario(conn, codvol)


def MenuPrincipal():
	opcion = 0	

	while opcion != 8:
		print("\nBienvenido a la aplicacion de la ONG 'Nadie sin Comer' ")
		print("-------------------------------------------------------")
		print("Seleccione operacion a realizar: ")
		print("1. Insertar nueva persona")
		print("2. Eliminar datos de institucion")
		print("3. Insertar datos de recogida")
		print("4. Ver alimentos de recogida por fecha")
		print("5. Actualizar cif de una institucion")
		print("6. Eliminar alimentos caducados")
		print("7. Obtener alimentos recogidos por un voluntario")
		print("8. Salir")

		opcion = int(input("Seleccione opcion: "))

		if opcion == 1:
			InsertarPersona()

		elif opcion == 2:
			EliminarInstitucion()

		elif opcion == 3:		 
			InsertarRecogida()
	
		elif opcion == 4:
			VerAlimentosRecogida()

		elif opcion == 5:
			ActualizarCif()

		elif opcion == 6:
			VerAlimentosCaducados()

		elif opcion == 7:
			MostrarRecogidaVoluntario()			

				

MenuPrincipal()


