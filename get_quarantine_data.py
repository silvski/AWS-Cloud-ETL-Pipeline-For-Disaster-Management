#! /usr/bin/env python

# Import packages
import sys
import json
import jsonlines

# Get the system arguments
source = sys.argv[1]
destination = sys.argv[2]

# Read the data from source
with open(source) as f:
    data = f.readlines()


data = list(filter(lambda y:
                   len(y),
                   list(map(lambda x:
                            x.strip(), data))))
# Convert to json
data = list(map(lambda y: json.loads(y), data))

# Filter / separate per loc_type
loc_data = list(filter(lambda x:
                       x['loc_type']=='quarantine', data))

if not loc_data:
    loc_data.append({})

# Dump the data
with open(destination, 'w') as fout:
    writer = jsonlines.Writer(fout)
    writer.write_all(loc_data)
    writer.close()

sys.exit()