# Theory: Sum of Digits (Interview Perspective)

## What does "Sum of Digits" mean?
The sum of digits of a number is obtained by separating each individual digit in the number and adding them together.

Example:
- 234 → 2 + 3 + 4 = 9
- 9001 → 9 + 0 + 0 + 1 = 10

The core challenge is not addition — it is **digit extraction**.

---

## Base-10 Representation (Key Concept)
All integers are represented in base-10.

Example:
234 = (2 × 100) + (3 × 10) + (4 × 1)

From this representation:
- The **last digit** of a number is obtained using remainder after division by 10.
- Removing the last digit is done using integer division by 10.

This concept is the foundation of digit-based problems.

---

## Why Modulo 10 Works
- Dividing a number by 10 gives a quotient and a remainder.
- The remainder always corresponds to the last digit.

Example:
- 234 % 10 → 4
- 23 % 10 → 3
- 2 % 10 → 2

Thus, modulo 10 extracts digits one by one from right to left.

---

## Why Integer Division by 10 Works
- Integer division removes the last digit of the number.

Example:
- 234 // 10 → 23
- 23 // 10 → 2
- 2 // 10 → 0 (loop stops)

This allows digit-by-digit traversal.

---

## Why a Loop is Required
Each digit must be processed once.
A loop ensures:
- One iteration per digit
- Controlled termination when all digits are consumed

Subtracting numbers (e.g., number = number - 1) does NOT work because it reduces value, not digit count.

---

## Handling Negative Numbers
The negative sign is not a digit.
Therefore, the absolute value of the number is taken before processing.

Example:
- -123 → digits are 1, 2, 3 → sum = 6

---

## Special Case: Zero
Zero is a valid integer and has exactly one digit.
The sum of digits of zero is zero.

The algorithm handles this naturally because:
- The loop does not run
- The sum remains zero

---

## Alternative Approach (String-Based)
Digits can also be processed by converting the number to a string and iterating over characters.

However:
- Mathematical approach is preferred in interviews
- String approach is acceptable in scripting or quick solutions

---

## Interview Takeaway
Digit-based problems test:
- Understanding of base-10 numbers
- Ability to break numbers systematically
- Control over loops and termination conditions

Clear reasoning is valued more than clever shortcuts.
