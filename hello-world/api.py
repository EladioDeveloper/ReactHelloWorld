from fastapi import FastAPI
from calc import Calc
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/sumar")
def read_sumar(self, num1, num2):
    return "Hola"