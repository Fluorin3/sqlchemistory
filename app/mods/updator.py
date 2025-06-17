from sqlalchemy import create_engine, text

class Updator():

    def __init__(self, command, db_name):
        self.engine = create_engine(f'sqlite:///{db_name}')
        self.command = command

    def update(self):
        
        with self.engine.connect() as conn:
            conn.execute(text(self.command))
            conn.commit()
        