# Getting Started with Snip NLP on Python

## Usage

```shell
pipenv install
pipenv shell
python console.py
# Enter weather questions
```

## From behind

### 01. Instal enviroment and depedencies

```shell
mkdir snip-nlp && cd snip-nlp
pipenv install snip-nlp
pipenv shell
```

### 02. Dataset

Create file `obtenerTiempo.txt` with example questions:

```
¿Qué tiempo hará [cuando:snips/time](mañana) en [donde:localidad](Molina de Aragón)?
¿Qué tal hará [cuando:snips/time](pasado mañana) en [donde:localidad](Ponferrada)?
¿Qué temperatura habrá [cuando:snips/time](mañana) en [donde:localidad](Frías)?
```

And another with example localities `localidad.txt`:

```
Burgos
Valladolid
Peñaranda de Bracamonte
Soria
Almazán
Íscar
Portillo
Toro
Fermoselle
Sahagún
Hervás
Oña
Saldaña
Sabiñánigo
Jaca
```

Now generate dataset:

```shell
generate-dataset --language es --intent-files obtenerTiempo.txt --entity-files localidad.txt > dataset.json
```

### 03. Training

Now training with next script `training.py`:

```python
#!/usr/bin/env python
import io
import json
from snips_nlu import load_resources, SnipsNLUEngine

load_resources("es")

with io.open("dataset.json") as f:
    dataset = json.load(f)

engine = SnipsNLUEngine()

engine.fit(dataset)

engine_json = json.dumps(engine.to_dict())
with io.open("trained.json",mode="w") as f:
    f.write(engine_json)
```

And execute traingin:

```shell
python training.py
```

### 04. Questions

Make next script `console.py`:

```python
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
```

And execute:

```shell
python console.py
```

## Reference

- [https://blog.adrianistan.eu/2018/04/17/natural-language-understanding-con-snips-nlu-en-python/](https://blog.adrianistan.eu/2018/04/17/natural-language-understanding-con-snips-nlu-en-python/)