class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://duck:lake@localhost:5432/GH'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SECRET_KEY = 'isthistheseed?'
    JWT_ERROR_MESSAGE_KEY = 'error message 86'