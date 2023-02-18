from fastapi import FastAPI

myapp = FastAPI()

@myapp.get("/")

def home():
    return 'Hello, world, Welcome to Umars Database'
# 
# async def root():
#     return {"message": "Hello World"}


# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
