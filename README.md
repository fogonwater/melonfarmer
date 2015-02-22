## melon.farmer()
---

Simple utilities that I seem to use all the time when harvesting metadata.

Import the module and create a farmer.

```
import melon
farmer = melon.Farmer()
```

### Some example uses.

Get more console messages.
```
farmer.verbose = True
```

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

Write a list of lists to a CSV file.
```
report = [
    ['col_a', 'col_b', 'col_c'],
    [1, 'melon', 'yes'],
    [9, 'apple', 'no'],
    [4, 'melon', 'maybe']
]
farmer.list_to_csv(report,'data/test.csv')
```

Load CSV as a list of dictionaries.
```
d3 = farmer.read_csv('data/test.csv')
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
