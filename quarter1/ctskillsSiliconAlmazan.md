# Computational Thinking Exercise
## [Smart School Canteen Queue]
**Name:** Jahanna Kyla I. Almazan

**Section:** 9 - Silicon

**Last Name:** Almazan

**Date:** August 11, 2026

---

## Step 1: Identify the Big Problem
### Main Problem
The school canteen has long, slow queues during break time because ordering, paying, and serving are all done manually. This causes delay, confusion, and often leaves students with little time to actually eat.

---

## Step 2: Identify the Sub-Problems
1. Students often cannot see what food is available before reaching the counter.
2. Queue order is not followed fairly because of unclear lines and other students cutting them.
3. Manual computation of orders and payments takes too long and causes mistakes.
4. During food preparation, kitchen staff do not know how many servings to get ready ahead of time.

---

## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| Cannot see available food ahead | Abstraction | Show only today's menu with prices and availability on a simple display. |
| Unfair queue order | Pattern Recognition | Assign queue numbers automatically and serve in exact order. |
| Slow manual computation | Algorithm Design | Calculate total cost and change instantly once items are selected. |
| Uncertain amounts of serving | Decomposition | Count daily orders to predict how much food to prepare next time. |

---

## Step 4: Algorithmic Solution
### Selected Sub-Problem
Calculate total cost and payment process automatically.
### Pseudocode
START
Display menu with item names and prices
SET total_cost = 0
REPEAT
Ask student to select an item
Add item price to total_cost
Ask if they want another item
UNTIL no more items

Display total_cost
Ask for amount paid
Compute change = amount paid - total_cost
 
IF change >= 0 THEN
Display "Please pay: " + total_cost
Display "Change: " + change
Mark order as PAID
ELSE
Display "Insufficient amount. Please try again."
END IF
END

---
