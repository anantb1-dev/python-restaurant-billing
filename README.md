# Restaurant Billing System

A console-based billing program written in Python 3 that calculates customer orders, applies conditional discounts, and adds GST. 

## Features
* Validates user input against a predefined menu dictionary.
* Calculates subtotal based on item quantities.
* Automatically applies a 10% discount if the subtotal strictly exceeds Rs. 500.
* Applies a 5% GST on the final discounted amount.
* Rejects invalid quantities and non-menu items without crashing.

## Prerequisites
* Python 3.x installed on your system.

## How to Run
1. Open your terminal or command prompt.
2. Navigate to the folder containing the script.
3. Run the following command:
   ```bash
   python billing.py
