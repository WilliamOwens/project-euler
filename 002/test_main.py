from main import evenFibonacci, readFile

def test():
  _input = readFile("test_input.txt")
  assert evenFibonacci(_input) == 44
  assert evenFibonacci(_input) != 45

if __name__ == "__main__":
  test()