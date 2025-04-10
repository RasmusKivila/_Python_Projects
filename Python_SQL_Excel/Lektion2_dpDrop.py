from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Skapa en engine och en session
engine = create_engine('sqlite:///Hemuppgift.db')
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# Drop alla tabeller
Base.metadata.drop_all(bind=engine)

# Commit
session.commit()
