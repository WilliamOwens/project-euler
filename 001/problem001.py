import os

def readFile(fileName):
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, fileName)) as file:
        _input = file.read().splitlines()
    return prepareData(_input)

def prepareData(l):
  return int(l[0])

def isMultipleOfThreeOrFive(l):
  return sum([i for i in range(1, l) if (i % 3 == 0 or i % 5 == 0)])

if __name__ == "__main__":
  _input = readFile("input.txt")
  print(isMultipleOfThreeOrFive(_input))