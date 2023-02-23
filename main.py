# declare reserved keywords, operators, and separators as lists
keywords = [
  "function", "int", "bool", "real", "if", "else", "fi", "return", "get",
  "put", "while", "endwhile"
]
operators = ["+", "-", "*", "/", "=", "==", "!=", ">=", "<="]
separators = ["(", ")", ",", "{", "}", ";", "#", "[*", "*]"]
skip = [' ', '\n', '\t']


# function to tokenize the input code
def tokenize(code):
  tokens = []
  i = 0
  while i < len(code):
    # skip white space
    for space in skip:
      if code[i] == space:
        i+=1
        continue

    # check for comments
    if code[i:].startswith("[*"):
      j = code[i:].find("*]")
      if j < 0:
        j = len(code) - i
      else:
        j += 2
      i += j
      continue

    # check for separators
    for sep in separators:
      if code[i:].startswith(sep):
        tokens.append([sep, "separator"])
        i += len(sep)
        break

    # check for operators
    for op in operators:
      if code[i:].startswith(op):
        tokens.append([op, "operator"])
        i += len(op)
        break

    # check for keywords, numbers, or identifiers
    j = i
    while j < len(code) and (code[j].isalnum() or code[j] == "."):
      j += 1
    word = code[i:j]
    if word in keywords:
      tokens.append([word, "keyword"])
    else:
      if word.isdigit():
        tokens.append([word, "INT"])
      elif '.' in word:
        try:
          tokens.append([float(word), "real"])
        except ValueError:
          #possibly don't need
          #tokens.append([word, "identifier"])
          continue
      else:
        for space in skip:
          if code[i] == space:
              i+=1
              continue
        tokens.append([word, "identifier"])
    i = j
  return tokens


if __name__ == "__main__":
  # example code to tokenize
  var = input("Enter your Rat Code File Name: ")
  with open(var, 'r') as file:
    # read the contents of the file into a string
    file_contents = file.read()

    code = file_contents
    #code = "while (fahr <= upper) a = 2300.045; endwhile"

    # tokenize the code
    tokens = tokenize(code)

    # print the tokens
    print("Token                Lexeme")
    for token in tokens:
      print("{:<20} {}".format(token[1], token[0]))
