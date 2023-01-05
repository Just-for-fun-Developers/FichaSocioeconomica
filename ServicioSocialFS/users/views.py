# users/views.py
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from ServicioSocialFS import db
from ServicioSocialFS.models import User, Ingresantes, DatosPersonales
from ServicioSocialFS.users.forms import RegistrationForm, LoginForm_ingresante, LoginForm_administrativo, LoginForm_regular, UpdateUserForm
from ServicioSocialFS.users.picture_handler import add_profile_pic

users = Blueprint('users', __name__)
# register

#### LOGIN ESTUDIANTE ######

@users.route('/login_ingresante', methods=['GET', 'POST'])
def login_ingresante():
    form = LoginForm_ingresante()
    if form.validate_on_submit():
        ingresante = Ingresantes.query.filter_by(dni=form.dni.data).first()
        user = DatosPersonales.query.filter_by(dni=form.dni.data).first()
        
        if user is None and ingresante is not None:
            print('ok1')
            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('services.form_ingresante')
                print("ok2")
            return redirect(next)
    return render_template('login_ingresante.html', form=form)


#### LOGIN REGULAR ######

@users.route('/login_regular', methods=['GET', 'POST'])
def login_regular():
    form = LoginForm_regular()
    if form.validate_on_submit():
        user = User.query.filter_by(codigo=form.codigo.data).first()
        
        if user.check_password(form.password.data) and user is not None:
            print('ok1')
            login_user(user)
            flash('Log in Success!')

            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('services.datos_personales')
                print("ok2")
            return redirect(next)
    return render_template('login_regular.html', form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("core.index"))

#### LOGIN ADMINISTRATIVO ######

@users.route('/login_administrativo', methods=['GET', 'POST'])
def login_administrativo():
    form = LoginForm_regular()
    if form.validate_on_submit():
        user = User.query.filter_by(codigo=form.codigo.data).first()
        
        if user.check_password(form.password.data) and user is not None:
            print('ok1')
            login_user(user)
            flash('Log in Success!')

            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('services.admin_page')
                print("ok2")
            return redirect(next)
    else:
        print('dont work')
    return render_template('login_administrativo.html', form=form)

########################################################


# @users.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()

#     if form.validate_on_submit():
#         user = User(email=form.email.data,
#                     username=form.username.data,
#                     password=form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Thanks for registration!')
#         return redirect(url_for('users.login'))
#     return render_template('register.html', form=form)
# # login


# @users.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         print(user)
#         print(form.password.data)
#         print(user.check_password(form.password.data))
#         if user.check_password(form.password.data) and user is not None:
#             print('ok1')
#             login_user(user)
#             flash('Log in Success!')

#             next = request.args.get('next')
#             if next == None or not next[0] == '/':
#                 next = url_for('core.index')
#                 print("ok2")
#             return redirect(next)
#     return render_template('login.html', form=form)


# # logout


# @users.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for("core.index"))

# # account (update UserForm)


# @users.route('/account', methods=['GET', 'POST'])
# @login_required
# def account():
#     form = UpdateUserForm()
#     if form.validate_on_submit():
#         if form.picture.data:
#             username = current_user.username
#             pic = add_profile_pic(form.picture.data, username)
#             current_user.profile_image = pic

#         current_user.username = form.username.data
#         current_user.email = form.email.data
#         db.session.commit()
#         flash('User Account Updated')
#         return redirect(url_for('users.account'))
#     elif request.method == 'GET':
#         form.username.data = current_user.username
#         form.email.data = current_user.email

#     profile_image = url_for(
#         'static', filename='profile_pics/'+current_user.profile_image)
#     return render_template('account.html', profile_image=profile_image, form=form)

# # user's list of News Post


# @users.route("/<username>")
# def user_posts(username):
#     page = request.args.get('page', 1, type=int)
#     user = User.query.filter_by(username=username).first_or_404()
#     news_posts = NewsPost.query.filter_by(author=user).order_by(
#         NewsPost.date.desc()).paginate(page=page, per_page=5)

#     return render_template('user_news_posts.html', news_posts=news_posts, user=user)
