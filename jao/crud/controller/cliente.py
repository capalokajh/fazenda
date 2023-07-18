#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(nome, tipo):
    db.cur.execute("""
                   INSERT into public.animais (nome, tipo)
                   VALUES ('%s','%s')
                   """ % (nome, tipo))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM animais
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

def excluir (id):
    db.cur.execute("""
            DELETE FROM animais WHERE id = '%s' """ % (id))
    db.con.commit()
