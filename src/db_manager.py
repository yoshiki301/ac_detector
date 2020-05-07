import sqlite3

class sqlite3manager():

    def __init__(self, db_path='database.sqlite3'):
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()

    def db_create(self):
        query = """
            CREATE TABLE IF NOT EXISTS ac_submission(
                id integer,
                problem_id integer,
                user_id string,
                language string
            )
        """
        self.c.execute(query)
        self.conn.commit()
        query = """
            CREATE TABLE IF NOT EXISTS resister_user(
                id integer,
                user_id string
            )
        """
        self.c.execute(query)
        self.conn.commit()

    def db_manipulate(self, query, fetch=False, commit=False):
        self.c.execute(query)
        if fetch:
            res = self.c.fetchall()
            return res
        elif commit:
            self.conn.commit()

