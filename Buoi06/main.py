from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

DATA_FILE = "students.json"
def read_student_data():
    try:
        with open(DATA_FILE, encoding="utf8") as f:
            return json.load(f)
    except Exception as ex:
        print(ex)
        return []

def get_student_by_id(id: int, data: list[Student]):
    for item in data:
        if item["id"] == id:
            return item
    return None

@app.get("/students")
def get_all_students():
    return read_student_data()

@app.get("/students/{id}")
def get_all_students(id: int):
    data = read_student_data()
    return get_student_by_id(id, data)

from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    gpa: float

@app.post("/students")
def create_new_student(model: Student):
    data = read_student_data()
    existed_std = get_student_by_id(id, data)
    if existed_std is None:
        data.append(model)
        # Save to file json
        return model
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Item {model.id}-{model.name} is existed."
        )