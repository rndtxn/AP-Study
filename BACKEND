from fastapi import FastAPI
from pydantic import BaseModel
from quiz_generator import generate_quiz
from notes_analyzer import analyze_notes

app = FastAPI()

class Notes(BaseModel):
    text: str

@app.post("/quiz")
def quiz(notes: Notes):

    quiz = generate_quiz(notes.text)

    return {"quiz": quiz}


@app.post("/analyze-notes")
def notes_analysis(notes: Notes):

    result = analyze_notes(notes.text)

    return result
