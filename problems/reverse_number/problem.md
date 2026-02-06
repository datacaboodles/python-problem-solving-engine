# Problem: Reverse a Number

## Step 1: Input / Output / Data Types
- Input: integer
- Output: integer
- Data Types: int → int

## Step 2: Constraints & Assumptions
- Constraints: No specific constraints are mentioned.
- Assumptions: The input is a valid integer.

## Step 3: Decision Logic
- The number is processed digit by digit starting from the last digit.
- Each extracted digit is added to a new number in reverse order.
- This process continues until all digits of the original number are processed.
- If the number is negative, the sign is preserved and applied to the final reversed number.

## Step 4: Edge Cases
- The input number is zero.
- The input number is a single-digit integer.
- The input number is a negative integer.

## Step 5: Sub-parts
- Accept the input number.
- Build a new number using the digits of the input.
- Display the final number.

## Step 6: Pseudocode
- Receive the input number.
- Initialize a variable to store the reversed number.
- Repeatedly update the reversed number using the input number.
- Update the input number to remove the processed part.
- Display the final reversed number.

## Step 7: Dry Run

### Example 1
Input: 2345  
Output: 5432

### Example 2
Input: -6709  
Output: 9076

## Step 8: Python Code
(See solution.py)

## Step 9: Validation
- Input: 2345 → Output: 5432
- Input: -6709 → Output: 9076
- Input: 0 → Output: 0
