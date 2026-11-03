# Restaurant Billing system 
# Problem Statement 41
# Name : Anant Belchandan 
# ERP : 02040
# Section : BCA AI/ML,1-A


def calculate_subtotal(order_list):
    return sum(item['amount'] for item in order_list)

def calculate_discount(subtotal):
    if subtotal > 500:
        return subtotal * 0.10
    return 0.0

def calculate_gst(amount_after_discount):
    return amount_after_discount * 0.05

def main():
    menu = {
        "Dosa": 80,
        "Idli": 40,
        "Thali": 150,
        "Tea": 20
    }
    
    order = []

    while True:
        # .strip().title() fixes accidental spaces and lowercase inputs (e.g., "dosa" becomes "Dosa")
        item_input = input("Order item: ").strip().title()
        
        if item_input == "Generate Bill":
            break
            
        if item_input not in menu:
            print("Item not on the menu. Available: Dosa, Idli, Thali, Tea")
            continue

        qty_input = input("Quantity: ").strip()
        
        try:
            quantity = int(qty_input)
            if quantity < 1:
                print("Quantity must be at least 1.")
                continue
        except ValueError:
            print("Invalid quantity. Enter a whole number.")
            continue

        amount = menu[item_input] * quantity
        order.append({
            "name": item_input,
            "quantity": quantity,
            "amount": amount
        })
        
        print(f"{item_input} x{quantity} added | Amount: {amount}")

    # Generate exact bill layout based on test cases
    if len(order) > 0:
        subtotal = calculate_subtotal(order)
        discount = calculate_discount(subtotal)
        amount_after_discount = subtotal - discount
        gst = calculate_gst(amount_after_discount)
        grand_total = amount_after_discount + gst

        # Matches Test Case 4 layout
        if len(order) > 1:
            item_strings = [f"{item['name']} x{item['quantity']} = {item['amount']}" for item in order]
            print(" | ".join(item_strings))
            
        if discount > 0:
            print(f"Subtotal: {int(subtotal)} | Discount (10%): {discount:.2f}")
            print(f"GST (5%): {gst:.2f}")
            print(f"Grand Total: {grand_total:.2f}")
        # Matches Test Case 2 layout
        else:
            print(f"Subtotal: {int(subtotal)} | Discount: 0.00")
            print(f"GST (5%): {gst:.2f} | Grand Total: {grand_total:.2f}")

if __name__ == "__main__":
    main()