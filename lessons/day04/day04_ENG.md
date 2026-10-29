# Day 04 — Variables, Naming, and Basic Data Types

- **Date:** 27 October 2026
- **Module:** Python Fundamentals
- **Level:** Beginner

## The big idea

A program receives, processes, and produces information. To work with information, we need names that let us refer to values in our code. This is where variables come in.

For a first explanation, it is useful to imagine a variable as a labelled box. That model is only an approximation, though. More precisely, in Python a name is bound to an object. The name is not the object itself; it is how we refer to the object.

```python
age = 20
name = "Ali"
height = 1.78

print(name)
print(age)
print(height)
```

Here, `name`, `age`, and `height` are names bound to different values. The `=` symbol is not a mathematical equality sign in this context. It binds the result of the expression on the right to the name on the left. Therefore, `age = age + 1` is not an algebraic equation: Python first evaluates `age + 1`, then binds the resulting value to `age`.

## Variables and values

A variable is a name used to refer to a value in a program. A value is the data the program is working with.

```python
score = 100
score = 125
print(score)  # 125
```

After the second assignment, `score` is bound to `125`. If the old value `100` is no longer reachable through any name, Python may reclaim its memory. The exact memory-management mechanism depends on the Python implementation.

Multiple names can also refer to the same object:

```python
first = [1, 2, 3]
second = first
second.append(4)

print(first)   # [1, 2, 3, 4]
print(second)  # [1, 2, 3, 4]
```

A list is a mutable object. `second = first` does not create a new list; both names refer to the same list object. This is an early preview of object references and mutability, which will be studied more deeply later.

## Why do data types matter?

Python does not treat `25`, `25.0`, `"25"`, and `True` as the same kind of value. They may look similar, but their types and the operations they support are different.

```python
print(25, type(25))
print(25.0, type(25.0))
print("25", type("25"))
print(True, type(True))
```

Important beginner-level types include:

- `int` — integers, such as `10`, `-4`, and `0`.
- `float` — floating-point numbers, such as `3.14` and `-0.5`.
- `str` — text, such as `"Python"` or `'hello'`.
- `bool` — the logical values `True` and `False`.
- `NoneType` — the type of `None`, commonly used to represent the absence of a value.
- `list` — an ordered, mutable sequence.
- `tuple` — an ordered sequence that is generally immutable.
- `dict` — key-value mappings.
- `set` — a collection of distinct elements.

This is not a complete list of Python types, but it covers useful foundations.

## Primitive types and objects

Programming languages organize values in different ways. For example, Java treats primitive types such as `int` and `boolean` separately from object types. JavaScript also distinguishes primitive values, such as numbers and booleans, from objects, although some operations give primitives temporary object-like behaviour.

Python has an important characteristic: **nearly all values in Python are represented as objects**. `int`, `float`, `bool`, `str`, `list`, `dict`, and even functions are objects. It is therefore misleading to transfer the idea of “primitive types” from another language directly to Python.

Even an ordinary integer is an object:

```python
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("hello"))  # <class 'str'>
print(type(True))     # <class 'bool'>
print(type([1, 2]))   # <class 'list'>
```

Beginners do not need to study every internal detail of objects yet. Remember this: a name is bound to an object, and the object's type affects which operations make sense.

## What does it mean to be stored in memory?

A simple memory analogy can help, but it should not be mistaken for a promise about exact physical addresses. The Python language defines the relationship between names and objects; how objects are placed in memory depends on the interpreter implementation.

```python
x = 10
y = x
x = 20

print(x)  # 20
print(y)  # 10
```

When `y = x` runs, `y` becomes bound to the current integer value `10`. Later, `x = 20` binds `x` to another integer object, while `y` remains bound to `10`.

This is easy to understand with immutable objects such as integers. With mutable objects such as lists, multiple names referring to the same object can lead to surprising results. We will revisit that topic later.

## Python is dynamically typed

Python does not require a variable's type to be declared in advance. A name can be bound to objects of different types at different times.

```python
value = 10
print(value, type(value))

value = "ten"
print(value, type(value))

value = 10.5
print(value, type(value))
```

Here, `value` is first bound to an `int`, then a `str`, and finally a `float`. This is called dynamic typing.

A precise distinction matters: the object itself does not spontaneously change its type. The integer `10` remains an integer object. When `value = "ten"` runs, the name becomes bound to a different object with a different type. Saying “the variable's type changed” is convenient shorthand; more precisely, “the name is now bound to an object of another type.”

## The `type()` function

`type(value)` reports the type of a value. It is especially useful for beginners who want to check whether something is text, an integer, or another kind of value.

```python
age = 18
price = 12.5
title = "Python"
is_ready = False
nothing = None

print(type(age))
print(type(price))
print(type(title))
print(type(is_ready))
print(type(nothing))
```

The output usually looks like `<class 'int'>`. This is also a reminder that types themselves are objects in Python. In everyday code, `isinstance()` is often useful for type checks too, but we can explore that distinction later.

## Variable naming rules

Names should make the meaning of the data clear. These are valid Python identifiers:

```python
name = "Ali"
age = 20
AGE = 21
AGE2 = 22
_name = "internal convention"
first_name = "Ali"
firstName = "Ali"
user2 = "guest"
```

The core syntax rules are:

1. A name may start with a letter or an underscore (`_`).
2. A name cannot start with a digit.
3. After the first character, letters, digits, and underscores may be used.
4. Spaces are not allowed inside an identifier.
5. Names are case-sensitive: `name`, `Name`, and `NAME` are different names.
6. Python keywords such as `if`, `for`, `class`, and `return` cannot be used as variable names.
7. Names such as `!age`, `(publicKey`, or `private key` are invalid because they do not follow identifier rules.

Examples:

```python
# Valid
public_key = "abc"
_name = "Ali"
age2 = 18
FirstName = "Ali"

# Invalid examples — keep these commented out:
# 5name = "Ali"        # starts with a digit
# private key = "x"   # contains a space
# !age = 18             # starts with !
# class = "Python"      # keyword
```

Python supports Unicode identifiers, so names are not strictly limited to English letters. However, in team projects, English names using ASCII characters are often preferred for consistency and compatibility with tools.

## Syntax rules versus style conventions

`firstName` is syntactically valid. However, the common Python style for variable names is `snake_case`, such as `first_name`. This is a convention for readability and consistency, not a syntax requirement.

Good examples:

```python
student_name = "Ali"
total_price = 150
is_logged_in = True
number_of_attempts = 3
```

Less descriptive examples:

```python
x = "Ali"
tp = 150
a1 = True
n = 3
```

Short names such as `i` or `x` can be appropriate in a very local context, but meaningful names are usually better.

A leading underscore in a name such as `_name` commonly signals “intended for internal use.” It does not automatically make the value private or enforce access restrictions.

Avoid reusing built-in names such as `list`, `str`, or `type` for variables. For example, after writing `list = [1, 2]`, calling the built-in `list()` function becomes difficult in that scope.

## Try it yourself

Run this code in IDLE and observe the output:

```python
value = 100
print(value, type(value))

value = "100"
print(value, type(value))

value = 100.0
print(value, type(value))

a = 7
b = a
a = 9
print(a, b)
```

Ask yourself: why are `100`, `"100"`, and `100.0` not the same type? Why do `a` and `b` show different values at the end?

## By the end of the lesson

Students should be able to explain:

- the difference between a variable name and a value;
- what assignment with `=` does;
- how to inspect a type with `type()`;
- what dynamic typing means in Python;
- why Python values are treated as objects;
- the difference between a valid identifier and a style convention;
- the rules about keywords, leading digits, spaces, and case sensitivity.

## Teacher notes

Check these only if they were actually covered in class:

- [ ] The variable concept was explained.
- [ ] Basic data types were demonstrated.
- [ ] Primitive and object types were compared across languages.
- [ ] Python's object model was introduced.
- [ ] Dynamic typing and `type()` were demonstrated.
- [ ] Naming rules were explained with examples.
- [ ] Naming style and readability were discussed.
