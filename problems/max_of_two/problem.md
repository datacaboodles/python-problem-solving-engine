# Problem: Maximum of Two Numbers

## Step 1: Input / Output / Data Types
- Input: two integers
- Output: integer (maximum value) or string ("Equal")
- Data Types: int → int or str

## Step 2: Constraints & Assumptions
- Constraints: No specific constraints are mentioned.
- Assumptions: Both inputs are valid integers.

## Step 3: Decision Logic
- If the first number is greater than the second number, the first number is the maximum.
- If the second number is greater than the first number, the second number is the maximum.
- If both numbers are equal, the output is "Equal".

## Step 4: Edge Cases
- One or both numbers can be zero.
- One or both numbers can be negative.

## Step 5: Sub-parts
- Accept two integer inputs.
- Compare the two numbers.
- Display the appropriate result.

## Step 6: Pseudocode
- Receive two integer numbers as input.
- Compare the two numbers.
- Determine the maximum value or equality.
- Display the result.

## Step 7: Dry Run

Example 1:
Input: 12, 2  
Output: 12

Example 2:
Input: 9, 12  
Output: 12

Example 3:
Input: 2, 2  
Output: "Equal"

## Step 8: Python Code
(See solution.py)

## Step 9: Validation
- Input: 2, 1 → Output: 2
- Input: 4, 5 → Output: 5
- Input: 2, 2 → Output: "Equal"
- Input: 2, 0 → Output: 2
- Input: -2, 3 → Output: 3
