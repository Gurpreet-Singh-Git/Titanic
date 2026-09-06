from fastapi import FastAPI, Path

app = FastAPI()

# amazom.com/create-user

# GET - GET AN INFROMATION
# POST - CREATE SOMETHING NEW
# PUT - UPDATE
# DELETE - DELETE SOMETHING


students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"
    }
}
@app.get("/")
def home():
    return {"name": "First Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="Give student id", gt=0,lt=2)):
    return students[student_id]

#lt(less than), gt(greater than), le(less than =), ge(greater than =)
# goggle.com/get-student/1