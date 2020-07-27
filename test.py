import os
import sys
from random import randint
import melon as farmer
from pprint import pprint as pp


print("\n=== STARTING TESTS ===")
# test getting json
url = "https://api.github.com/users/fogonwater/repos"
d1 = farmer.get_json(url)
print("Retrieved Github repo info with {} entries.".format(len(d1)))
print("---")

if os.path.isdir("data"):
    print("Tests written to 'data' directory")
else:
    print(
        "* WARNING: Remaining tests require a directory called 'data'. Exiting early.."
    )
    print("Try: mkdir data")
    sys.exit()

# write json from http request to file
farmer.write_json(d1, "data/test1.json")
print("---")


# write dictionary to file & read it back
farmer.write_json(
    {"foo": "bar", "fruit_set": ["apple", "apple", "orange"]}, "data/test2.json"
)
print("---")
d2 = farmer.read_json("data/test2.json")
pp(d2)
print("---")

# get filenames for a directory
json_files = farmer.get_filenames("data", suffix=".json")
pp(json_files)
print("---")

# test if files exist
json_files.append("red_herring.json")
for f_name in json_files:
    if farmer.file_exists(f_name):
        print("{} exists.".format(f_name))
    else:
        print("{} does not exist.".format(f_name))
print("---")

# post json to url
# farmer.post_json({'foo' : 'bar'}, 'http://example.com')

# write list of lists to disc and read it back
report = [["a", "b", "c"]]
for num in range(6):
    report.append([randint(0, 9), randint(0, 9), randint(0, 9)])
farmer.list_to_csv(report, "data/test.csv")
csv_data = farmer.read_csv("data/test.csv")
pp(csv_data)
print("---")

farmer.write_text("Hello, World\n  something else here?", "data/written_text.txt")
print("---")


farmer.write_text("1,2,3\n4,5,6", "data/test_nohead.csv")
# read a headerless csv
csv_data = farmer.read_csv("data/test_nohead.csv", fieldnames=["foo", "bar", "blah"])
print('Reading a CSV with no fieldnames')
pp(csv_data)
print("---")

s = 'value1,"oh look, an embedded comma",value3'
print('Parsing a one-line string to CSV: {}'.format(s))
pp(farmer.parse_one_line_csv(s))

print("=== END TESTS ===")
