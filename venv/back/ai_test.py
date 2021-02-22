#!/usr/bin/env python
from .ai import Ai

ai = Ai()


def test_with_one():
    img = "./assets/one.png"

    value = ai.predict(img, True)

    assert value == 1

