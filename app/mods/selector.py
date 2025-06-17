from sqlalchemy import create_engine, text

class Selector():
    def __init__(self, name, command):
        self.engine = create_engine(f"sqlite:///{name}")
        self.command = command
    
    def select_where(self):
        with self.engine.connect() as conn:
            return conn.execute(text(self.command)).fetchall()
            conn.commit()

    def select_all(self):
        with self.engine.connect() as conn:
            return conn.execute(text(self.command)).fetchall()
            