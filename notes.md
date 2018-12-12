# Automate the Boring Stuff with Python
[Website](https://automatetheboringstuff.com)

[Video course](https://www.udemy.com/automate/learn/v4)

*This course doesn't focus on Computer Science subjects*

# Lecture 2
## Expressions, Data Types and Variables
- **Expressions** consist of **values** and **operators.** 
  - Expressions = Values + Operators
  - Ex: `2 + 2 = 4`

- Python follows the order of operations.
  - Ex: `2 + 3 * 6 = 20`
  - Ex: `(2 + 3) * 6 = 30`
  - A visualization tool can be found [here](https://automatetheboringstuff.com/eval/2-1.html)

- **Integers** are also called "*ints*" and **floating points** are called "*floats*".
  - Ex: 42 is an *interger* while *42.0* is a float.

- **Variables** hold values.
  - Ex: `spam = 42`
    - Typing `spam` will print 42.
    - Once your variable has been reassigned, it will take the value last given to it.
    - This is called **overwriting** the variable.

- If a Python instruction evaluates to a single value, it's an **expression**. Otherwise, it's a **statement**.

- Recap:
  - Expressions = Values + Operators
  - Int, Float, String
  - 'Hello World'
  - spam = 42
  - spam + 1

# Lecture 3
## Writing Our First Program
- The `#` in Python denotes a comment, which is ignored, as in, it is not executed. 
- Blank lines are completely ignored by Python.
  - This is useful for segmenting certain parts of programs.
- Values and arguments are the same thing and used interchangably. 
- `input()` waits for the user to give the variable a value. 
  - Ex: varName = `input()`
- The `(len(var))` function prints out the number of characters in a string.
- `str, int` and `float` return string, interger and floating data types respectively.
  - Ex: `str(26)` will make 26 a string data type.
  - To specifically specify it as an interger, you could type `int('26')` and it would then treat it as an interger.
  - Floating point values can be assigned using `float()`.
  - This is particularly useful when using `input()` as anything that is input by the user via this argument would be treated as a **string**.
  - If the desired outcome from `input()` is a string, the varName given must be written int(varName) to be treated as such, otherwise you will be given a syntax error.
  - Intergers cannot be added to strings, such as `27 + ' years old.'`. This will also return a syntax error.
  - An interactive demo of this is found [here](https://automatetheboringstuff.com/eval/3-4.html).

- Recap: 
  - Type programs into the file editor (you are now).
  - The execution statrs at the top and moves down.
  - `#` Comments are ignored by Python.
  - Functions are mini-programs in your program.
  - `print()` displays the value passed to it.
  - `input()` lets user type in a value.
  - `len()` takes a string value and returns an integer value of the string's length
  - `int()`, `str()`, and `float()` convert values' data type.