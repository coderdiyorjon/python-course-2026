# IDLE quick reference

IDLE includes two main window types. Their menus are not identical, so first check which window is active.

## Shell window

The Shell is the interactive Python environment. The `>>>` prompt means Python is waiting for a command. It is suitable for short experiments.

- **File:** open files, review recent files, and close the window or application.
- **Edit:** undo, copy, paste, find, and select text.
- **Shell:** restart the interactive session, browse command history, or interrupt execution.
- **Debug:** enable the debugger and inspect information about exceptions.
- **Options:** configure fonts, colors, key bindings, and other preferences.
- **Window:** switch between open IDLE windows.
- **Help:** open IDLE Help, Python documentation, or About IDLE.

## Editor window

Use `File → New File` to open the editor. Write your Python program here and save it with a `.py` extension.

- **File:** create, open, save, and close source files.
- **Edit:** use the regular editing and search commands.
- **Format:** perform indentation and related code-formatting actions. The available commands depend on the IDLE version.
- **Run:** check and run the current module. `Run → Run Module` or `F5` is the standard beginner workflow.
- **Options:** adjust editor preferences, such as fonts and line numbers.
- **Window:** switch to the Shell or another open editor.
- **Help:** find IDLE and Python documentation.

## The standard beginner workflow

1. Open IDLE.
2. Select `File → New File`.
3. Write the program in the Editor window.
4. Save the file as `something.py`.
5. Press `F5` or select `Run → Run Module`.
6. Read the result in the Shell window.

Do not type the Shell prompt `>>>` into a `.py` source file. The prompt is part of the interactive interface, not part of Python program syntax.

Official reference: <https://docs.python.org/3/library/idle.html>
