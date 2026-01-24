# Problem: Leap Year Check

## Step 1: Input / Output / Data Types
- Input: a single integer year
- Output: string
- Data Types: int → str

## Step 2: Constraints & Assumptions
- Constraints: No specific constraints are mentioned.
- Assumptions: The input is a valid integer year.

## Step 3: Decision Logic
- A year is generally considered a leap year if it can be divided by 4.
- However, if the year can be divided by 100, it is not considered a leap year.
- An exception to this rule is that if the year can also be divided by 400, it is considered a leap year.

## Step 4: Edge Cases
- The input year can be zero.
- The input year can be negative.

## Step 5: Sub-parts
- Accept the input year.
- Determine whether the year belongs to one category or the other.
- Display the corresponding result.

## Step 6: Pseudocode
- Take the input year.
- Decide which category the year belongs to.
- Assign the appropriate label.
- Display the result.

## Step 7: Dry Run

Example 1:
Input: 2020  
Output: "Leap Year"

Example 2:
Input: 1900  
Output: "Not Leap Year"

Example 3:
Input: 2000  
Output: "Leap Year"

## Step 8: Python Code
(See solution.py)

## Step 9: Validation
- Input: 2020 → Output: "Leap Year"
- Input: 1900 → Output: "Not Leap Year"
- Input: 2000 → Output: "Leap Year"
- Input: 2023 → Output: "Not Leap Year"
