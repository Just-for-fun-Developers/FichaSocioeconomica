# models.py
from ServicioSocialFS import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Ingresantes(db.Model, UserMixin):

    __tablename__ = 'ingresantes'

    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(8),nullable=False, unique=True)
    modalidad = db.Column(db.String(45), nullable=False)
    codigo = db.Column(db.String(6), nullable=False)

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(
        db.String(64), nullable=False, default='default_profile.png')
    codigo = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    #relationships   
    datos_personales_id = db.Column(db.Integer, db.ForeignKey('datos_personales.id'), nullable=False)
    procedencia_id = db.Column(db.Integer, db.ForeignKey('procedencia.id'), nullable=False)
    residencia_id = db.Column(db.Integer, db.ForeignKey('residencia.id'), nullable=False)
    # calificacion_id = db.Column(db.Integer, db.ForeignKey('calificacion.id'), nullable=False)
    situacion_familiar_id = db.Column(db.Integer, db.ForeignKey('situacion_familiar.id'), nullable=False)
    datos_madre_id = db.Column(db.Integer, db.ForeignKey('datos_madre.id'), nullable=False)
    datos_padre_id = db.Column(db.Integer, db.ForeignKey('datos_padre.id'), nullable=False)
    # contacto_emergencia_id = db.Column(db.Integer, db.ForeignKey('contacto_emergencia.id'), nullable=False)
    datos_academicos_id = db.Column(db.Integer, db.ForeignKey('datos_academicos.id'), nullable=False)
    # carga_familiar_id = db.Column(db.Integer, db.ForeignKey('carga_familiar.id'), nullable=False)

    # posts = db.relationship('NewsPost', backref='author', lazy=True)

    def __init__(self, codigo, password_hash, datos_personales_id, procedencia_id, residencia_id, situacion_familiar_id, datos_madre_id, datos_padre_id, datos_academicos_id):
        self.codigo = codigo
        self.password_hash = generate_password_hash(password_hash)
        self.datos_personales_id =datos_personales_id
        self.procedencia_id = procedencia_id
        self.residencia_id = residencia_id
        self.situacion_familiar_id = situacion_familiar_id
        self.datos_madre_id = datos_madre_id
        self.datos_padre_id = datos_padre_id
        self.datos_academicos_id = datos_academicos_id

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Username {self.codigo}"

class DatosPersonales(db.Model, UserMixin):
    __tablename__ = 'datos_personales'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    codigo_matricula = db.Column(db.String(6), unique=True, index=True, nullable=False)
    carrera = db.Column(db.String(90), nullable=False)
    facultad = db.Column(db.String(90), nullable=False)
    apellido_pa = db.Column(db.String(20), nullable=False)
    apellido_ma = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(30), nullable=False)
    dni = db.Column(db.String(8), unique=True, index=True, nullable=False)
    discapacitado = db.Column(db.Boolean, nullable=False)
    estado_civil = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(45), unique=True, index=True, nullable=False)
    celular = db.Column(db.String(9), unique=True, index=True, nullable=False)
    user = db.relationship('User', backref='id_dper', lazy=True)

    def __init__(self, codigo_matricula, carrera, facultad, apellido_pa, apellido_ma, nombre, dni, discapacitado, estado_civil, email, celular):
        self.codigo_matricula = codigo_matricula 
        self.carrera = carrera
        self.facultad = facultad
        self.apellido_pa = apellido_pa
        self.apellido_ma = apellido_ma
        self.nombre = nombre
        self.dni = dni
        self.discapacitado = discapacitado
        self.estado_civil = estado_civil
        self.email = email
        self.celular = celular

class Procedencia(db.Model, UserMixin):
    __tablename__ = 'procedencia'
    id = db.Column(db.Integer, primary_key=True)
    pais = db.Column(db.String(20), index=True, nullable=False)
    departamento = db.Column(db.String(20), index=True, nullable=False)
    provincia = db.Column(db.String(20), index=True, nullable=False)
    distrito = db.Column(db.String(20), index=True, nullable=False)
    tipo_vivienda = db.Column(db.String(20), nullable=False)
    material_vivienda = db.Column(db.String(15), nullable=False)
    num_habitaciones = db.Column(db.Integer, nullable=False)
    zona_rural = db.Column(db.Boolean, nullable=False)
    barrio = db.Column(db.String(30), nullable=False)
    direccion = db.Column(db.String(30), nullable=False)
    luz_electrica = db.Column(db.Boolean, nullable=False)
    agua_potable = db.Column(db.Boolean, nullable=False)
    desague = db.Column(db.Boolean, nullable=False)
    telefono_fijo = db.Column(db.Boolean, nullable=False)
    internet = db.Column(db.Boolean, nullable=False)
    television_cable = db.Column(db.Boolean, nullable=False)
    radio = db.Column(db.Boolean, nullable=False)
    user = db.relationship('User', backref='id_p', lazy=True)

    def __init__(self, pais, departamento, provincia, distrito, tipo_vivienda, material_vivienda,  num_habitaciones, zona_rural,  barrio,  direccion,  luz_electrica, agua_potable, desague, telefono_fijo, internet, television_cable, radio):
        self.pais = pais
        self.departamento = departamento
        self.provincia = provincia
        self.distrito = distrito
        self.tipo_vivienda = tipo_vivienda
        self.material_vivienda = material_vivienda
        self.num_habitaciones = num_habitaciones
        self.zona_rural = zona_rural
        self.barrio = barrio
        self.direccion = direccion
        self.luz_electrica = luz_electrica
        self.agua_potable = agua_potable
        self.desague = desague
        self.telefono_fijo = telefono_fijo
        self.internet = internet
        self.television_cable = television_cable
        self.radio = radio

class Residencia(db.Model, UserMixin):
    __tablename__ = 'residencia'
    id = db.Column(db.Integer, primary_key=True)
    pais = db.Column(db.String(20), index=True, nullable=False)
    departamento = db.Column(db.String(20), index=True, nullable=False)
    provincia = db.Column(db.String(20), index=True, nullable=False)
    distrito = db.Column(db.String(20), index=True, nullable=False)
    tipo_vivienda = db.Column(db.String(20), nullable=False)
    material_vivienda = db.Column(db.String(15), nullable=False)
    num_habitaciones = db.Column(db.Integer, nullable=False)
    zona_rural = db.Column(db.Boolean, nullable=False)
    barrio = db.Column(db.String(30), nullable=False)
    direccion = db.Column(db.String(30), nullable=False)
    referencia = db.Column(db.String(45), nullable=False)
    luz_electrica = db.Column(db.Boolean, nullable=False)
    agua_potable = db.Column(db.Boolean, nullable=False)
    desague = db.Column(db.Boolean, nullable=False)
    telefono_fijo = db.Column(db.Boolean, nullable=False)
    internet = db.Column(db.Boolean, nullable=False)
    television_cable = db.Column(db.Boolean, nullable=False)
    radio = db.Column(db.Boolean, nullable=False)
    user = db.relationship('User', backref='id_r', lazy=True)

    def __init__(self, pais,  departamento,  provincia,  distrito,  tipo_vivienda,   material_vivienda,  num_habitaciones,  zona_rural,  barrio,  direccion,  referencia,  luz_electrica,  agua_potable,  desague,  telefono_fijo,   internet,  television_cable, radio):
        self.pais = pais
        self.departamento = departamento
        self.provincia = provincia
        self.distrito = distrito
        self.tipo_vivienda = tipo_vivienda
        self.material_vivienda = material_vivienda
        self.num_habitaciones = num_habitaciones
        self.zona_rural = zona_rural
        self.barrio = barrio
        self.direccion = direccion
        self.referencia = referencia
        self.luz_electrica = luz_electrica
        self.agua_potable = agua_potable
        self.desague = desague
        self.telefono_fijo = telefono_fijo
        self.internet = internet
        self.television_cable = television_cable
        self.radio = radio

        

class DatosAcademicos(db.Model, UserMixin):
    __tablename__ = 'datos_academicos'
    id = db.Column(db.Integer, primary_key=True)
    colegio = db.Column(db.String(45), nullable=False)
    ano_culminacion_estudio = db.Column(db.String(4), nullable=False)
    num_postulacion = db.Column(db.Integer, nullable=False)
    otra_carrera = db.Column(db.String(60), nullable=False)
    tipo_preparacion = db.Column(db.String(20), nullable=False)
    motivo_postulacion = db.Column(db.String(45), nullable=False)
    escuela_motivo = db.Column(db.String(45), nullable=False)
    user = db.relationship('User', backref='id_da', lazy=True)

    def __init__(self, colegio, ano_culminacion_estudio, num_postulacion, otra_carrera, tipo_preparacion, motivo_postulacion, escuela_motivo):
        self.colegio = colegio
        self.ano_culminacion_estudio = ano_culminacion_estudio
        self.num_postulacion = num_postulacion
        self.otra_carrera = otra_carrera
        self.tipo_preparacion = tipo_preparacion
        self.motivo_postulacion = motivo_postulacion
        self.escuela_motivo = escuela_motivo

        

class DatosPadre(db.Model, UserMixin):
    __tablename__ = 'datos_padre'
    id = db.Column(db.Integer, primary_key=True)
    apellido_pa = db.Column(db.String(20), nullable=False)
    apellido_ma = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(30), nullable=False)
    esta_vivo = db.Column(db.Boolean, nullable=False)
    estado_civil = db.Column(db.String(15), nullable=False)
    nivel_educacion = db.Column(db.String(30), nullable=False)
    fecha_nacimiento = db.Column(db.String(10), nullable=False)
    pais = db.Column(db.String(20), index=True, nullable=False)
    departamento = db.Column(db.String(20), index=True, nullable=False)
    provincia = db.Column(db.String(20), index=True, nullable=False)
    distrito = db.Column(db.String(20), index=True, nullable=False)
    zona_rural = db.Column(db.Boolean, nullable=False)
    discapacidad_trabajo = db.Column(db.Boolean, nullable=False)
    primera_ocupacion = db.Column(db.String(45), nullable=False)
    segunda_ocupacion = db.Column(db.String(45), nullable=False)
    ingresos = db.Column(db.String(10), nullable=False)
    user = db.relationship('User', backref='id_dpadre', lazy=True)

    def __init__(self, apellido_pa, apellido_ma, nombre, esta_vivo, estado_civil, nivel_educacion, fecha_nacimiento, pais, departamento ,provincia, distrito, zona_rural, discapacidad_trabajo, primera_ocupacion, segunda_ocupacion, ingresos):
        self.apellido_pa = apellido_pa
        self.apellido_ma = apellido_ma
        self.nombre = nombre
        self.esta_vivo = esta_vivo
        self.estado_civil = estado_civil
        self.nivel_educacion = nivel_educacion
        self.fecha_nacimiento = fecha_nacimiento
        self.pais = pais
        self.departamento = departamento
        self.provincia = provincia
        self.distrito = distrito
        self.zona_rural = zona_rural
        self.discapacidad_trabajo = discapacidad_trabajo
        self.primera_ocupacion = primera_ocupacion
        self.segunda_ocupacion = segunda_ocupacion
        self.ingresos = ingresos

        

class DatosMadre(db.Model, UserMixin):
    __tablename__ = 'datos_madre'
    id = db.Column(db.Integer, primary_key=True)
    apellido_pa = db.Column(db.String(20), nullable=False)
    apellido_ma = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(30), nullable=False)
    esta_vivo = db.Column(db.Boolean, nullable=False)
    estado_civil = db.Column(db.String(15), nullable=False)
    nivel_educacion = db.Column(db.String(30), nullable=False)
    fecha_nacimiento = db.Column(db.String(10), nullable=False)
    pais = db.Column(db.String(20), index=True, nullable=False)
    departamento = db.Column(db.String(20), index=True, nullable=False)
    provincia = db.Column(db.String(20), index=True, nullable=False)
    distrito = db.Column(db.String(20), index=True, nullable=False)
    zona_rural = db.Column(db.Boolean, nullable=False)
    discapacidad_trabajo = db.Column(db.Boolean, nullable=False)
    primera_ocupacion = db.Column(db.String(45), nullable=False)
    segunda_ocupacion = db.Column(db.String(45), nullable=False)
    ingresos = db.Column(db.String(10), nullable=False)
    user = db.relationship('User', backref='id_dmadre', lazy=True)

    def __init__(self, apellido_pa, apellido_ma, nombre, esta_vivo, estado_civil, nivel_educacion, fecha_nacimiento, pais, departamento ,provincia, distrito, zona_rural, discapacidad_trabajo, primera_ocupacion, segunda_ocupacion, ingresos):
        self.apellido_pa = apellido_pa
        self.apellido_ma = apellido_ma
        self.nombre = nombre
        self.esta_vivo = esta_vivo
        self.estado_civil = estado_civil
        self.nivel_educacion = nivel_educacion
        self.fecha_nacimiento = fecha_nacimiento
        self.pais = pais
        self.departamento = departamento
        self.provincia = provincia
        self.distrito = distrito
        self.zona_rural = zona_rural
        self.discapacidad_trabajo = discapacidad_trabajo
        self.primera_ocupacion = primera_ocupacion
        self.segunda_ocupacion = segunda_ocupacion
        self.ingresos = ingresos

class SituacionFamiliar(db.Model, UserMixin):
    __tablename__ = 'situacion_familiar'
    id = db.Column(db.Integer, primary_key=True) 
    dependencia_padre = db.Column(db.Boolean, nullable=False)
    dependencia_madre = db.Column(db.Boolean, nullable=False)
    dependencia_hermanos = db.Column(db.Boolean, nullable=False)
    dependencia_conyuge = db.Column(db.Boolean, nullable=False)
    dependencia_pariente = db.Column(db.Boolean, nullable=False)
    autosostenimiento = db.Column(db.Boolean, nullable=False)
    vive_con = db.Column(db.String(10), nullable=False)
    contacto_nombre = db.Column(db.String(80), nullable=False)
    contacto_parentesco = db.Column(db.String(15), nullable=False)
    contacto_direccion = db.Column(db.String(45), nullable=False)
    contacto_lugar = db.Column(db.String(45), nullable=False)
    contacto_celular = db.Column(db.String(9), nullable=False)
    user = db.relationship('User', backref='id_s', lazy=True)

    def __init__(self, dependencia_padre, dependencia_madre, dependencia_hermanos, dependencia_conyuge, dependencia_pariente,autosostenimiento, vive_con, contacto_nombre, contacto_parentesco, contacto_direccion, contacto_lugar, contacto_celular):
        self.dependencia_padre = dependencia_padre
        self.dependencia_madre = dependencia_madre
        self.dependencia_hermanos = dependencia_hermanos
        self.dependencia_conyuge = dependencia_conyuge
        self.dependencia_pariente = dependencia_pariente
        self.autosostenimiento = autosostenimiento
        self.vive_con = vive_con
        self.contacto_nombre = contacto_nombre
        self.contacto_parentesco = contacto_parentesco
        self.contacto_direccion = contacto_direccion
        self.contacto_lugar = contacto_lugar
        self.contacto_celular = contacto_celular

        
