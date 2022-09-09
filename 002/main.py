import os

def readFile(fileName):
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, fileName)) as file:
        _input = file.read().splitlines()
    return prepareData(_input)

def prepareData(l):
  return int(l[0])

def evenFibonacci(l):
  runningTotal = 0
  x = 1
  y = 2
  while (y < l):
    temp_y = y
    if (y % 2 == 0):
      runningTotal += y
    y = x + y
    x = temp_y
  return runningTotal


if __name__ == "__main__":
  _input = readFile("input.txt")
  print(evenFibonacci(_input))