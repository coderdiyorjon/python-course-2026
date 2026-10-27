# Day 03 — Python, IDLE, print(), and Comments

The goal of these tasks is not to simply copy code, but to confidently work with the installed environment and consciously predict the results of your first commands.

## 1. Checking the Python Environment

Do the following on your computer:

1. Find IDLE in the Start menu.
2. Verify that the Shell window opens in IDLE.
3. Open Windows Terminal or Command Prompt and try either `python --version` or `py --version`.
4. Note down which Python version is displayed.
5. In one sentence, explain the difference between Python, the interpreter, and IDLE.

If the terminal commands don't work, don't immediately conclude that Python isn't installed if IDLE is available. Record the error message and show it to your instructor.

## 2. First Python File

In IDLE, open a new Editor window via `File → New File`. Type the following and save it as `hello_world.py`:

```python
print("Hello World!")
```

Execute it by pressing `F5` or going to `Run → Run Module`.

Check:
- In which window did the result appear?
- Which file was the code saved to?
- What is the file's extension?
- If you run the program again, do you need to rewrite the code?

## 3. Different Forms of print()

Write the following code in a separate `print_basics.py` file and predict the result before running it.

```python
print("Hello, world!")
print("Python", "course")
print("Python" + " course")
print("Result:", 10 + 5)
print("2026", "10", "24", sep="-")
print("One line", end=" ")
print("continued")
```

Explain the result of each line. Especially explain the difference between using a comma and using `+`.

## 4. Your Own Greeting Program

Create a file named `my_introduction.py`. The program should consist of at least 5 lines and output the following:

- a greeting;
- your name or nickname;
- the course name;
- the IT field you want to learn;
- a concluding sentence.

Requirements:
- Use the `print("A", "B")` format at least once;
- Concatenate strings using `+` at least once;
- Use `sep` or `end` at least once;
- Save the file and try running it again.

## 5. Comments

In a file named `comments.py`, write examples for all three of the following situations:

1. A `#` comment on its own line.
2. An inline comment on the same line as code.
3. A block of comments spanning multiple lines.

Then, write one example of a bad comment and one example of a better comment. Explain the difference: a good comment explains *why* the code is written that way, while a bad or redundant comment just repeats what the code itself says.

Write one sentence about a text block enclosed in triple quotes: why can't it always be considered a comment?

## 6. Practical Check of IDLE Menus

Find and try each action in IDLE:

- Open the Editor via `File → New File`.
- Save the file with a new name via `File → Save As`.
- Undo and redo edits with `Edit → Undo` and `Edit → Redo`.
- Run the file via `Run → Run Module`.
- Find the font or color settings in `Options → Configure IDLE`. You don't have to change all the settings.
- Switch between the Shell and Editor via the `Window` menu.
- Find IDLE Help or Python Docs in the `Help` menu.

Note that the Shell menu might appear in the Shell window, and the Run/Format menu in the Editor window. Do not expect both windows to have identical menus.

## 7. Predicting Output Results

Without running the following code yet, write down the result of each line in a notebook or a Markdown file. Then run it to check.

```python
print("A", "B")
print("A" + "B")
print("A" + " " + "B")
print("X", "Y", sep="-")
print("First", end="...")
print("second")
print()
print("Finished")
```

Why is there a space in the first line, but not in the second? What happens if `end` is not changed? What does `print()` output if called without arguments?

## 8. Challenge — Small Console Greeting

Create a small program named `course_welcome.py`. It should greet a new student joining the course and output at least three pieces of information using multiple `print()` methods.

Additional conditions:
- Write a comment at the beginning of the program explaining what it does.
- Compare combining texts using `+` with passing multiple arguments separated by commas.
- Format the result so it's easy to read.
- Save the code in `examples/day03/`.

## Submission

The `examples/day03/` folder in your repository should contain `hello_world.py`, `print_basics.py`, `comments.py`, and at least one of the programs you wrote yourself. Written answers to tasks can be provided in a separate file or notebook depending on the submission method.