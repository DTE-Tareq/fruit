from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
DATABASE_URL = "postgresql+psycopg2://fruitdb_h3wr_user:8sYFQordKIXbAMB9V91Bjd2YOv0dKpqN@dpg-dc3bdvqjnfac73a9bpng-a.ohio-postgres.render.com/fruitdb_h3wr"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
