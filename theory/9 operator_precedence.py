# De arriba hacia abajo

# ()
# **
# %, /, //, *
# +, -

expression = (9 - 7) * 2 ** 3 + 10 % 6 // -1 * 2 - 1

# Step 1: 2 * 2 ** 3 + 10 % 6 // -1 * 2
# Step 2: 2 * 8 + 10 % 6 // -1 * 2 - 1
# Step 3: 16 + -8 - 1
# Final: 7

print(expression)