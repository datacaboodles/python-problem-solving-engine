# Problem: Count the Number of Digits in a Number

## Step 1: Input / Output / Data Types
- Input: a single integer
- Output: integer
- Data Types: int → int

## Step 2: Constraints & Assumptions
- Constraints: No specific constraints are mentioned.
- Assumptions: The input is a valid integer.

## Step 3: Decision Logic
- The number of digits is determined by repeatedly removing the last digit of the number and counting how many times this can be done until no digits remain.
- Each removal of a digit increases the count by one.
- Zero is treated as a single-digit number, and the negative sign is ignored while counting digits.

## Step 4: Edge Cases
- The input number is zero.
- The input number is a single-digit integer.
- The input number is a negative integer.

## Step 5: Sub-parts
- Accept the input number.
- Determine the total number of digits in the number.
- Display the digit count.

## Step 6: Pseudocode
- Receive the input number.
- Process the number to count how many digits it contains.
- Store the total digit count.
- Display the result.

## Step 7: Dry Run

Example 1:
Input: 23456  
Output: 5  

Example 2:
Input: 0  
Output: 1  

Example 3:
Input: -987  
Output: 3  

## Step 8: Python Code
(See solution.py)

## Step 9: Validation
- Input: 23456 → Output: 5
- Input: 0 → Output: 1
- Input: -987 → Output: 3
