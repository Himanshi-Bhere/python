https://cdn.codewithmosh.com/image/upload/v1702942822/cheat-sheets/python.pdf
### Introduction to Python

**What is Python?**
Python is one of the most popular programming languages today, known for being powerful and relatively easy for beginners to learn.


**Why is Python used?**
It is highly versatile and used for a variety of tasks across many industries, including:
* **Automation:** Writing scripts to perform repetitive tasks quickly.
* **Artificial Intelligence (AI) and Machine Learning:** Building complex models that can make predictions or process data.
* **Web Development:** Creating applications and websites (popular sites like *Instagram* and *Dropbox* use Python).

### Variables
Variables are used to temporarily store data in a computer's memory. You can think of a variable as a labeled box where a specific piece of information is kept.

* **Definition:** You define a variable using an identifier (the name), followed by an equals sign, and then the value.
* **Example:** `price = 10`
* **Rules:** 
    * When Python executes this, it allocates memory to store the number 10 and attaches the label 'price' to that location.
    * When you want to use the value later, you simply call it by its name (without quotation marks, which are reserved for text strings).
    * Variable names should be descriptive and use underscores to separate words (e.g., `is_published`).
    * Python is **case-sensitive**, meaning `True` and `true` are not the same.

### Data Types
Python handles different types of values. The basic types mentioned include:

* **Integers:** Whole numbers without a decimal point (e.g., 10).
* **Floats (Floating point numbers):** Numbers that contain a decimal point (e.g., 2.9).
* **Strings:** Sequences of characters used for text (e.g., 'Mosh').
* **Booleans:** Logical values that represent `True` or `False`. They act like 'yes' or 'no' in programming.

### Receiving Input

To make programs interactive, you can capture input from the user.
* **The Input Function:** Using `input()` allows you to prompt the user for information.
* **Execution:** When the code hits an `input()` statement, it waits for the user to type something and press enter. The program then takes that value and proceeds.

* **Example:** `name = input("What is your name? ")`

* **Note:** The input received from the user is always treated as a **string** by default, even if they type a number. If you need to perform calculations with a number provided by the user, you must use **type conversion** (e.g., converting a string to an integer using `int()` or to a float using `float()`) before proceeding.
**input**
![[Pasted image 20260605170631.png]]

![[Pasted image 20260605170705.png]]


**data type**
![[Pasted image 20260605170839.png]]

![[Pasted image 20260605170805.png]]