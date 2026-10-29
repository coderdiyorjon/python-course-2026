# Day 04 — Independent Practice

These exercises reinforce variables, data types, `type()`, and naming rules. Do not only guess the answers; try to explain why each result occurs.

## 1. Predict the output

Before running the code, write down what each `print()` will display. Then run it and check your answers.

```python
value = 12
print(value, type(value))

value = "12"
print(value, type(value))

value = 12.0
print(value, type(value))

value = True
print(value, type(value))
```

Why do the values have different types even when some of them look similar?

## 2. Rebinding a name

```python
number = 5
other = number
number = 8

print(number)
print(other)
```

Write the output and explain why `other` does not become `8`.

## 3. Valid and invalid names

Sort these names into three groups: **valid**, **invalid**, and **valid but not a great style choice**.

- `user_name`
- `2user`
- `_count`
- `first name`
- `class`
- `total2`
- `FirstName`
- `list`
- `user-name`
- `AGE`

Explain why the invalid names fail. Explain why `list` is syntactically valid but is usually a poor variable name.

## 4. Inspect types

Write code that uses `type()` for each of the following:

- an integer;
- a floating-point number;
- a string;
- a Boolean value;
- `None`;
- a list;
- a dictionary.

Choose your own example value for each.

## 5. Values that look similar

Explain the difference between:

```python
a = 7
b = 7.0
c = "7"
```

Check their types. Try a few operations and observe which ones may raise an error.

## 6. Two names, one object

```python
first = [1, 2]
second = first
second.append(3)

print(first)
print(second)
```

Explain the output. Why is this different from `number = 5; other = number; number = 8`? For now, explain “mutable” and “immutable” in your own words.

## 7. Improve the names

Rename these variables using clear Python style:

- `x` — a user's age;
- `tp` — an order's total price;
- `a1` — whether a user is logged in;
- `n` — the number of attempts.

## 8. Challenge

Create a file named `student_profile.py`. Store each of these in a separate variable:

- the student's name;
- their age;
- the course name;
- a Boolean value indicating whether they are continuing the course;
- a final grade that has not been assigned yet (`None`).

Print each value and its type using `type()`. Use `snake_case` for variable names.

## Assessment criteria

- Predicted output is checked against actual output.
- Invalid identifiers are explained correctly.
- `type()` results are interpreted correctly.
- Rebinding a name is distinguished from multiple names referring to one object.
- The code uses readable names.
