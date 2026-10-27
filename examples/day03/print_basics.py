"""Examples of print(), separate arguments, string concatenation, sep, and end."""

# A single string argument.
print("Hello World!")

# Multiple arguments: print inserts a space by default.
print("Hello", "World!")
print("Course:", "Python Fundamentals")
print("Result:", 10 + 5)

# The + operator concatenates strings; it does not insert spaces automatically.
print("Hello" + "World!")
print("Hello" + " " + "World!")

# sep controls the separator between multiple arguments.
print("2026", "10", "24", sep="-")
print("red", "green", "blue", sep=" | ")

# end controls what is printed after the final argument.
print("This is the first part", end=" ")
print("and this is the second part.")

# Calling print() without arguments prints a blank line.
print()
print("The previous line was blank.")

# This would raise TypeError because + cannot concatenate str and int:
# print("Age: " + 18)

# These alternatives work:
print("Age:", 18)
print("Age: " + str(18))
