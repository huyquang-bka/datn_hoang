import json

path = "/Users/huyquang/Downloads/annotation_val.odgt"

with open(path, "r") as f:
    for line in f.readlines():
        data = json.loads(line)
        print(data)
        break