from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]
