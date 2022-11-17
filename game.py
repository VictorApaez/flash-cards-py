from models import Note
from flask import Flask, jsonify, request
from playhouse.shortcuts import model_to_dict, dict_to_model

def note_taker():
  note_title = input("Insert a title for you note: ")
  note_msg = input("Insert a message for you note: ")

  new_note = Note(title=f"{note_title}", message=f"{note_msg}")
  new_note.save()
  
  all_notes = input("Do you want to see your notes? (y/n): ")
  if all_notes.lower() == "y":
    print("\n    Here are all your notes!")
    for note in [model_to_dict(note) for note in Note.select()]:
      print(f"{note['title']}: {note['message']}")
  print("\n Goodbye!")


note_taker()