from peewee import *
from flask import Flask, jsonify, request
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('notes', user='victorapaez', password='',
                        host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Note(BaseModel):
    title = CharField()
    message = CharField()