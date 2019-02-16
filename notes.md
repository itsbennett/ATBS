# Automate the Boring Stuff with Python
[Website](https://automatetheboringstuff.com)

[Video course](https://www.udemy.com/automate/learn/v4)

*Note: I think most of this is done in Python 3, as such, Python 2 syntax will likely not work.*

<!-- [Visualizer](https://pythontutor.com/) 
Depreciated -->

*This course doesn't focus on Computer Science subjects*

# Lecture 2
## Expressions, Data Types and Variables
- **Expressions** consist of **values** and **operators.** 
  - Expressions = Values + Operators
- Python follows the order of operations.

Example:
```python
  2 + 3 * 6
```
Output:
```
20
```
Where as:
```python
  (2 + 3) * 6
```
Output:
```
30
```       
  - A visualization tool can be found [here](https://automatetheboringstuff.com/eval/2-1.html)

- **Integers** are also called "*ints*" and **floating points** are called "*floats*".
  - Ex: 42 is an *interger* while *42.0* is a float.

- **Variables** hold values.
  ```python
  spam = 42
  spam
  ```
  Output:
  ```
  42
  ```
   - Typing `spam` will print 42.
    - Once your variable has been reassigned, it will take the value last given to it.
    - This is called **overwriting** the variable.
  ```python
  spam = 42
  spam + 1
  spam
  ```
  Output:
  ```
  43
  ```

- If a Python instruction evaluates to a single value, it's an **expression**. Otherwise, it's a **statement**.

## Recap:
  - Expressions = Values + Operators
  - Int, Float, String
  - `'Hello World'`
  - `spam = 42`
  - `spam + 1`

# Lecture 3
## Writing Our First Program
- The `#` in Python denotes a comment, which is ignored, as in, it is not executed. 
- Blank lines are completely ignored by Python.
  - This is useful for segmenting certain parts of programs.
- Values and arguments are the same thing and used interchangably. 
- `input()` waits for the user to give the variable a value. 
```python
varName = input()
```
- The `(len(var))` function prints out the number of characters in a string.
- `str, int` and `float` return string, interger and floating data types respectively.
  
  Example:
  ```python
  str(26)
  ```
  will make 26 a string data type.
  ```python
  int(26)
  ```
  will make 26 an interger.
  - Floating point values can be assigned using `float()`.
  - This is particularly useful when using `input()` as anything that is input by the user via this argument would be treated as a **string**.
  - If the desired outcome from `input()` is a string, the varName given must be written int(varName) to be treated as such, otherwise you will be given a syntax error.
  - Intergers cannot be added to strings, such as
  ```python 
  27 + ' years old.'. 
  ```
  This will also return a syntax error.
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

Example: 
```python 
myAge = 26
myPet = 'cat'
myAge > 20 and myPet == 'cat'
```
Output:
```
True
```

## Recap: 
- Boolean data type: `True`, `False`.
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`.
- `==` is a *comparison*, `=` is an *assignment*.
- Boolean operators: `and`, `or`, `not`.

# Lecture 5
## Else, If, Elif Statements
- `if` Statements:

```python
if name == 'Alice':
  print('Hi, Alice')
  print('Done')
```
Output:
``` 
Hi, Alice
Done
```
- If in the example *Alice* were another name, it would just print *Done*.
- Conditions and expressions are the same thing
- A block is made up of lines of code that are at the same level.
- Clauses and blocks are the same thing.

- `else` Statements:
- Code will run specifically when a condition is false using an `else` statement.
```python
password = 'swordfish'
if password == 'swordfish'
  print('Access granted.')
else: 
  print('Wrong password.')
  ```
  - If the condition is true, then the `if` block is executed and the `else` block is skipped.
  - Only **one** of the blocks will be executed.
  
  - `elif` statements
  ```python
name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an unded, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
  ```
  Output:
  ```
  Unlike you, Alice is not an undead, immortal vampire.
  ```
- An `else` statement can be appended to the end of an `elif` statement.

```python
print('Enter a name.')
name = input()
if name:
  print('Thank you for entering a name.')
else:
  print('You did not enter a name.')
```

- While this code works, you would want to write something more along the lines of:
```python
if name != '':
```
- For intergers, the value 0 is a **falsey** value, everything else is **truthy**.
- 0.0 for float is **falsey**, all others are **truthy**.

Falsey:
```python
bool(0)
bool('')
```
Output
```
False
```

Truthy:
```python
bool(42)
bool('Hello')
```

Output
```
True
```

## Recap
- An `if` statement can be used to conditionally execute code depending on whether the statement is True or False.
- An `elif` ("else if") statement can follow an `if` statement. Its block executes if its condition is True and all previous conditions have been False.
- An `else` statement comes **at the end**. Its block is executed if all of hte previous conditions have been False.
- The values 0, 0.0 and the empty string are considered to be Falsey values. When used in conditions they are considered False. You can always see for yourself which values are Truthy or Falsey by passing them to the `bool()` function.

# Lecture 6
## `while` Loops
- You can make a block of code execute over and over again so long as the condition(s) in the `while` statement are met.

```python
spam = 0
while spam < 5:
  print('Hello world!')
  spam = spam + 1 
```
Output:
```
Hello world!
Hello world!
Hello world!
Hello world!
Hello world!
```
- This outputs the way it does because `spam` is given a value of zero. The block
```python
print('Hello world!')
spam = spam + 1
```
- gets repeated until the `while` statement is no longer True. 
- Once `spam` is equal to `5`, the code ends and no more outputs are given.

```python
name =''
while name != 'your name':
  print('Please type your name.')
  name = input()
print('Thank you!')
```
- As long as the input given is not `your name`, it will continue to repeatedly ask for the input until the correct one is given.
- Loops are useful for having a user provide a valid kind of input for the data type you are trying to get. If you ask a user their age and they type in something that isn't numerical, a loop can force them to keep entering data until it satisfies the call.

- **Infinite Loops** can be quit using `ctrl+c`.