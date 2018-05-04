# letras-scaper
This scraper get songwriter and genre by letras.mus.br

### Requirements
This aplicattion use two scripts, search.js to get url from song in letra.mus.br and father.py with get composite and genre by link.

###### Requirements Python

```python
import BeautifulSoup
import requests
import json
import subprocess
import time
import sys
import re
import pprint
```

###### Requirements NodeJS
```node
google-search-scraper
minimist
```

#### To Execute
```
python father.py <file_name>
```

#### Example
The file example.json contains
```json
[
	{"title":"Fix You","artist":"Coldplay"},
	{"title":"7 Years","artist":"Lukas Graham"}
]
```

Execute:
```bash
python father.py example 
```

generate example.csv with contains
```csv
Fix You;Coldplay;https://www.letras.mus.br/coldplay/183253/;Chris Martin / Guy Berryman / Jonny Buckland / Will Champion;Pop
7 Years;Lukas Graham;https://www.letras.mus.br/lukas-graham/7-years/traducao.html;Morten Ristorp / Morten Pilegaard / David Labrel / Stefan Forrest / Lukas Forchhammer / Christopher Brown;Pop
```
