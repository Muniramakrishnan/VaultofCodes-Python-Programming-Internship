def reverse_string(s):
  reversed = ""
  for i in range(len(s) - 1, -1, -1):
     reversed += s[i]
  return reversed
def main():
  input_string = "Hello, world!"
  reversed_string = reverse_string(input_string)
  print(f"Reversed string: {reversed_string}")
  main()
