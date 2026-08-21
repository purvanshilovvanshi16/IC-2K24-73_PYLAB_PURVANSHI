# LAB2 - Python Programs

This folder contains Python programs covering number problems, patterns, recursion/loops, menu-driven logic, and the number guessing game.

> **Note:** Replace the sample input/output marked as "Tested value" with the exact values you actually used while running each program before submitting.

---

## 1. Armstrong Number

### Aim
To check whether a given number is an Armstrong number.

### Logic
Take a number as input and separate its digits using arithmetic operations.
Raise each digit to the required power, add the results, and compare the sum with the original number.

### Sample Input / Output
**Tested value:** 153

**Output:**
```text
153 is an Armstrong number
```

---

## 2. Fibonacci Series

### Aim
To print the Fibonacci series for a given number of terms.

### Logic
Take the number of terms as input and start with 0 and 1.
Generate each next term by adding the previous two terms and continue until the required number of terms is printed.

### Sample Input / Output
**Tested value:** 10

**Output:**
```text
0 1 1 2 3 5 8 13 21 34
```

---

## 3. Menu-Driven Program Using Match Case

### Aim
To create a menu-driven Python application using `match-case` that performs the selected operation.

### Logic
Display a menu of available operations and take the user's choice.
Use `match-case` to execute the corresponding logic and continue displaying the menu until the user chooses to exit.

### Sample Input / Output
**Tested value:** Choice = 1

**Output:**
```text
Selected operation executed successfully.
```

---

## 4. Number Guessing Game

### Aim
To create a number guessing game in which the user guesses a randomly selected number within a limited number of attempts.

### Logic
Generate a random number within the specified range and repeatedly take guesses from the user.
After every guess, indicate whether it is too high or too low, and stop when the number is guessed correctly or the maximum attempts are reached.

### Sample Input / Output
**Tested value:** Target number = 50, Guess = 50

**Output:**
```text
Congratulations! You guessed the correct number.
```

---

## 5. Palindrome

### Aim
To check whether a given number is a palindrome using arithmetic operations.

### Logic
Reverse the number by extracting its digits one by one and constructing the reversed number.
Compare the reversed number with the original number to determine whether it is a palindrome.

### Sample Input / Output
**Tested value:** 121

**Output:**
```text
The number is a palindrome
```

---

## 6. Pattern

### Aim
To print a specified pattern using Python loops.

### Logic
Use nested loops to control the number of rows, spaces, and symbols printed in each row.
The outer loop controls the rows while the inner loops generate the required pattern.

### Sample Input / Output
**Tested value:** Number of rows = 5

**Output:**
```text
*
**
***
****
*****
```

---

## 7. Perfect Number

### Aim
To check whether a given number is a perfect number.

### Logic
Find the proper divisors of the input number and calculate their sum.
If the sum of the proper divisors is equal to the original number, the number is a perfect number.

### Sample Input / Output
**Tested value:** 28

**Output:**
```text
28 is a perfect number
```

---

## 8. Prime Number

### Aim
To check whether a given number is a prime number.

### Logic
Take a number as input and check whether it has any divisor other than 1 and itself.
If no such divisor exists, the number is prime; otherwise, it is not prime.

### Sample Input / Output
**Tested value:** 17

**Output:**
```text
17 is a prime number
```

---

## Files in This Folder

- `armstrong_num.py` - Armstrong number program
- `fibonacci_series.py` - Fibonacci series program
- `match_case.py` - Menu-driven program using match-case
- `num_guess.py` - Number guessing game
- `Palindrome.py` - Palindrome checking program
- `pattern.py` - Pattern printing program
- `Perfect_Number.py` - Perfect number program
- `Prime_Number.py` - Prime number program

### Submission Note

`tempCodeRunnerFile.py` and `tempCodeRunnerFile.python` are temporary files created by the editor and should normally **not be included in the GitHub submission**.
