from fastapi import FastAPI
import secrets


app = FastAPI()

user_inf = {
    "login": "email@email.com",
    "password": "OASIKJLAKSHAOIUADOAIDLKJ&"
}

token_g = secrets.token_urlsafe(32)
token = {
    "token": f"{token_g}"
}
    


@app.get("/login")
async def login(login: str, password: str):
    if login == user_inf['login'] and password == user_inf['password']:
        return token['token']
    else:
        return "ERROR INVALID CREDENTIAL"
