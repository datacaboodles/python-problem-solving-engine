# Problem: Grade Classification

## Step 1: Input / Output / Data Types
- Input: a single integer score
- Output: string
- Data Types: int → str

## Step 2: Constraints & Assumptions
- Constraints: No specific constraints are mentioned.
- Assumptions: The input score is a valid integer.

## Step 3: Decision Logic
- If the score falls under the highest grade category, it is assigned that grade.
- If the score does not qualify for the highest grade but qualifies for the next lower grade category, it is assigned that grade.
- This evaluation continues in descending order across grade categories.
- Once the score matches a grade category, that grade is assigned.
- If the score does not qualify for any higher category, the lowest grade category is assigned.

## Step 4: Edge Cases
- The score is at the lowest possible boundary.
- The score is at the highest possible boundary.

## Step 5: Sub-parts
- Accept the score input.
- Assign the appropriate grade category.
- Display the assigned grade.

## Step 6: Pseudocode
- Receive the score as input.
- Evaluate the score against the grading categories.
- Assign the appropriate grade label.
- Display the final grade.

## Step 7: Dry Run

Example 1:  
Input: 25  
Output: Fail  

Example 2:  
Input: 90  
Output: A  

## Step 8: Python Code
(See solution.py)

## Step 9: Validation
- Input: 95 → Output: A
- Input: 80 → Output: B
- Input: 60 → Output: C
- Input: 3 → Output: Fail
