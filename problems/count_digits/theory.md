# Theory: Counting Digits in an Integer

## Core Idea
The number of digits in an integer is not based on its value but on how many times it can be reduced by removing one digit at a time.

Digits are counted by repeatedly removing the last digit until no digits remain.

## Why Division by 10 Works
In base-10 numbers, dividing an integer by 10 and keeping only the whole-number part removes the rightmost digit.

Examples:
- 987 → 98
- 98 → 9
- 9 → 0

Each division removes exactly one digit.

## Loop Insight
A loop is used because the same action is repeated:
1. Count one digit.
2. Remove one digit.
3. Continue until the number becomes zero.

The loop must modify the number each iteration to eventually stop.

## Special Case: Zero
The number zero has one digit.
If zero is processed through the loop directly, it would produce a count of zero.
Therefore, zero must be handled explicitly.

## Handling Negative Numbers
The negative sign is not a digit.
Taking the absolute value of the number ensures only numeric digits are counted.

## Key Interview Takeaways
- Counting digits is about structure, not magnitude.
- Loops must always move toward termination.
- Zero is a common and important edge case.
- Understanding *why* division works matters more than memorizing code.
