## melon (farmer)
---

Simple utilities for harvesting data + reading and writing files.

Import just what you need...

```
from melon import read_json, list_to_csv
```

... or [import melon as farmer](https://www.youtube.com/watch?v=PwN3SoWSUrY) if that's how you roll.

```
import melon as farmer
```

### Some example uses.

Get some json and write to a file.
```
url = 'https://api.github.com/users/fogonwater/repos'
d1 = farmer.get_json(url)
farmer.write_json(d1, 'data/test1.json')
```

Write json to file and then read it back.
```
farmer.write_json({'foo' : 'bar'}, 'data/test2.json')
d2 = farmer.read_json('data/test2.json')
```

Post json to a webservice.
```
farmer.post_json({'foo' : 'bar'}, 'http://example.com')
```

Write a list of dictionaries to a CSV file. (Assumes all dicts have identical keys.)
```
report = [
    {'num':0,'day':'Mon'}, 
    {'num':1,'day':'Tue'}
]
farmer.dict_to_csv(report,'data/test1.csv')
```

Write a list of lists to a CSV file.
```
report = [
    ['col_a', 'col_b', 'col_c'],
    [1, 'melon', 'yes'],
    [9, 'apple', 'no'],
    [4, 'melon', 'maybe']
]
farmer.list_to_csv(report,'data/test2.csv')
```

Load CSV as a list of dictionaries.
```
rows = farmer.read_csv('data/test2.csv')
```

Get a list of all .json files in a directory called 'data'.
```
json_files = farmer.get_filenames('data', suffix='.json')
print(json_files)
```

Check to see whether specific files exist.
```
json_files = farmer.get_filenames('data', suffix='.json')
json_files.append('red_herring.json')
for f_name in json_files:
    if farmer.file_exists(f_name):
        print("{} exists.".format(f_name))
    else:
        print("{} does not exist.".format(f_name))
```
