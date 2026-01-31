# Problem: Sum of Digits

## Step 1: Input / Output / Data Types
- Input: an integer
- Output: integer
- Data Types: int → int

## Step 2: Constraints & Assumptions
- Constraints: No specific constraints mentioned.
- Assumptions: Input is a valid integer.

## Step 3: Decision Logic
- Each digit of the number is considered individually.
- The last digit is extracted and added to a running total.
- The number is reduced by removing the last digit.
- This process continues until no digits remain.
- Negative sign is ignored.

## Step 4: Edge Cases
- Input number is zero.
- Input number is a single-digit integer.
- Input number is negative.

## Step 5: Sub-parts
- Accept the input number.
- Extract and add each digit to a total.
- Display the final sum.

## Step 6: Pseudocode
- Receive the input number.
- Ignore the sign of the number.
- Extract digits one by one and add them to a total.
- Display the final sum.

## Step 7: Dry Run
Input: 234 → Output: 9  
Input: 9001 → Output: 10  
Input: -123 → Output: 6

## Step 8: Python Code
(See solution.py)

## Step 9: Validation
- Input: 234 → Output: 9
- Input: 9001 → Output: 10
- Input: -123 → Output: 6
- Input: 0 → Output: 0
