def write_to_file():
 """
 Creates a new text file named "my_file.txt" and writes content to it.
 """
 try:
   with open("my_file.txt", 'w') as file:
     file.write("This is the first line of text.\n")
     file.write("Here's some more content with a number: 42.\n")
     file.write("The last line for now.\n")
   print("Successfully wrote content to my_file.txt")
 except Exception as e:
   print(f"Error writing to file: {e}")

def read_from_file():
 """
 Reads the contents of "my_file.txt" and displays them on the console.
 """
 try:
   with open("my_file.txt", 'r') as file:
     contents = file.read()
     print("Contents of my_file.txt:")
     print(contents)
 except FileNotFoundError:
   print("File 'my_file.txt' not found.")
 except Exception as e:
   print(f"Error reading from file: {e}")

def append_to_file():
 """
 Opens "my_file.txt" in append mode and writes additional content.
 """
 try:
   with open("my_file.txt", 'a') as file:
     file.write("\nAppended some new lines:\n")
     file.write("Line 1 of appended content.\n")
     file.write("Line 2 with another number: 100.\n")
     file.write("Line 3, the final addition.\n")
     file.write("Line 4, welcome to Nairobi in 2024")
     
   print("Successfully appended content to my_file.txt")
 except Exception as e:
   print(f"Error appending to file: {e}")

# Call the functions to perform file operations
write_to_file()
read_from_file()
append_to_file()
read_from_file()  # Read again to show appended content
