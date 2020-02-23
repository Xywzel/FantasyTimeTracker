import re

# Remove extra white spaces and swap single spaces to underscores
# for use as file name or internal link
def simplify(line):
    line = re.sub(r"[^\w\s]", ' ', line).strip().lower()
    line = re.sub(r"\s+", '_', line)
    return line

# Given filename, reads it and returns a list of rows
def read_list(filename):
    with open(filename) as f:
        data = f.read()
        return data.splitlines()

# Read csv file separated by ':' and return list of objects of specified type
def object_from_csv(Type, filename):
    alist = read_list(filename)
    blist = [[x.strip() for x in a.split(";")] for a in alist if not a.startswith("#")]
    return [Type(*param) for param in blist]

def list_from_csv(filename):
    print(filename)
    alist = read_list(filename)
    blist = [[x.strip() for x in a.split(";")] for a in alist if not a.startswith("#")]
    return blist

# Reads whole file into single string
def read_file(filename):
    with open(filename) as f:
        data = f.read()
        return data
