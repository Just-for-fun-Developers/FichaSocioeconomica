# services/views.py
from flask_login import current_user, login_required
from flask import render_template,url_for,flash, redirect,request,Blueprint
from ServicioSocialFS.services.forms import FichaForm
from ServicioSocialFS.models import DatosPersonales, Procedencia, Residencia, DatosAcademicos, DatosPadre, DatosMadre, SituacionFamiliar,User
from ServicioSocialFS import db

services = Blueprint('services',__name__)

@services.route("/formulario_ingresante", methods=['GET', 'POST'])
#@login_required
def form_ingresante():
    form = FichaForm()
    if (request.method == 'POST') or (form.validate_on_submit()):
        dper = DatosPersonales(
            codigo_matricula = form.dper_codigo_matricula.data,
            carrera = form.dper_carrera.data,
            facultad = form.dper_facultad.data,
            apellido_pa = form.dper_apellido_pa.data,
            apellido_ma = form.dper_apellido_ma.data,
            nombre = form.dper_nombre.data,
            dni = form.dper_dni.data,
            discapacitado = form.dper_discapacitado.data,
            estado_civil = form.dper_estado_civil.data,
            email = form.dper_email.data,
            celular = form.dper_celular.data
        )
        db.session.add(dper)
        db.session.commit()

        dpro = Procedencia(
            pais = form.dpro_pais.data,
            departamento = form.dpro_departamento.data,
            provincia = form.dpro_provincia.data,
            distrito = form.dpro_distrito.data,
            tipo_vivienda = form.dpro_tipo_vivienda.data,
            material_vivienda = form.dpro_material_vivienda.data,
            num_habitaciones = form.dpro_num_habitaciones.data,
            zona_rural = form.dpro_zona_rural.data,
            barrio = form.dpro_barrio.data,
            direccion = form.dpro_direccion.data,
            luz_electrica = form.dpro_luz_electrica.data,
            agua_potable = form.dpro_agua_potable.data,
            desague = form.dpro_desague.data,
            telefono_fijo = form.dpro_telefono_fijo.data,
            internet = form.dpro_internet.data,
            television_cable = form.dpro_television_cable.data,
            radio = form.dpro_radio.data
        )
        db.session.add(dpro)
        db.session.commit()
        
        dres = Residencia(
            pais = form.dres_pais.data,
            departamento = form.dres_departamento.data,
            provincia = form.dres_provincia.data,
            distrito = form.dres_distrito.data,
            tipo_vivienda = form.dres_tipo_vivienda.data,
            material_vivienda = form.dres_material_vivienda.data,
            num_habitaciones = form.dres_num_habitaciones.data,
            zona_rural = form.dres_zona_rural.data,
            barrio = form.dres_barrio.data,
            direccion = form.dres_direccion.data,
            referencia = form.dres_referencia.data,
            luz_electrica = form.dres_luz_electrica.data,
            agua_potable = form.dres_agua_potable.data,
            desague = form.dres_desague.data,
            telefono_fijo = form.dres_telefono_fijo.data,
            internet = form.dres_internet.data,
            television_cable = form.dres_television_cable.data,
            radio = form.dres_radio.data
        )
        db.session.add(dres)
        db.session.commit()

        daca = DatosAcademicos(
            colegio = form.daca_colegio.data,
            ano_culminacion_estudio = form.daca_ano_culminacion_estudio.data,
            num_postulacion =  form.daca_num_postulacion.data,
            otra_carrera = form.daca_otra_carrera.data,
            tipo_preparacion = form.daca_tipo_preparacion.data,
            motivo_postulacion = form.daca_motivo_postulacion.data,
            escuela_motivo = form.daca_escuela_motivo.data
        )
        db.session.add(daca)
        db.session.commit()

        dpad = DatosPadre(
            apellido_pa = form.dpad_apellido_pa.data,
            apellido_ma = form.dpad_apellido_ma.data,
            nombre = form.dpad_nombre.data,
            esta_vivo = form.dpad_esta_vivo.data,
            estado_civil = form.dpad_estado_civil.data,
            nivel_educacion = form.dpad_nivel_educacion.data,
            fecha_nacimiento =  form.dpad_fecha_nacimiento.data,
            pais = form.dpad_pais.data,
            departamento = form.dpad_departamento.data,
            provincia = form.dpad_provincia.data,
            distrito = form.dpad_distrito.data,
            zona_rural = form.dpad_zona_rural.data,
            discapacidad_trabajo =  form.dpad_discapacidad_trabajo.data,
            primera_ocupacion = form.dpad_primera_ocupacion.data,
            segunda_ocupacion = form.dpad_segunda_ocupacion.data,
            ingresos = form.dpad_ingresos.data
        )
        db.session.add(dpad)
        db.session.commit()

        dmad = DatosMadre(
            apellido_pa = form.dmad_apellido_pa.data,
            apellido_ma = form.dmad_apellido_ma.data,
            nombre = form.dmad_nombre.data,
            esta_vivo = form.dmad_esta_vivo.data,
            estado_civil = form.dmad_estado_civil.data,
            nivel_educacion = form.dmad_nivel_educacion.data,
            fecha_nacimiento =  form.dmad_fecha_nacimiento.data,
            pais = form.dmad_pais.data,
            departamento = form.dmad_departamento.data,
            provincia = form.dmad_provincia.data,
            distrito = form.dmad_distrito.data,
            zona_rural = form.dmad_zona_rural.data,
            discapacidad_trabajo =  form.dmad_discapacidad_trabajo.data,
            primera_ocupacion = form.dmad_primera_ocupacion.data,
            segunda_ocupacion = form.dmad_segunda_ocupacion.data,
            ingresos = form.dmad_ingresos.data
        )
        db.session.add(dmad)
        db.session.commit()

        sfam = SituacionFamiliar(
            dependencia_padre = form.sfam_dependencia_padre.data,
            dependencia_madre = form.sfam_dependencia_madre.data,
            dependencia_hermanos = form.sfam_dependencia_hermanos.data,
            dependencia_conyuge = form.sfam_dependencia_conyuge.data,
            dependencia_pariente = form.sfam_dependencia_pariente.data,
            autosostenimiento = form.sfam_autosostenimiento.data,
            vive_con = form.sfam_vive_con.data,
            contacto_nombre = form.sfam_contacto_nombre.data,
            contacto_parentesco =  form.sfam_contacto_parentesco.data,
            contacto_direccion = form.sfam_contacto_direccion.data,
            contacto_lugar = form.sfam_contacto_lugar.data,
            contacto_celular = form.sfam_contacto_celular.data
        )
        db.session.add(sfam)
        db.session.commit()
        
        user = User(
            codigo = form.dper_codigo_matricula.data,
            password_hash = form.user_password.data,
            datos_personales_id = dper.id,
            procedencia_id = dpro.id,
            residencia_id = dres.id,
            situacion_familiar_id = sfam.id,
            datos_madre_id = dmad.id,
            datos_padre_id = dpad.id,
            datos_academicos_id = daca.id
        )
        db.session.add(user)
        db.session.commit()
        print('Done')
        return redirect(url_for('core.index'))
    else:
        print('pass qweqwe')
    return render_template('ficha_formulario.html', form=form)

@services.route("/datos_personales")
@login_required
def datos_personales():
    dper = DatosPersonales.query.filter_by(id=current_user.datos_personales_id).first()
    print(dper)
    return render_template('ficha_dper.html', dper=dper)

@services.route("/datos_procedencia")
@login_required
def datos_procedencia():
    dpro = Procedencia.query.filter_by(id=current_user.procedencia_id).first()
    
    return render_template('ficha_dpro.html', dpro=dpro)

@services.route("/datos_residencia")
@login_required
def datos_residencia():
    dres = Residencia.query.filter_by(id=current_user.residencia_id).first()
    
    return render_template('ficha_dres.html', dres=dres)

@services.route("/datos_academicos")
@login_required
def datos_academicos():
    daca = DatosAcademicos.query.filter_by(id=current_user.datos_academicos_id).first()
    
    return render_template('ficha_daca.html', daca=daca)

@services.route("/datos_padre")
@login_required
def datos_padre():
    dpad = DatosPadre.query.filter_by(id=current_user.datos_padre_id).first()
    
    return render_template('ficha_dpad.html', dpad=dpad)

@services.route("/datos_madre")
@login_required
def datos_madre():
    dmad = DatosMadre.query.filter_by(id=current_user.datos_madre_id).first()
    
    return render_template('ficha_dmad.html', dmad=dmad)

@services.route("/situacion_familiar")
@login_required
def situacion_familiar():
    sfam = SituacionFamiliar.query.filter_by(id=current_user.situacion_familiar_id).first()
    
    return render_template('ficha_sfam.html', sfam=sfam)

# @services.route("/news")
# def news():
#     page = request.args.get('page', 1, type=int)
#     news_posts = NewsPost.query.order_by(NewsPost.date.desc()).paginate(page=page, per_page=5)
#     return render_template('news.html', news_posts=news_posts)