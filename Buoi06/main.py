from fastapi import FastAPI, HTTPException, UploadFile, File
import json
import os
import shutil

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
    

DIRECTORY = os.getcwd()
@app.post("/images", tags=["UPLOAD"])
def upload_single_file(image: UploadFile = File(...)):
    try:
        file_save = os.path.join(DIRECTORY, "data", image.filename)
        with open(file_save, "wb") as tmp:
            shutil.copyfileobj(image.file, tmp)
        return {"filename": image.filename}
    except Exception as e:
        print(e)
        return {"success": False}