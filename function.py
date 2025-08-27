def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Discount is applied only if discount_percent >= 20.
    
    :param price: float - original price of the item
    :param discount_percent: float - discount percentage
    :return: float - final price after discount (or original price if <20%)
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# --- Main program ---
# Prompt the user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Use the function to calculate final price
final_price = calculate_discount(price, discount_percent)

# Print result
if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount: {final_price:.2f}")
else:
    print(f"No discount applied. Final price: {final_price:.2f}")
