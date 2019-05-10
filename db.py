def validate(cursor, user, password):
    cursor.execute(f'select idpessoas, nome, tipo from pessoas where login = "{user}" and senha = "{password}"')
    usuario = cursor.fetchone()
    return usuario

def listar_pessoas(cursor, idpessoas):
    cursor.execute(f'select idpessoas, nome, tipo from pessoas where idpessoas <> {idpessoas} order by nome asc')
    lista = cursor.fetchall()
    return lista

def listar_projetos(cursor, idpessoas):
    cursor.execute(f'select idprojeto, nome, data_inicio, data_fim from projeto where gerente = {idpessoas}')
    lista = cursor.fetchall()
    return lista

def ver_tipo(conn, cursor, idpessoa, tipo):
    cursor.execute(f'update pessoas set tipo = {tipo} where idpessoas = {idpessoa}')
    conn.commit()
