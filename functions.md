# 📘 Introduction to Functions in Python

Functions are one of the most important building blocks in Python. They help you organize your code, avoid repetition, and make it easier to understand.

---

## 🔧 What is a Function?

A **function** is a block of code that performs a specific task. Instead of writing the same code over and over, you can "call" the function whenever you need it.

Think of a function like a **recipe** – you follow the steps to get a result.

---

## 🛠️ Defining a Function

You define a function in Python using the `def` keyword:

```python
def say_hello():
    print("Hello!")
```

And then call it

```python
say_hello()
```

Output:
```
Hello!
```


## 🎯 Functions with Parameters
Functions can take parameters (inputs) to make them more flexible:

```python
def greet(name):
    print("Hello, " + name + "!")
```
Now call it with a name:

```python
greet("Alice")
```
Output:

```
Hello, Alice!
```
## 🔁 Functions That Return Values

Some functions return a value using the return keyword:

```python
def add(a, b):
    return a + b
```
You can store the result in a variable:

```python
result = add(3, 5)
print(result)
```
Output:
```
8
```


## 🔁 Function comments

Functions can have comments that describe what they do

```python
def add(a, b):
    """This function adds two numbers together """
    return a + b
```

This does not change what the function does.


