from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create a SQLite database engine
engine = create_engine('mysql+pymysql://root:root@localhost/game_platform')

# Create a session maker object for interacting with the database
Session = sessionmaker(bind=engine)
