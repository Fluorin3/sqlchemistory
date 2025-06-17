from sqlalchemy import create_engine, text

class Inserter():

    def __init__(self, command, name):
        self.engine = create_engine(f"sqlite:///{name}")
        self.command = command

    def insert(self):

        with self.engine.connect() as conn:
            conn.execute(text(self.command))
            conn.commit()