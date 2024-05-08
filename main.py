from fastapi import	FastAPI, Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class UserLogin(BaseModel):
    name: str
    last_name: str
    phone: str
    address: str
    age: str
    

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Métodos permitidos
    allow_headers=["*"],
    
)

@app.post("/login/")
async def login(user: UserLogin = Body(...)):
    return user.model_dump()








#uvicorn body_fastapi:app --reload
#curl -X POST "http://localhost:8000/login/" -H "Content-Type: application/json" -d '{"username":"john", "rol":"Developer"}'

"""json{
    "username": "juan",
    "rol": "admin"
}"""