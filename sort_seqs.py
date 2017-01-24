import sys

def parse_fas(file_path):
    with open(file_path) as fas_file:
        lines = fas_file.read().splitlines()
    if len(lines) % 2 != 0:
        raise Error(".fas file must contain even number of lines")
    ids = lines[::2]
    ids = [id.lstrip(">") for id in ids]
    vals = lines[1::2]
    assert len(ids) == len(vals)
    mappings = {}
    for id, v in zip(ids, vals):
        mappings[id] = v
    return mappings

def write_fas(seqs, order, file_path):
    assert len(order) == len(seqs)
    sorted = []
    for elem in order:
        sorted.append(">" + elem)
        sorted.append(seqs[elem])
    with open(file_path, 'w') as fas_file:
        fas_file.write("\n".join(sorted))

if __name__ == "__main__":
    seqs = parse_fas(sys.argv[1])
    with open(sys.argv[2]) as order_file:
        order = order_file.readlines()[0].rstrip(";\n").split(", ")
    write_fas(seqs, order, sys.argv[3])