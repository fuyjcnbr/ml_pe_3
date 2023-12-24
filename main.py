
from fastapi import FastAPI
from pydantic import BaseModel

import numpy as np


class Item(BaseModel):
    text: str


_labels = ['good', 'bad', 'ugly']

app = FastAPI()


@app.get("/")
def root():
    """default response"""
    return {"message": "Hello World"}


if __name__ == '__main__':
    from transformers import pipeline

    classifier = pipeline('zero-shot-classification', model='roberta-large-mnli')

    @app.post("/predict/")
    def predict(item: Item):
        """Sentiment analysis for a text"""
        c = classifier(item.text, _labels)
        i = np.argmax(c["scores"])
        label = c["labels"][i]
        return f"most probable label is {label}"
