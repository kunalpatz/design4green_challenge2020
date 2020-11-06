import sqlite3

database = r"db/score_data.db"


def get_commune():
    _conn = sqlite3.connect(database)
    _c = _conn.cursor()
    _c.execute('SELECT libcom FROM score_comm;')
    result = [x[0] for x in _c.fetchall()]
    result = [i for i in result if i]
    _conn.close()
    return result


def get_show_data(commune):
    _conn = sqlite3.connect(database)
    _c = _conn.cursor()
    _c.execute('SELECT * FROM main.score_comm c'
               ' inner join main.score_dep d on c.code_departement=d.code_departement '
               'inner join main.score_reg r on r.code_region=c.code_region'
               ' WHERE c.libcom like ?', (commune,))
    result = _c.fetchall()
    _conn.close()
    return result


def get_show_data_cp(code_postal):
    _conn = sqlite3.connect(database)
    _c = _conn.cursor()
    _c.execute('SELECT * FROM main.score_comm c'
               ' inner join main.score_dep d on c.code_departement=d.code_departement '
               'inner join main.score_reg r on r.code_region=c.code_region'
               ' WHERE c.code_postal = ?', (code_postal,))
    result = _c.fetchall()
    _conn.close()
    return result
