from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///database.db')
Base = declarative_base(engine)
Session = sessionmaker(engine)
