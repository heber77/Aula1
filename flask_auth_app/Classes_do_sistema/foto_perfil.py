from os import link
from Classes_do_sistema.Upload_image import upload_image,get_static,Fieldname
from flask import redirect, url_for, request
from . import db
import flask_auth_app as main
import flask_auth_app.project as auth

@main.route('/signup', methods=['POST'])
def Upload_imagem():
    file = request.form.get('file')

    fieldname = Fieldname.query.filter_by(file=file)

    if fieldname:
        return redirect(url_for('main.signup'))
    
    new_fieldname = Fieldname(file=file)
    link = upload_image(new_fieldname)
    link.saveFile(new_fieldname,get_static ('imagens'))
    
@auth.route('/templates/base_2', methods=['POST'])
def foto_perfil():
    return link
     

    

        



   

