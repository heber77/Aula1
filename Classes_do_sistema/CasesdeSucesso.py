from Classes_do_sistema.Upload_video import upload_video,get_static,Fieldname 
from flask import redirect, url_for, request
from . import db


@auth.route('/cases_sucesso', methods=['POST'])
def Upload_case():
    file = request.form.get('file')
    enviar = request.form.get('submit')
    fieldname = Fieldname.query.filter_by(file=file)

    if fieldname:
        return redirect(url_for('auth.cases_sucesso'))
    
    new_fieldname = Fieldname(file=file)
    link = upload_video(new_fieldname)
    db.enviar.saveFile(new_fieldname,get_static ('imagens'))
    return link
    
 
    

    
    
    
         
    
    
    


