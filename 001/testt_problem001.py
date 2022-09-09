from problem001 import isMultipleOfThreeOrFive, readFile

def test():
  _input = readFile("test_input.txt")
  assert isMultipleOfThreeOrFive(_input) == 23
  assert isMultipleOfThreeOrFive(_input) != 24

if __name__ == "__main__":
  test()