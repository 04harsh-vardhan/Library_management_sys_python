from sqlalchemy import create_engine

# here second parameter echo = True is used for logging
#pymysql is the db connection driver here
engine = create_engine("mysql+pymysql://root:Harshvardhan_123@localhost/LMS",echo=True)