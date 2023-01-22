import sqlite3


def all(query: str):
   with sqlite3.connect('netflix.db') as con:
       con.row_factory = sqlite3.Row
       result = []

       for i in con.execute(query).fetchall():
           result.append(dict(i))

       return result

def one(querry: str):
    with sqlite3.connect('netflix.db') as con:
        con.row_factory = sqlite3.Row
        result = con.execute(querry).fetchone()

    if result is None:
        return None
    else:
        return dict(result)









