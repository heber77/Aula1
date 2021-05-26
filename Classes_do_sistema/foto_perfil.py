from Classes_do_sistema.Upload_image import upload_image,get_static
from flask import redirect, url_for, request
from . import db

@main.route('/signup', methods=['POST'])
def foto_perfil():
    file = request.form.get('file')

    fieldname = Fieldname.query.filter_by(file=file)

    if fieldname:
        return redirect(url_for('main.signup'))
    
    new_fieldname = Fieldname(file=file)
    link = upload_image(new_fieldname)
    link.saveFile(new_fieldname,get_static (new_fieldname))
    

        



   

