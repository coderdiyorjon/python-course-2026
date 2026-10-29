# Day 03 — Installing Python, Getting to Know IDLE, and Writing the First Program

**Date:** 24.10.2026  
**Module:** Introduction to Python  
**Level:** Beginner  
**Central idea of the lesson:** prepare the environment for programming, distinguish the place where code is written from the place where its output appears, and give the computer the first precise instructions.

## What do we start with?

In the previous lesson, we discussed algorithms, data, and how information is represented in a computer. Now we will put those theoretical ideas into practice. To write a program, we need the Python interpreter on the computer, an editor in which to write code, and a way to see the result. In this first practical session, we will install these components, distinguish their roles, and create the simplest working program.

By the end of the lesson, students should be able to find the installer on the official Python website, check whether Python is installed, explain the difference between IDLE Shell and Editor, create and save a new `.py` file, and run it. They should also understand how to display text with `print()`, the difference between using a comma and `+`, and why comments are useful.

## 1. Where do we download Python, and why use the official source?

The first question when installing software is: where should we get it? The official website for Python is [python.org](https://www.python.org/). The downloads page offers an installer or Python install manager suitable for the operating system. There is no need to download an installer at random from another website: the official source makes it easier to verify the version, security, and correct distribution.

On the lesson date, 24 October 2026, the Windows page had a traditional installer for Python 3.13.17. Python versions change over time. As of 27 October 2026, the official page lists 3.15.2 as the latest feature release and 3.14.10 as an updated release in the 3.14 series; 3.13.18 is a security release for which no Windows installer is provided. Therefore, it is important to check which version is installed on the computers used by the course and keep the group on a consistent version suitable for the course. Version numbers change, so remembering how to check the version is more important than memorising a particular number.

Official Python Windows page: <https://www.python.org/downloads/windows/>  
General Python downloads page: <https://www.python.org/downloads/>

### Installation on Windows

1. Open `python.org` in a browser.
2. Open **Downloads**, then go to the **Windows** page.
3. Choose the Python version selected for the course and the package appropriate for the computer. Most modern Windows computers use 64-bit x86-64, but ARM devices may need a separate package.
4. Follow the installation instructions on the official page. The options shown in the installer may vary by distribution and version.
5. If the classic installer shows **Add python.exe to PATH**, enable it if the course expects students to run Python using the `python` command in a terminal. The process may differ with the new Python install manager or another installation method.
6. After installation, open **IDLE (Python 3.x ...)** from the Start menu. IDLE is usually installed alongside Python's main components.
7. To verify the installation, try `py --version` or `python --version` in Windows Terminal or Command Prompt. Depending on the installation type, one of these commands may not work; that does not immediately mean Python is absent. You can also check by opening IDLE from the Start menu.

Why check the version? More than one Python version may be installed. For example, `python` may launch one version, while `py -3.13` may launch the 3.13 series specifically. Later, packages, libraries, and some syntax features may depend on the version.

### Installation and configuration are not the same thing

**Installation** means placing the required program files on the computer. **Configuration** means determining how the program starts, which interpreter is used, and how the environment is set up. No complicated configuration is required in this beginner lesson; first, students only need to launch the installed Python correctly, open IDLE, and learn to save a file.

If several Python versions are installed on students' computers, the results of `python --version`, `py --version`, or `py -3.13 --version` may differ. The important skill is identifying which interpreter is running, rather than repeatedly reinstalling Python without checking.

## 2. Python, IDLE, and the code window are not the same thing

Beginners often treat three concepts as if they were one: the Python language, the Python interpreter, and IDLE. They are related, but their roles differ.

**Python** is a programming language in which program text is written.  
**Python interpreter** is the software that reads and executes Python code.  
**IDLE** is a simple integrated development environment that comes with Python. It combines an Editor for writing code, a Shell for executing commands directly, and some inspection and debugging tools.

IDLE is not the only way to write Python. Students may later use VS Code, PyCharm, or other editors. However, IDLE is convenient for beginners: it usually requires no complicated separate setup and is installed with Python.

When IDLE opens, a **Python Shell** window, often with a dark or light background, usually appears. It contains the `>>>` prompt. This means Python is waiting for an interactive command. Students do not type the prompt themselves. When the cursor is after `>>>`, a short expression such as `2 + 3` can be entered; pressing Enter immediately displays the result.

However, when writing a program with several lines that must be saved, instead of simply entering everything into the Shell, open a separate **Editor** window using **File → New File**. It is useful to distinguish the purposes of these two windows from the beginning:

- **Shell:** test short commands, see results quickly, and run small experiments.
- **Editor:** write, save, modify, and run program text again later.

The Shell is not bad or incorrect; it is very useful. What matters is that students can tell when they are performing a temporary experiment and when they are writing a `.py` program that needs to be saved.

## 3. IDLE windows and how they differ

### Shell window

The Shell usually opens when Python starts. It executes the expression or command entered by the user and displays the result. For example:

```pycon
>>> 2 + 3
5

>>> print("Hello")
Hello
```

Commands and their results appear interactively in the Shell. However, do not assume that commands in Shell history have automatically been saved as a `.py` file. Lines entered in the Shell are not managed like a normal Editor file. If you need to reuse them later, copy them into an Editor file or write them in the Editor from the start.

### Editor window

The Editor is designed for writing and editing Python files. Open it through **File → New File**. Write code in the Editor and save it using `File → Save` or `Ctrl+S`; for example, name the file `hello_world.py`. The `.py` extension indicates that the file contains Python source code.

Run a saved Editor file through **Run → Run Module** or, usually, by pressing `F5`. If necessary, IDLE asks you to save the file and then executes it in the Shell. This shows students that the Editor is the source of the code, while the Shell is where the running program's output appears.

### Why save the file from the beginning?

If code exists only temporarily in the Shell, it may be difficult to reproduce the exact steps after the computer is shut down or the Shell is restarted. A `.py` file is saved on disk. It can be reopened, edited, sent to someone else, and added to a GitHub repository. Therefore, throughout the course, we will save code examples for each lesson in the `examples/dayXX/` folder.

## 4. What are the IDLE menus for?

The menus in IDLE vary depending on which window is active. On Windows and Linux, the Shell and Editor have their own menus. Therefore, a menu item seen in one window may not appear in exactly the same place in the other. The goal is not to make students memorise menu names, but to understand what they do. The official IDLE documentation describes each menu in detail: <https://docs.python.org/3/library/idle.html>.

### File

This menu manages file- and window-related actions.

- **New File:** opens a new, empty Editor window. We use this to write the first program.
- **Open:** opens an existing file from disk.
- **Open Module:** helps locate a module on Python's search paths. It is not necessary to use this every day at the beginner stage.
- **Recent Files:** lists recently opened files.
- **Save:** saves the current file.
- **Save As:** saves the file under another name or in another location. Useful when naming a new program.
- **Close / Exit:** closes the current window or IDLE. Do not ignore a prompt to save if there are unsaved changes.

The exact placement of menu commands may vary slightly between IDLE versions.

### Edit

This menu is used to edit text.

- **Undo / Redo:** undo or restore the most recent edit.
- **Cut / Copy / Paste:** cut, copy, and paste text.
- **Select All:** select all text in the window.
- **Find / Find Again:** search for a word or character in the text.
- **Replace:** replace found text with other text.
- **Go to Line:** move to a particular line in the file.

For beginners, the most useful commands are Undo, Copy, Paste, Find, and Select All.

### Shell — only in the Shell window

The Shell menu controls the interactive environment.

- **View Last Restart:** helps locate the point where the Shell was last restarted.
- **Restart Shell:** restarts the interactive environment; the previous Shell state and variables may be lost.
- **Previous History / Next History:** move through previously entered commands.
- **Interrupt Execution:** attempts to stop a command that is taking too long or is not responding.

Restart Shell does not uninstall Python from the computer; it only resets the current interactive session.

### Debug — mainly for investigating errors

Tools in the Debug menu help determine why a program is not producing the expected result.

- **Debugger (toggle):** enables or disables running the program through the debugger.
- **Stack Viewer:** helps display the sequence of calls at the time of an error.
- **Auto-open Stack Viewer:** controls whether Stack Viewer opens automatically for certain exceptions.
- **Go to File/Line:** helps navigate to the file and line shown in an error message.

Students do not need to use all these tools in the first lesson. For now, Debug simply shows that tools exist for investigating errors rather than blindly rewriting code. We will return to the debugger later.

### Options

The Options menu configures IDLE's appearance and preferences. Under **Configure IDLE**, you can change the font size, colours, keyboard shortcuts, startup window, some editing settings, and additional help sources. Display settings such as showing line numbers may also be available in the Editor.

There is no need to change every setting. It is enough for students to know how to increase the font size if the text is too small and make code comfortable to read.

### Window

This menu helps switch between open Shell and Editor windows. If several `.py` files are open, you can quickly return to the required window. To understand this menu, simply open the Shell and Editor at the same time.

### Help

The Help menu provides access to help and documentation.

- **About IDLE:** information about IDLE and its version.
- **IDLE Help:** documentation about IDLE windows, menus, and usage.
- **Python Docs:** opens the official Python documentation; depending on the configuration, it may open a local copy or documentation in a browser.
- **Turtle Demo:** opens examples based on Python's `turtle` module. These may be useful for interesting graphical examples later in the course.

### Format and Run menus that may appear in the Editor

Students may see additional **Format** and **Run** menus in the Editor window. This is normal.

**Format** helps manage code-block indentation, comment out or uncomment selected lines, and perform some formatting tasks. This menu becomes useful later when Python indentation is important.

The **Run** menu is used to execute and check the file in the Editor.

- **Run Module:** checks the current program file, saves it if necessary, and executes it in the Shell.
- **Check Module:** helps detect certain syntax problems before running the file.
- **Python Shell:** opens the Shell window or brings it to the front.

The main habit for the first lessons is: `File → New File`, write code, save it as `.py`, and run it with `Run → Run Module` or `F5`.

## 5. The first program — Hello World!

Open a new Editor window and write:

```python
print("Hello World!")
```

Save the file as `hello_world.py` and press `F5`. The result appears in the Shell as follows:

```text
Hello World!
```

At first, this may look like just one line of text. In fact, successful execution checks several things: Python starts, the code syntax is correct, the Editor can save the file, IDLE passes it for execution, and the result appears in the Shell.

### Why “Hello World!”?

This is a programming tradition that developed historically. In the early 1970s, Brian Kernighan used a simple example that printed a greeting in a guide to the B programming language. The example later became widely known through *The C Programming Language*, written with Dennis Ritchie. Many courses continue this tradition today. The syntax of Hello World differs between languages, but the goal is similar: write the simplest working program in the installed environment and demonstrate output.

The text does not have to be exactly `Hello World!`. `Hello, world!` or `Salom, dunyo!` works too. The important thing is that students understand the relationship between writing a program, running it, and seeing its result.

### What is `print`?

`print()` is a built-in Python function. It sends the textual representation of the given objects, by default, to the standard output stream, usually the Shell window. Write what you want to display inside the parentheses. A text value is called a string; a string is usually enclosed in a pair of double quotes (`"..."`) or single quotes (`'...'`).

```python
print("Hello World!")
print('Hello, world!')
print("We are learning the Python programming language.")
```

The quotation marks themselves usually do not appear in the output; they tell Python where the text literal begins and ends. If the text itself needs quotation marks, you can use the other kind of outer quote or escape characters, which will be covered later.

### Using commas and `+` with `print()`

Both can be used to display several pieces, but they do not do the same thing.

**Passing multiple arguments separated by commas:**

```python
print("Hello", "World!")
print("Age:", 18)
print("Result:", 2 + 3)
```

Each argument is passed to `print()` as a separate value. By default, one space is placed between arguments. The output is:

```text
Hello World!
Age: 18
Result: 5
```

This method lets you display a number together with text without manually converting the number to a string, because `print()` displays each supplied argument as text.

**Combining strings with `+`:**

```python
print("Hello" + "World!")
print("Hello" + " " + "World!")
print("Python " + "course")
```

Here, `+` joins strings. The first result is `HelloWorld!` because we did not add a space ourselves. The second result is `Hello World!`.

The most important difference is that a comma passes several separate arguments to `print()`, whereas `+` combines compatible values into one new value. Therefore:

```python
print("Age:", 18)       # works
# print("Age: " + 18)   # raises TypeError: str and int are incompatible
```

If you need to use `+`, you can convert the integer to text:

```python
print("Age: " + str(18))
```

For now, `str()` is introduced only briefly; we will study it in more detail in later lessons.

### `sep` and `end` — controlling `print()`

By default, `print()` uses a single space between arguments and a newline at the end of each call. These can be changed using `sep` and `end`, respectively.

```python
print("2026", "10", "24", sep="-")
print("Ali", "Vali", "Hasan", sep=" | ")

print("Hello", end=" ")
print("world!")
```

Output:

```text
2026-10-24
Ali | Vali | Hasan
Hello world!
```

`sep` defines what is placed between multiple arguments. `end` defines what is placed after the output finishes. These parameters are optional; if they are omitted, the default values are used. For now, it is enough to experiment with them.

### Simple and useful forms of `print()`

```python
print("First line")
print("Second line")

print()  # prints an empty line

print("2 + 3 =", 2 + 3)
print("A", "B", "C", sep=",")
```

Full documentation for Python's `print()`: <https://docs.python.org/3/library/functions.html#print>.

## 6. Comments — notes inside code

Code may be easy to understand at first, but as a program grows, it is easy to forget why a particular decision was made. A comment is a note written inside the code to help the programmer; it is not interpreted as an instruction for Python to execute.

In Python, an ordinary comment begins with `#`. Everything after that symbol to the end of the line is a comment.

### A comment on its own line

```python
# This program greets the user.
print("Hello!")
```

This form is useful for explaining a new topic, a complex idea, or the purpose of code. A comment does not make Python perform a new operation.

### A comment on the same line as code

```python
answer = 2 + 3  # calculate the sum in this simple example
print(answer)
```

A trailing comment works technically, but using too many of them can make code dense and harder to read. If the explanation is long, it is better to put it on a separate line.

### A comment spanning several lines

The usual way to comment out multiple lines in Python is to put `#` at the beginning of each line.

```python
# Before displaying the result,
# the program might calculate a variable.
# We will study variables in the next lesson.
```

This is sometimes called a “block comment,” but it is not a separate special multiline-comment syntax: it is a sequence of ordinary line comments.

### Triple quotes are not always comments

Sometimes you may see this:

```python
"""
The purpose of this module is to demonstrate print() examples.
This text serves as the module's docstring.
"""
```

A triple-quoted string is not a special form of ordinary Python comment. It is a multiline string literal. When placed in the appropriate position at the beginning of a module, function, or class, it serves as a **docstring** used for documentation. A docstring may later be displayed by tools such as `help()`. If a string is written casually just to replace `#` comments, it may remain a string literal that is evaluated in some circumstances.

Therefore, follow these beginner rules:

- Use `#` for ordinary explanations or temporary notes.
- Use a docstring in the appropriate place when documenting what a module, function, or class does.
- Do not describe triple quotes as “Python's multiline comment”; that is not technically accurate.

### What makes a good comment?

A comment should not merely repeat the code; it should explain necessary context.

```python
# Good: explains the reason.
# The result should appear to the user on a separate line.
print("Calculation complete")
```

The following comment is often unnecessary:

```python
# Call the print function
print("Hello")
```

For a new student, there is no need to insist that this comment is always bad. However, as experience grows, aim to explain why something was done rather than describing something already obvious from the code.

## 7. Common mistakes

**Code was entered in the wrong place, Shell instead of Editor, or vice versa.** Remember that Shell is for interactive commands and Editor is for files that need to be saved. If the code must be submitted as a `.py` file, save it from the Editor.

**The `>>>` prompt was included in the code.** Do not copy the Shell prompt into the Editor. In the Editor, write `print("Hello World!")`, not `>>> print(...)`.

**The file was saved as `.py.txt` instead of `.py`.** Windows may hide extensions. Check the file name and save location. Enabling the display of file extensions in File Explorer is useful.

**Changes were not saved.** Press `Ctrl+S` after modifying the code. IDLE may remind you to save, but you should check the save status yourself.

**Comma and `+` were treated as identical.** `print("A", "B")` puts a space between arguments; `"A" + "B"` joins the strings to produce `AB`.

**A number and a string were joined with `+`.** `"Age: " + 18` raises `TypeError` because one value is a string and the other is an integer. Use `print("Age:", 18)` or `print("Age: " + str(18))`.

**Comment syntax was written incorrectly.** An ordinary Python comment begins with `#`. `//`, used for comments in some other languages, is not Python's ordinary comment marker.

**Quotation marks were expected in the output.** `print("Hello")` displays `Hello`, not the quotation marks. Quotes mark the boundaries of a string in Python code.

**Python was installed multiple times.** Before reinstalling, check which interpreter is running with `python --version` or `py --version`. Multiple installations may exist, but there is no need to remove them without understanding the issue.

## 8. Review at the end of the lesson

Students should be able to answer these questions in their own words:

1. What is the difference between the Python programming language, the interpreter, and IDLE?
2. What does the `>>>` prompt shown when IDLE opens mean?
3. Why do we use `File → New File` for a program that needs to be saved?
4. How do you run a `.py` file written in the Editor?
5. What does the “Hello World!” program check, and why is it commonly used as the first example?
6. What is the difference between `print("A", "B")` and `print("A" + "B")`?
7. What are `sep` and `end` used for?
8. Why are comments useful, and which symbol begins an ordinary comment?
9. Why is it not entirely correct to call a triple-quoted string an ordinary comment?
10. How can you check whether Python is installed?

## Teacher's checklist

After the lesson, mark the parts that were actually covered. Do not automatically mark additional explanations in the plan as “covered” if there was not enough time to teach them.

- [ ] Demonstrated how to find and download an installer from Python.org.
- [ ] Explained the difference between installation and configuration.
- [ ] Explained the difference between Python, the interpreter, and IDLE.
- [ ] Demonstrated the difference between Shell and Editor.
- [ ] Explained the purpose of IDLE menus.
- [ ] Wrote and ran the `Hello World!` program.
- [ ] Demonstrated multiple `print()` arguments separated by commas.
- [ ] Demonstrated joining strings using `+`.
- [ ] Explained comments with examples.
- [ ] Explained the homework assignment.
