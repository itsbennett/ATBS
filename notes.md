# Automate the Boring Stuff with Python
[Website](https://automatetheboringstuff.com)

[Video course](https://www.udemy.com/automate/learn/v4)

<!-- [Visualizer](https://pythontutor.com/) 
Depreciated -->

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

## Recap:
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

## Recap: 
  - Type programs into the file editor (you are now).
  - The execution statrs at the top and moves down.
  - `#` Comments are ignored by Python.
  - Functions are mini-programs in your program.
  - `print()` displays the value passed to it.
  - `input()` lets user type in a value.
  - `len()` takes a string value and returns an integer value of the string's length
  - `int()`, `str()`, and `float()` convert values' data type.

# Lecture 4
## Flow Charts and Basic Flow Concepts
- A flow chart diagram can be found in [this video](https://www.udemy.com/automate/learn/v4/t/lecture/3465802?start=0).
- Flow control statements are instructions that decides what Python instructions to execute under which conditions.
  - Yes/No options represented by:
    - **Boolean values**
    - **Comparison operators**
    - **Boolean operators**
- Boolean data types have two values: *true* or *false*.
- Boolean values can be stored in variables.
  - Ex: `varName = True`
    - Note: These values **must** be written as such: `True, False`. Any other way to stylize will not work, such as `TRUE`, `false`, or `'True'`.

- Comparison operators are used in expressions just like a plus or minus.
- There are six comparison operators:
  - `==` equal to
  - `!=` not equal to
  - `<` less than
  - `>` greater than
  - `<=` less than or equal to
  - `>=` greater than or equal to
- `42==42` will output the boolean value `True`.
- `42 == 'Hello` will output the boolean value `False`.
- When you have a variable assigned to a value, you can compare it to another value that will output a boolean.
  - Ex: `myAge = 26` and compared with `myAge < 30` will output `True`.
  - The value that the variable has assigned to it when used with a comparison operator must be the same value type. If an interger is compared to a string, regardless if it is the same, it will return `False` because the *string* is not an *interger*.
  - The exception to this rule is *float values* **can** be equal to an *interger*.
  - If one part of the expression is False, the entire expression will evaluate to `False`.

## The `and` Operator's Truth Table
- `True` and `True` evalutes to: `True`
- `True` and `False` evalutes to: `False`
- `False` and `True` evalutes to: `False`
- `False` and `False` evalutes to: `False`

- The `or` operator is essentially the exact opposite. 

## The `or` Operator's Truth Table
- `True` or `True` evalutes to: `True`
- `True` or `False` evalutes to: `True`
- `False` or `True` evalutes to: `True`
- `False` or `False` evalutes to: `False`

- The `not` operator evalutes to the opposite boolean value. It only operators on **one** boolean value.

## The `not` Operator's Truth Table
- `not True` evalutes to: `False`
- `not False` evalutes to: `True`

- Ex: 
`myAge = 26`
`myPet = 'cat'`
`myAge > 20 and myPet == 'cat'`
Output: `True`

## Recap: 
- Boolean data type: `True`, `False`.
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`.
- `==` is a *comparison*, `=` is an *assignment*.
- Boolean operators: `and`, `or`, `not`.

# Lecture 5
## Else, If, Elif Statements
- `if` Statements:
- Conditions and expressions are the same thing
- 