

# Lesson 05 — Practice Tasks

**Topics:** `input()`, type conversion, and f-strings

These tasks are designed to reinforce the concepts covered in the lesson. The goal is to receive input from the user, handle data types correctly, and produce readable output using f-strings.

## 1. Personal introduction

Write a program that asks the user for their first name, last name, and age. Display the information in the following format:

```text
Hello, Ali Valiyev!
You are 20 years old.
```

Requirements:
- Store the first and last names as `str` values.
- Convert the age to `int`.
- Display the result using an f-string.

## 2. Age next year

Ask the user for their age and calculate how old they will be next year.

Example:

```text
Enter your age: 20
Next year, you will be 21 years old.
```

Remember to convert the input using `int()`.

## 3. Estimate the birth year

Ask the user for their age and estimate their birth year using the formula `2026 - age`.

Display the result in a format similar to this:

```text
You were approximately born in 2006.
```

**Think about it:** Why might this result not always be exact? What uncertainty remains when the day and month of birth are unknown?

## 4. Basic calculator

Ask the user to enter two numbers and display the following results:

- Their sum
- Their difference
- Their product
- Their quotient

Requirements:
- Read the values using `float()`.
- Display the results using f-strings.
- The second number must not be zero when performing division. For now, try checking this situation separately and observe what problem occurs if you divide by zero, even before learning conditional statements.

## 5. Store checkout

Ask the user for a product name, its price, and the quantity. Calculate the total price.

Example:

```text
Product name: Notebook
Price: 12.5
Quantity: 3

Product: Notebook
Price per item: 12.50
Quantity: 3
Total: 37.50
```

Requirements:
- The price must be a `float`.
- The quantity must be an `int`.
- Calculate the total using `price * quantity`.
- Display monetary values with two decimal places using f-strings.

## 6. Conversion experiments

Execute the following expressions separately and observe their results and errors:

```python
int("25")
int("25.5")
int(25.5)

float("25")
float("25.5")
float("hello")

str(25)
str(25.5)

bool("")
bool("False")
bool("0")
bool(0)
bool(1)
```

Try to explain why each expression produces its result. Record the expressions that raise errors as well.

## 7. Mini-project: Personal profile card

Create a small program that asks the user for the following information:

- Full name
- Age
- City
- Height in meters (for example, `1.75`)
- Favorite programming language

Use this information to display a neatly formatted profile. Convert each value to the appropriate type and format the result using f-strings.

Example:

```text
========== PROFILE ==========
Name: Ali Valiyev
Age: 20
City: Tashkent
Height: 1.75 m
Favorite language: Python
=============================
```

## Additional questions

1. Why does `input()` always return a `str`?
2. What is the difference between `int("12")` and `int("12.5")`?
3. What does `int(12.9)` return, and why?
4. What is the difference between `ValueError` and `TypeError`?
5. Why can't we determine an exact date of birth using only a person's age?
6. What is the difference between `print("Age:", age)` and `print(f"Age: {age}")`?
7. In which Python version were f-strings introduced?
8. Why does `bool("False")` evaluate to `True`?

