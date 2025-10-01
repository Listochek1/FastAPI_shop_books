from dotenv import load_dotenv
import os
load_dotenv()
class Settings:
    
    user_db = os.getenv("USER_DB")
    password = os.getenv("PASSWORD")
    database = os.getenv("DATABASE")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")