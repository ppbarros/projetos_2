from flask import Flask, request, render_template,redirect, url_for
from flaskext.mysql import MySQL
from db import *

app = Flask(__name__)
bd = MySQL()
bd.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'projetos'


@app.route('/')
def principal():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def validar_login():
    if request.method != 'POST':
        return redirect(url_for('principal'))

    else:
        user = request.form.get('user')
        password = request.form.get('password')
        conn = bd.connect()
        cursor = conn.cursor()
        usuario = validate(cursor, user, password)
        cursor.close()
        conn.close()
        if usuario is None:
            return render_template('login.html', erro='Usuário/Senha incorretos ou inexistentes')
        else:
            conn = bd.connect()
            cursor = conn.cursor()
            if usuario[2] == 1:
                pessoas = listar_pessoas(cursor, usuario[0])
                cursor.close()
                conn.close()
                return render_template('adm.html', lista=pessoas, nome=usuario[1])
            elif usuario[2] == 2:
                projetos = listar_projetos(cursor, usuario[0])
                cursor.close()
                conn.close()
                return render_template('gerente.html', lista=projetos, nome=usuario[1])
            elif usuario[2] == 3:
                return render_template('peao.html')
            else:
                return render_template('erro.html')

@app.route('/mudar_tipo/<idpessoa>/<tipo>')
def lista_tipo(idpessoa, tipo):
    conn = bd.connect()
    cursor = conn.cursor()
    ver_tipo(conn, cursor, idpessoa, tipo)
    cursor.close()
    conn.close()
    return redirect(url_for('validar_login'))








if __name__ == '__main__':
    app.run(debug=True)