import sys
from yaml import dump, serialize

fruit = {
  "Apple": "Red",
  "Orange": "Orange",
  "Banana": "Yellow"
} 

with open('py-dumped.yaml', 'w') as file:
  dump(fruit, file)

with open('py-dumped.yaml', 'w') as file:
  serialize(fruit, file)