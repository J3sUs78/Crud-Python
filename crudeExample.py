import sqlite3


def insert(db,element):
    db.execute('insert into almacen (a1,i1) values(?,?)', (element['a1'], element['i1']))

    db.commit()

def show(db):
    cursor = db.execute('select * from almacen')
    print('Nombres || Edades')
    for row in cursor:
        print('\n\t','{} : {}'.format(row['a1'],row['i1']))


def read(db,key):
    print('||Reading Data||')
    cursor = db.execute('select * from almacen where a1 = ?', (key,))
    return cursor.fetchone()#se detiene linea a linea

def uptdate(db,key):
    print('||Updating Data||')
    old_age = read(db, key['a1'])
    print("Actualizando edad de {} ||antes: {} ahora: {}||".format(key['a1'], old_age['i1'], key['i1']))
    db.execute('update almacen set i1 = ? where a1 = ?', (key['i1'],key['a1']))
    db.commit()
    
    
def delete(db,key):
    print('||eliminando Data||')
    db.execute('delete from almacen where a1 = ?', (key,))
    db.commit()

def main():
    # Variable para conectar a la bd
    db = sqlite3.connect('almacen.db')
    db.row_factory = sqlite3.Row
    db.execute('drop table if exists almacen')
    db.execute('create table almacen (a1 text,i1 int)')

    insert(db,dict(a1='Jesus', i1=19))
    insert(db,dict(a1='Joaco', i1=20))
    insert(db,dict(a1='Nacha', i1=21))
    insert(db,dict(a1='Nico', i1=25))
    show(db)
    
    
    print(dict(read(db,'Joaco')),dict(read(db,'Nico')))
    
    uptdate(db,dict(a1 = 'Joaco',i1 = 19))
    show(db)    
    delete(db,'Nacha')
    show(db)
    

main()
