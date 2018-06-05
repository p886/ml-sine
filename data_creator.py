import csv
import random
import math
import os.path

configs = [
  {
    "filename": 'data_train.csv',
    "size": 10000,
  },
  {
    "filename": 'data_test.csv',
    "size": 1000,
  }
]

for config in configs:
  with open(os.path.join('data', config["filename"]), 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    for n in range(0, config["size"]):
      x = random.randint(0,7) + random.random()
      writer.writerow([x, math.sin(x)])

print("Finished creating data")
