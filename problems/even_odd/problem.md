# Problem: Even or Odd

## Step 1: Input / Output / Data Types
- Input: a single integer
- Output: string
- Data Types: int → str

## Step 2: Constraints & Assumptions
- Constraints: No specific constraints are mentioned in the problem.
- Assumptions: The input will always be a valid integer.

## Step 3: Decision Logic
- A number is considered even if it can be divided by 2 without leaving any remainder.
- If dividing the number by 2 leaves no remainder, the output is "Even".
- If dividing the number by 2 leaves a remainder, the output is "Odd".

## Step 4: Edge Cases
- The input number is 0.
- The input number is a negative integer.

## Step 5: Sub-parts
- Accept the input number.
- Determine whether the number belongs to one category or the other.
- Display the appropriate result.

## Step 6: Pseudocode
- Receive an integer number as input.
- Decide whether the number belongs to the even category or the odd category.
- Store the result as a text value.
- Display the result.

## Step 7: Dry Run

### Example 1
Input: 4  
Output: "Even"

### Example 2
Input: 7  
Output: "Odd"

## Step 8: Python Code
(See solution.py)

## Step 9: Validation
- Input: 6 → Output: Even
- Input: 9 → Output: Odd
- Input: 0 → Output: Even
- Input: -2 → Output: Even
