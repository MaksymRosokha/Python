profit = 44500
tax = 0

if (profit >= 8000) and (profit <= 34500):
    tax = profit * 0.1
elif profit > 34500:
    tax = profit * 0.24

print(f"Tax for profit {profit} is {tax}")