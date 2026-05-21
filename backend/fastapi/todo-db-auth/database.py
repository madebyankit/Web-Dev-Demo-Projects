from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker	

SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"

engine = create_engine(
		SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# "check_same_thread": It allows the SQLite database to be accessed from multiple threads. 
# By default, SQLite does not allow multiple threads to access the same database connection, 
# which can lead to issues in a multi-threaded application. 
# Setting "check_same_thread" to False allows the application to bypass this restriction 
# and use the same connection across different threads.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# The sessionmaker function is used to create a new session factory. 
# The parameters passed to sessionmaker configure the behavior of the sessions it creates:
# - autocommit=False: This means that changes made to the database will not be automatically committed. 
				# You will need to explicitly call session.commit() to save changes to the database.
# - autoflush=False: This means that changes made to the database will not be automatically flushed to the database. 
				# You will need to explicitly call session.flush() to send changes to the database before they are committed.
# - bind=engine: This binds the session to the database engine created earlier, allowing the session to interact with the database.


Base = declarative_base()
# The declarative_base function is used to create a base class for your database models. 
# This base class will be used to define your database tables and their relationships.