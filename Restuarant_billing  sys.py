
print("--- Restaurant Billing System ---")
customer_name = input("Enter customer name: ")
bill_amount = input("Enter bill amount: ")

# Convert bill amount to float
bill_amount = int(bill_amount)

# Calculate tip (10% of bill amount)
tip = bill_amount /10

# Calculate GST (20% of bill amount)
gst = bill_amount /20

# Calculate total amount
total_amount = bill_amount + tip + gst

# Display the bill
print(f"""
    --- Bill Summary ---
      
    Customer Name: {customer_name}
    Bill Amount:   Rs.{bill_amount}
    Tip (10%):     Rs.{tip}
    GSt (20%):     RS.{gst}

------------------------------
    Total Amount: Rs.{total_amount}
""")
