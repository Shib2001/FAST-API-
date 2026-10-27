import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text


#STEP-1 : GET THE URL FROM THE .env FILE
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)


# STEP -2 : let's create a engine the road to the database 
engine = create_engine(DATABASE_URL)
with engine.connect() as conn:
    version = conn.execute(text("SELECT version()"))
    print(f"Connected to the {version}")
