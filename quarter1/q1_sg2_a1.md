# Annex 1
# Computational Thinking Exercise: "Smart School Canteen Queue"

## 19/Sofia Margaret M. Bengco
## 20/Angelica Mei S. Cara
## 21/Samantha Rose S. Deocampo
9 - Pinatubo
Aug 14, 2026

## Scenario
The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:

- Some students take too long to decide what to order.
- The cashier has to manually calculate totals and give change.
- There is no system to track which food items are running out.

Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

## Step 1: Identify the Big Problem
Main Problem: The school canteen has a slow and unorganized ordering system which causes long waiting time and long lines.

## Step 2: Identify three to four Sub-Problems
1. The cashier takes longer due to having to manually calculate money
2. The students and cashier will not know which food items are still in stock.
3. The line gets held up because of students cutting in line
4. Students are indecisive of their order, holding up the line once they get to the counter

## Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:
Sub-Problem:
1. Slow calculation
2. No real-time stock updates
3. Unoriganized lines
4. Indecision of students
Example Solution:
1. Algorithmic thinking - Add a calculator-like system where it can compute the prices
2. Data representation - A list/menu of all items available. A system that can mark whenever items are available or unavailable
3. Algorithmic thinking - Add queue numbers so everyone follows a sequence
4. Decomposition - Make the stock-list visible for students to preview before they approach the counter

## Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem
Pseudocode:
START
    INPUT price
    INPUT quantity
    INPUT payment

    total = price x quantity
    change = payment - total

    DISPLAY total
    DISPLAY change
END
