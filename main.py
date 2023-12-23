
from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

import numpy as np


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline('zero-shot-classification', model='roberta-large-mnli')

_labels = ['good', 'bad', 'ugly']


@app.get("/")
def root():
    """default response"""
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    """Sentiment analysis for a text"""
    c = classifier(item.text, _labels)
    i = np.argmax(c["scores"])
    label = c["labels"][i]
    return f"most probable label is {label}"
