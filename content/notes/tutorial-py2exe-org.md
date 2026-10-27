---
title: "Tutorial - py2exe.org"
date: '2013-02-11T19:43:30-03:00'
category: webclip
summary: 'py2exe packages Python programs for Windows computers that do not need Python installed. The tutorial walks through testing a script, writing setup.py, running py2exe, and handling Visual C runtime DLLs.'
tags: ["py2exe", "python", "windows", "distutils"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Tutorial - py2exe.org"
    url: "http://www.py2exe.org/index.cgi/Tutorial"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-02/py2exe-org--tutorial-py2exe-org.md"
    kind: repo
---

py2exe turns Python programs into packages that can run on other Windows computers without Python installed there. The tutorial assumes basic Python knowledge and explains the steps needed after installation, from testing the script to building and checking the output.

## Reading notes

- py2exe runs on a computer that already has Python, because it is itself a Python program and includes parts of Python in the package it builds.
- Before using py2exe, the program should already work; py2exe is not meant to fix a broken script.
- The tutorial’s sample program is a simple `print "Hello World!"` script that is tested from the command prompt first.
- py2exe extends Distutils with a new command, so the user writes a `setup.py` file and imports both `setup` and `py2exe`.
- The sample `setup.py` calls `setup(console=['hello.py'])` to define a single console application with `hello.py` as the entry point.
- Running `python setup.py py2exe` creates `build` and `dist` directories, with `build` used as working space and `dist` containing the files needed to run the application.
- The generated executable is tested from the `dist` directory to confirm that it runs correctly.
- The tutorial explains that the Microsoft Visual C runtime DLL may be needed, depending on the Python version and whether the user can redistribute that DLL.
- For Python 2.4 and 2.5, the DLL is MSVCR71.dll; for Python 2.6, 2.7, 3.0, and 3.1, the DLL is MSVCR90.dll.
- If redistribution is allowed, the runtime files can be bundled in a `Microsoft.VC90.CRT` subdirectory through `data_files` in `setup.py`.
- If redistribution is not allowed, users must install the appropriate Microsoft Visual C++ Redistributable Package themselves.
- py2exe is not an installer builder; it only assembles the files needed to run the program, so separate installer tools such as NSIS or Inno Setup may be used.
