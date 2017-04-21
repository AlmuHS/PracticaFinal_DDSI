create table VOLUNTARIO(
	codigo char(2),
	tipo numeric(1) not null,
	CONSTRAINT claveprimaria PRIMARY KEY (codigo)
);

create table PERSONA(
	dni char(9),
	codPersona char(2),	
	nombre varchar(50) not null,
	telefono numeric(9),
	correo varchar(20),
	edad numeric(3),
	localidad varchar(20),
	CONSTRAINT cpper PRIMARY KEY (dni),
	CONSTRAINT cajpersona FOREIGN KEY (codPersona) references VOLUNTARIO(codigo)
	CONSTRAINT codPerUnico UNIQUE(codPersona)
);

create table INSTITUCION(
	cif char(9),
	codIns char(2),
	nombre varchar(50) not null,
	razon_social varchar(20),
	telefono numeric(9),
	CONSTRAINT cpinst PRIMARY KEY (cif),
	CONSTRAINT caj FOREIGN KEY (codIns) REFERENCES VOLUNTARIO (codigo)
	CONSTRAINT codInsUnico UNIQUE(codIns)
);


create table ESTABLECIMIENTO(
	codigo char(5),
	nombre varchar(20) not null,
	direccion varchar(20),
	localidad varchar(15),
	CONSTRAINT cpest PRIMARY KEY (codigo)
);

create table ALIMENTO(
	codigo char(5),
	descripcion varchar(50),
	fechaCaducidad date,
	establecimiento char(5),
	fechaRecogida date not null,
	codVoluntario char(2),
	entregado numeric(1),
	CONSTRAINT cpal PRIMARY KEY(codigo),
	CONSTRAINT cest FOREIGN KEY (establecimiento) REFERENCES ESTABLECIMIENTO(codigo),
	CONSTRAINT cvol FOREIGN KEY (codVoluntario) REFERENCES VOLUNTARIO(codigo)
);
