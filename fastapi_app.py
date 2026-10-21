from fastapi import FastAPI

app = FastAPI(title="Лабораторная работа 6")


# Задание 6: FastAPI «Hello»
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


# Задание 8: FastAPI принимает параметр и отвечает
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Привет, {name}!"}