
class db_map:
    def __init__(self):
        self.createTableNotes = """CREATE table if not exists notes(
                                        id integer PRIMARY KEY,
                                        note text
                                    )"""

        self.insertNote = """INSERT into notes(id, note)
                              VALUES(?,?)"""

        self.updateNote = "UPDATE notes SET note = ? WHERE id = ?"

    def createTableNotes_sql(self):
        return self.createTableNotes
    def insertNote_sql(self):
        return self.insertNote
    def updateNote_sql(self):
        return self.updateNote
    