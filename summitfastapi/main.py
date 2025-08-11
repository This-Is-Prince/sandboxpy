from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

class Tea(BaseModel):
    id: int
    name: str
    origin: str

teas: List[Tea] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to chai code"}

@app.get("/teas")
def get_teas():
    return teas

@app.post("/tea")
def add_tea(tea: Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for i, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[i] = update_tea

    return {"message": "success"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for i, tea in enumerate(teas):
        if tea.id == tea_id:
            return teas.pop(i)

def main():
    print("Hello from summitfastapi!")


if __name__ == "__main__":
    main()
