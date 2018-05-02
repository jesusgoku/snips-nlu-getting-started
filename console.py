#!/usr/bin/env python
import io
import json
from snips_nlu import SnipsNLUEngine, load_resources

load_resources("es")

with io.open("trained.json") as f:
    engine_dict = json.load(f)

engine = SnipsNLUEngine.from_dict(engine_dict)

while True:
    phrase = input("Pregunta (Enter for exit): ")

    if len(phrase) == 0:
        break
    
    r = engine.parse(phrase)
    print(json.dumps(r, indent=2))