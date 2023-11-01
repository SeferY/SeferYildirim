from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()




#testneu




'''import mysql.connector

class SQLAufgabe:
    def __init__(self, query):
        self.query = query
        self.mycursor = None
        self.mydb = None

    def execute_query(self):
        self.mydb = mysql.connector.connect(
            host="yedibela.dynv6.net",
            user="sefer1",
            password="Sefer007!?",
            database="temp"  # Ersetze "deine_datenbank" durch den Namen deiner Datenbank
        )
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(self.query)
        self.mydb.commit()

    def close_connection(self):
        if self.mycursor:
            self.mycursor.close()
        if self.mydb:
            self.mydb.close()


def sql_befehl(query):
    # Verwendung der SQLAufgabe-Klasse
    query = query
    sql_task = SQLAufgabe(query)
    sql_task.execute_query()
    sql_task.close_connection()

sql_befehl("CREATE TABLE x_tabelle (spalte1 INT, spalte2 VARCHAR(255))")
'''



















'''import mysql.connector

# datenbank initialisieren
mydb = mysql.connector.connect(
  host="yedibela.dynv6.net",
  user="sefer1",
  password="Sefer007!?"
)

mycursor = mydb.cursor()


class SQLAufgabe:
    def __int__(self, query):
        self.query = query
        mycursor.execute(query)
        mydb.commit()
        mydb.close()

'''

'''
# cursor erstellen
mycursor = mydb.cursor()

# auszuführender code
sql = "CREATE TABLE temp.neue_tabelle (spalte1 INT, spalte2 VARCHAR(255))"

# code ausführen
mycursor.execute(sql)

# Die Änderungen in der Datenbank speichern
mydb.commit()

# Die Verbindung zur Datenbank schließen
mydb.close()
'''
