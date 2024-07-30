def write_to_file(data):
  """
  Appends data to a text file.

  Args:
      data: The data to write to the file.
  """
  with open("log.txt", "a") as file:
    file.write(data + "\n")

def main():
  """
  Simulates user input and writes it to a file for demonstration.
  """
  while True:
    user_input = input("Enter some text (press q to quit): ")
    if user_input.lower() == 'q':
      break
    write_to_file(user_input)
  print("Exiting program.")

if __name__ == "__main__":
  main()
