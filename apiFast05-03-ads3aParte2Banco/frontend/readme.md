RUN BACK
cd backend
python -m venv env
env/Scripts/activate
(env)pip install -r requirements.txt
(env)python main.py
http://127.0.0.1:8000/   
no pc, é o mesmo que 
http://localhost:8000/  
porém localhost é entendido na nuvem como o local que subir

RUN FRONT
cd frontend
npm install
npm run start
http://localhost:3000

RUN BANCO DE DADOS
docker compose up -d