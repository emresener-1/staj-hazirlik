from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI ()

class NoteIn(BaseModel):
    title: str
    content: str

notes = []
next_id = 1

@app.get("/")
def root():
    return {"message": "Day 4 API is running"}

@app.get("/notes")
def list_notes():
    return notes

@app.post("/notes")
def create_note(note: NoteIn):
    global next_id
    new_note = {
        "id": next_id,
        "title": note.title,
        "content": note.content
    }
    notes.append(new_note)
    next_id += 1
    return new_note

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for n in notes:
        if n["id"] == note_id:
            return n
    raise HTTPException(status_code=404, detail="Note not found") 
  