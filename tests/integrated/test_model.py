from transformers import pipeline

from numpy import argmax

from main import _labels


classifier = pipeline('zero-shot-classification', model='roberta-large-mnli')


def test_good():
        c = classifier("i am happy", _labels)
        i = argmax(c["scores"])
        label = c["labels"][i]
        assert label == "good"


def test_bad():
        c = classifier("nothing is good", _labels)
        i = argmax(c["scores"])
        label = c["labels"][i]
        assert label == "bad"
