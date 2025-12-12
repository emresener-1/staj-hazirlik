from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/double")
def double(x: int):
    return {"x": x, "double": x * 2} 