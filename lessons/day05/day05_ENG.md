

# Lesson 05 — User Input, Type Conversion, and f-strings

**Date:** 29 October 2026  
**Topics:** `input()`, type conversion, and f-strings

## A program cannot rely only on predefined data

When we begin learning programming, we usually display information using `print()`:

```python
print("Hello, world!")
print("We are learning Python.")
```

These statements produce the same output every time the program runs. The information is predefined, so the program is static in this respect.

Real applications often need information such as a user's name, age, email address, or other details. Rewriting the code for every user would not make sense. Instead, a program should be able to receive information from the user.

In Python, we use the `input()` function for this purpose.

## `input()` — receiving information from the user

The `input()` function pauses program execution and waits until the user presses Enter. We can pass a string as an argument to tell the user what to enter.

```python
name = input("Enter your name: ")

print("Hello,", name)
```

The program asks the user for a name and assigns the entered value to the `name` variable.

Another example:

```python
age = input("Enter your age: ")

print("Your age is:", age)
```

There is one important detail here: **`input()` always returns a value of type `str`.**

Even if the user enters `18`, Python receives it as the string `"18"`, not as an integer.

We can verify this using `type()`:

```python
age = input("Enter your age: ")

print(type(age))
```

Output:

```text
<class 'str'>
```

This distinction becomes especially important when our program needs to perform mathematical calculations.

## Why do we need to convert data types?

Suppose we ask the user for their age and then try to estimate their birth year:

```python
age = input("Enter your age: ")

birth_year = 2026 - age
```

This code does not work. The reason is that `2026` is an `int`, while `age` is a `str`. Python cannot subtract a string from an integer, so it raises a `TypeError`.

Strings can be concatenated with other strings, but that is not the same as arithmetic addition:

```python
age = "18"

print(age + "1")
```

Output:

```text
181
```

Python joined the two strings. Therefore, before performing a mathematical operation, we need to convert the data to a suitable type.

## Type conversion

Python provides several built-in functions for converting values from one type to another. The most commonly used ones at this stage are:

- `int()` — converts a value to an integer when possible.
- `float()` — converts a value to a floating-point number when possible.
- `str()` — converts a value to a string.
- `bool()` — converts a value to a Boolean value.

First, let's use ordinary variables without `input()`:

```python
number = "25"

converted_number = int(number)

print(converted_number)
print(type(converted_number))
```

Output:

```text
25
<class 'int'>
```

`int()` converted a string containing an integer into an actual integer value.

Now let's work with a floating-point number:

```python
price = "19.99"

converted_price = float(price)

print(converted_price)
print(type(converted_price))
```

Output:

```text
19.99
<class 'float'>
```

We can also convert a number into a string:

```python
number = 100

text = str(number)

print(text)
print(type(text))
```

Output:

```text
100
<class 'str'>
```

This is useful when we need to combine numeric values with text.

### Conversion does not always succeed

Python raises an error when it cannot convert a value to the requested type.

For example:

```python
age = int("eighteen")
```

The string `"eighteen"` does not contain a numeric representation that `int()` can parse. Therefore, Python raises a `ValueError`.

Consider another example:

```python
number = int("18.5")
```

This also raises a `ValueError`. The string `"18.5"` contains a decimal part and is not a valid integer representation for `int()`.

However, the following two cases are different:

```python
print(int(18.5))
print(int("18.5"))
```

In the first line, `18.5` is already a `float`. `int()` removes its fractional part and returns `18`.

In the second line, `int()` cannot directly parse the string `"18.5"`, so a `ValueError` is raised.

Remember: `int()` does not round a floating-point number. It truncates the fractional part. For example, `int(-3.9)` returns `-3`.

In other situations, `TypeError` is raised when the object provided is not suitable for the operation. For example, `int(None)` cannot be performed.

These two errors have different causes:

- `ValueError` — the type of the input may be acceptable, but its value cannot be converted as requested.
- `TypeError` — the object type is not suitable for the operation being performed.

One more important detail: converting text with `bool()` does not interpret the words `"True"` and `"False"` as Boolean literals. Any non-empty string, including `"False"` and `"0"`, evaluates to `True`. Therefore, passing user-entered text directly to `bool()` is not a reliable way to parse textual Boolean values.

## Using conversion with `input()`

Now let's combine what we have learned:

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", age)
print("Your age next year:", age + 1)
```

This time, the text returned by `input()` is immediately converted into an integer using `int()`.

The following statement:

```python
age = int(input("Enter your age: "))
```

logically consists of two steps:

1. `input()` receives text from the user.
2. `int()` converts that text into an integer.

Therefore, it has the same meaning as:

```python
age_text = input("Enter your age: ")
age = int(age_text)
```

If the user enters something such as `"eighteen"` or `"18.5"` instead of an integer, the program stops with a `ValueError`. At this stage, understanding why the error occurs is important. In later lessons, we can learn to handle such situations using `try` and `except`.

## The problem with calculating a birth year from age

Suppose we know the user's age and want to calculate their birth year:

```python
age = int(input("Enter your age: "))

birth_year = 2026 - age

print("You were approximately born in", birth_year)
```

This calculation may be useful in some situations, but its result is not always exact.

Why?

We do not know whether the user's birthday has already occurred in the current year. For example, on 29 October 2026, a person who is 20 years old could have been born in either 2005 or 2006.

This means that age alone cannot always tell us the exact date of birth — or even the exact birth year. We also need the person's birth day and month to calculate it accurately.

This example teaches us another important idea: a program's correctness depends not only on the code, but also on whether the supplied information is sufficient.

## `print()` and f-strings

In previous examples, we used commas inside `print()` to display multiple values:

```python
name = "Ali"
age = 20

print("Name:", name, "Age:", age)
```

Output:

```text
Name: Ali Age: 20
```

This approach is convenient because `print()` accepts values of different types as separate arguments and normally places a space between them.

However, in larger programs, we often want our output to be more structured and readable. This is where f-strings become useful.

F-strings were introduced in Python 3.6. Their basic syntax looks like this:

```python
name = "Ali"
age = 20

print(f"My name is {name}, and I am {age} years old.")
```

Output:

```text
My name is Ali, and I am 20 years old.
```

The `f` prefix tells Python that the string is a formatted string. We can place variables or expressions inside curly braces `{}`.

For example:

```python
a = 10
b = 5

print(f"{a} + {b} = {a + b}")
```

Output:

```text
10 + 5 = 15
```

An f-string can contain Python expressions, not just variable names.

### Formatting numbers

F-strings also allow us to display numbers in a cleaner format:

```python
price = 19.9876

print(f"Price: {price:.2f}")
```

Output:

```text
Price: 19.99
```

The `:.2f` format specification displays the number with two digits after the decimal point.

Another example:

```python
name = "Ali"
score = 95.5

print(f"{name} scored {score:.1f} points.")
```

Output:

```text
Ali scored 95.5 points.
```

F-strings provide a readable way to combine text and values in a single string.

## Comparing three approaches

All three examples below serve the same purpose:

```python
name = "Ali"
age = 20

# Using commas
print("Name:", name, "Age:", age)

# Using string concatenation
print("Name: " + name + " Age: " + str(age))

# Using an f-string
print(f"Name: {name} Age: {age}")
```

In the second approach, we need `str()` to convert `age` into a string. Python cannot directly concatenate a `str` and an `int` using `+`.

F-strings are usually more convenient and easier to read in this situation.

## Common mistakes

Keep these cases in mind:

```python
age = input("Age: ")
print(age + 1)  # TypeError: cannot add str and int
```

```python
age = int(input("Age: "))
print(age + 1)  # Works if the user enters an integer
```

```python
price = float("19.99")  # Valid
```

```python
price = int("19.99")  # ValueError
```

```python
print("Age: " + 20)  # TypeError
```

```python
print(f"Age: {20}")  # Valid
```

## At the end of this lesson

In this lesson, we learned how to receive information from a user, inspect the type returned by `input()`, convert values to the required types, and format output using f-strings.

The most important idea is: **before using user-provided data, check its type and make sure its value has the form your program expects.**

In the next lessons, we will use user input to make decisions in our programs and begin working with conditions and logical expressions.

