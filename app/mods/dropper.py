from sqlalchemy import create_engine, text

class Dropper():

    def __init__(self, db_name, command):
        self.engine = create_engine(f'sqlite:///{db_name}')
        self.command = command

    def delete(self):
        with self.engine.connect() as conn:
            conn.execute(text(self.command))
            conn.commit()