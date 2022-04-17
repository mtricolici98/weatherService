from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base, sessionmaker

from conf import DATABASE_URL

engine = create_engine(DATABASE_URL)
Base = declarative_base(engine)
Session = sessionmaker(engine)
