from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from ServicioSocialFS.models import User

class FichaForm(FlaskForm):
    
    dper_codigo_matricula = StringField('Código de Matricula', validators=[DataRequired()])
    dper_carrera = StringField('Carrera', validators=[DataRequired()])
    dper_facultad = StringField('Facultad', validators=[DataRequired()])
    dper_apellido_pa = StringField('Apellido Paterno', validators=[DataRequired()])
    dper_apellido_ma = StringField('Apellido Materno', validators=[DataRequired()])
    dper_nombre = StringField('Nombre', validators=[DataRequired()])
    dper_dni = StringField('DNI', validators=[DataRequired()])
    dper_discapacitado = BooleanField('¿Tiene discapacidad?')
    dper_estado_civil = StringField('Estado Civil', validators=[DataRequired()])
    dper_email = StringField('Correo Electronico', validators=[DataRequired()])
    dper_celular = StringField('Número de Celular', validators=[DataRequired()])

    dpro_pais = StringField('País', validators=[DataRequired()])
    dpro_departamento = StringField('Departamento', validators=[DataRequired()])
    dpro_provincia = StringField('Provincia', validators=[DataRequired()])
    dpro_distrito = StringField('Distrito', validators=[DataRequired()])
    dpro_tipo_vivienda = StringField('Tipo de Vivienda', validators=[DataRequired()])
    dpro_material_vivienda = StringField('Material de Vivienda', validators=[DataRequired()])
    dpro_num_habitaciones = IntegerField('Número de Habitaciones', validators=[DataRequired()])
    dpro_zona_rural = BooleanField('¿Vive en Zona Rural?')
    dpro_barrio = StringField('Barrio', validators=[DataRequired()])
    dpro_direccion = StringField('Dirección', validators=[DataRequired()])
    dpro_luz_electrica = BooleanField('Luz Eléctrica')
    dpro_agua_potable = BooleanField('Agua Potable')
    dpro_desague = BooleanField('Desague')
    dpro_telefono_fijo = BooleanField('Teléfono Fijo')
    dpro_internet = BooleanField('Internet')
    dpro_television_cable = BooleanField('Televisión por Cable')
    dpro_radio = BooleanField('Radio')
   
    dres_pais = StringField('País', validators=[DataRequired()])
    dres_departamento = StringField('Departamento', validators=[DataRequired()])
    dres_provincia = StringField('Provincia', validators=[DataRequired()])
    dres_distrito = StringField('Distrito', validators=[DataRequired()])
    dres_tipo_vivienda = StringField('Tipo de Vivienda', validators=[DataRequired()])
    dres_material_vivienda = StringField('Material de Vivienda', validators=[DataRequired()])
    dres_num_habitaciones = IntegerField('Número de Habitaciones', validators=[DataRequired()])
    dres_zona_rural = BooleanField('¿Vive en Zona Rural?')
    dres_barrio = StringField('Barrio', validators=[DataRequired()])
    dres_direccion = StringField('Dirección', validators=[DataRequired()])
    dres_referencia = StringField('Referencia', validators=[DataRequired()])
    dres_luz_electrica = BooleanField('Luz Eléctrica')
    dres_agua_potable = BooleanField('Agua Potable')
    dres_desague = BooleanField('Desague')
    dres_telefono_fijo = BooleanField('Teléfono Fijo')
    dres_internet = BooleanField('Internet')
    dres_television_cable = BooleanField('Televisión por Cable')
    dres_radio = BooleanField('Radio')
   
    daca_colegio = StringField('Colegio', validators=[DataRequired()])
    daca_ano_culminacion_estudio = StringField('Año que Culmino sus Estudios', validators=[DataRequired()])
    daca_num_postulacion = IntegerField('Número de Veces que Postuló', validators=[DataRequired()])
    daca_otra_carrera = StringField('Estudia Adicionalmente en la Escuela Profesional', validators=[DataRequired()])
    daca_tipo_preparacion = StringField('Tipo de Preparación', validators=[DataRequired()])
    daca_motivo_postulacion = StringField('Escogio la UNAP por:', validators=[DataRequired()])
    daca_escuela_motivo = StringField('Escuela Profesional a la que Ingreso por:', validators=[DataRequired()])
    
    dpad_apellido_pa = StringField('Apellido Paterno', validators=[DataRequired()])
    dpad_apellido_ma = StringField('Apellido Materno', validators=[DataRequired()])
    dpad_nombre = StringField('Nombre', validators=[DataRequired()])
    dpad_esta_vivo = BooleanField('¿Está vivo su Padre?')
    dpad_estado_civil = StringField('Estado Civil de su Padre', validators=[DataRequired()])
    dpad_nivel_educacion = StringField('Nivel de Instrucción de su Padre', validators=[DataRequired()])
    dpad_fecha_nacimiento = StringField('Fecha de Nacimiento de su Padre', validators=[DataRequired()])
    dpad_pais = StringField('País', validators=[DataRequired()])
    dpad_departamento = StringField('Departamento', validators=[DataRequired()])
    dpad_provincia = StringField('Provincia', validators=[DataRequired()])
    dpad_distrito = StringField('Distrito', validators=[DataRequired()])
    dpad_zona_rural = BooleanField('¿Vive en Zona Rural?')
    dpad_discapacidad_trabajo = BooleanField('¿Presenta Alguna Discapacidad para Trabajar?')
    dpad_primera_ocupacion = StringField('Ocupación', validators=[DataRequired()])
    dpad_segunda_ocupacion = StringField('Segunda Ocupación', validators=[DataRequired()])
    dpad_ingresos = StringField('Ingresos de su Padre (S/.)', validators=[DataRequired()])
    


    dmad_apellido_pa = StringField('Apellido Paterno', validators=[DataRequired()])
    dmad_apellido_ma = StringField('Apellido Materno', validators=[DataRequired()])
    dmad_nombre = StringField('Nombre', validators=[DataRequired()])
    dmad_esta_vivo = BooleanField('¿Está viva su Madre?')
    dmad_estado_civil = StringField('Estado Civil de su Madre', validators=[DataRequired()])
    dmad_nivel_educacion = StringField('Nivel de Instrucción de su Madre', validators=[DataRequired()])
    dmad_fecha_nacimiento = StringField('Fecha de Nacimiento de su Madre', validators=[DataRequired()])
    dmad_pais = StringField('País', validators=[DataRequired()])
    dmad_departamento = StringField('Departamento', validators=[DataRequired()])
    dmad_provincia = StringField('Provincia', validators=[DataRequired()])
    dmad_distrito = StringField('Distrito', validators=[DataRequired()])
    dmad_zona_rural = BooleanField('¿Vive en Zona Rural?')
    dmad_discapacidad_trabajo = BooleanField('¿Presenta Alguna Discapacidad para Trabajar?')
    dmad_primera_ocupacion = StringField('Ocupación', validators=[DataRequired()])
    dmad_segunda_ocupacion = StringField('Segunda Ocupación', validators=[DataRequired()])
    dmad_ingresos = StringField('Ingresos de su Madre (S/.)', validators=[DataRequired()])
    
    sfam_dependencia_padre = BooleanField('¿Depende de su Padre?')
    sfam_dependencia_madre = BooleanField('¿Depende de su Madre?')
    sfam_dependencia_hermanos = BooleanField('¿Depende de sus Hermanos?')
    sfam_dependencia_conyuge = BooleanField('¿Depende de su Conyuge?')
    sfam_dependencia_pariente = BooleanField('¿Depende de algún Pariente?')
    sfam_autosostenimiento = BooleanField('¿Autosostenimiento?')
    sfam_vive_con = StringField('Vive con', validators=[DataRequired()])
    sfam_contacto_nombre = StringField('Apellidos y Nombres', validators=[DataRequired()])
    sfam_contacto_parentesco = StringField('Parentesco', validators=[DataRequired()])
    sfam_contacto_direccion = StringField('Dirección', validators=[DataRequired()])
    sfam_contacto_lugar = StringField('Lugar', validators=[DataRequired()])
    sfam_contacto_celular = StringField('Celular', validators=[DataRequired()])

    user_password = PasswordField('Password', validators=[DataRequired(), EqualTo(
        'user_pass_confirm', message='Passwords must match!!')])
    user_pass_confirm = PasswordField(
        'Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Terminar')

    

    

    
   