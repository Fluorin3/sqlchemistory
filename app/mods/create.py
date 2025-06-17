from sqlalchemy import create_engine, text

class Creator():

    def __init__(self, name, command):

        self.engine = create_engine(f'sqlite:///{name}')
        self.command = command
    
    def create_table(self):

        with self.engine.connect() as conn:
            conn.execute(text(self.command))
            conn.commit()


def create_database(name):

    file = open(name, 'w')
    file.close()

