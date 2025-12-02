# City namer
Generate city names by removing "city" or "sity" from the end of randomly selected English words.

Run from the terminal or import into your own code.

## Terminal

Run with or without arguments.

### Without arguments
```
python city_namer.py
```

Generates 1 city name by default.

### With arguments
```
python city_namer.py 5
```

Generates 5 city names.

## Import

Call with or without arguments.

### Without arguments
```python
from city_namer import city_names

for city in city_names():
    print(city)
```

Generates 1 city name by default.

### With arguments
```python
from city_namer import city_names

for city in city_names(5):
    print(city)
```

Generates 5 city names.

## Limitation

Note that the number of city names available is limited by the number of words ending with "city" or "sity", and beyond this limit specifying a higher number will not generate more words.
