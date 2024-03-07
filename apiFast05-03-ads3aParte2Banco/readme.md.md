cd backend
python -m venv env
env/Scripts/activate
(env)pip install -r requirements.txt
(env)python main.py

http://localhost:8000/


cd frontend
npm install
npm run start
ir para http://localhost:3000

docker compose up -d

# default
engine = create_engine("postgresql://scott:tiger@localhost/mydatabase")

# psycopg2
engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/mydatabase")

# pg8000
engine = create_engine("postgresql+pg8000://scott:tiger@localhost/mydatabase")
More notes on connecting to PostgreSQL at PostgreSQL.

MySQL
The MySQL dialect uses mysqlclient as the default DBAPI. There are other MySQL DBAPIs available, including PyMySQL:

# default
engine = create_engine("mysql://scott:tiger@localhost/foo")

# mysqlclient (a maintained fork of MySQL-Python)
engine = create_engine("mysql+mysqldb://scott:tiger@localhost/foo")

# PyMySQL
engine = create_engine("mysql+pymysql://scott:tiger@localhost/foo")


# sql server
engine = create_engine("mssql+pymssql://scott:tiger@hostname:port/dbname")