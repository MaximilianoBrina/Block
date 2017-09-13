import sqlite3
base = sqlite3.connect('block2.db')

base.execute('''CREATE TABLE "BLOCK2" (
`ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
`TITULO`	TEXT,
`TEXTO`	TEXT,
`FECHA`	DATE,
`ESTADO`	INTEGER
);''')
base.execute('''CREATE TRIGGER NUEVO_REGISTRO AFTER INSERT ON BLOCK2
BEGIN
UPDATE BLOCK2 SET FECHA = DATETIME('NOW', 'LOCALTIME')
WHERE rowid = new.rowid;
END;''')
base.execute('''CREATE TRIGGER NUEVO_ESTADO AFTER INSERT ON BLOCK2
    BEGIN
    UPDATE BLOCK2 SET ESTADO = 'ACTIVO'
    WHERE rowid = new.rowid;
    END;''')

base.commit()

base.close()
