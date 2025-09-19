from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres:sMc110499meNcp@127.0.0.1/pmd_dev"
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        print("Connected successfully!")
except Exception as e:
    print("Connection failed:")
    print(e)
