import json

infile='postgres_classic_1981PhRvD..23..347G.json'
outfile='new_1981PhRvD..23..347G.json'

with open(infile, 'r') as fj:
    data = json.load(fj)


with open(outfile, 'w') as fj:
    fj.write("%s\n" % json.dumps(data, indent=2, sort_keys=True))
