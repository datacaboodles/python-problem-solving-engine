# Reverse a Number — Theory

## Core Idea
Reversing a number means extracting digits from right to left and building a new number from left to right.

## Why Modulo 10 is Used
Modulo 10 gives the remainder after division by 10, which is always the last digit.
Example:
2345 % 10 → 5

## Why Division by 10 is Used
Dividing a number by 10 and ignoring the decimal part removes the last digit.
Example:
2345 // 10 → 234

## Why Multiplication by 10 is Used
Multiplying a number by 10 shifts its digits left, making space to attach a new digit at the end.
Example:
54 * 10 + 3 → 543

## Key Rule
Digit-based problems use:
- % 10 to extract a digit
- // 10 to remove a digit
- * 10 to build a new number

This pattern applies to reversing numbers, counting digits, and similar problems.
