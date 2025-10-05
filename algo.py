# =========================================================
# PROGRAM: Arithmetic Operations (Signed & Unsigned)
# AUTHOR : <Your Name>
# DESCRIPTION:
#     Performs addition, subtraction (step-by-step),
#     multiplication & division (final answer only),
#     for signed and unsigned integers.
# =========================================================

# ------------------ ADDITION ----------------------------
def addition(a, b, signed=True):
    print("\n--- ADDITION ---")
    print(f"Adding {a} + {b}")
    result = a + b
    if signed:
        if result > 2147483647:
            result -= 4294967296
        elif result < -2147483648:
            result += 4294967296
    else:
        if result < 0:
            result = (result + 4294967296) % 4294967296
        elif result > 4294967295:
            result %= 4294967296
    print(f"Result = {result}")
    return result

# ------------------ SUBTRACTION -------------------------
def subtraction(a, b, signed=True):
    print("\n--- SUBTRACTION ---")
    print(f"Subtracting {a} - {b}")
    result = a - b
    if signed:
        if result > 2147483647:
            result -= 4294967296
        elif result < -2147483648:
            result += 4294967296
    else:
        if result < 0:
            result = (result + 4294967296) % 4294967296
    print(f"Result = {result}")
    return result

# ------------------ SEQUENTIAL MULTIPLICATION -----------
def sequential_multiplication(a, b, signed=True):
    neg_result = False
    if signed:
        if a < 0:
            a = -a
            neg_result = not neg_result
        if b < 0:
            b = -b
            neg_result = not neg_result
    result = a * b
    if signed and neg_result:
        result = -result
    print(f"\nSequential Multiplication: {result}")
    return result

# ------------------ BOOTH'S MULTIPLICATION --------------
def booths_multiplication(a, b):
    result = a * b  # simplified final answer
    print(f"Booth's Multiplication: {result}")
    return result

# ------------------ BIT MULTIPLICATION ------------------
def bit_multiplication(a, b):
    result = a * b  # simplified final answer
    print(f"Bit Multiplication: {result}")
    return result

# ------------------ BIT-PAIR MULTIPLICATION ------------
def bit_pair_multiplication(a, b):
    result = a * b  # simplified final answer
    print(f"Bit-Pair Multiplication: {result}")
    return result

# ------------------ RESTORING DIVISION ------------------
def restoring_division(a, b):
    quotient = a // b
    remainder = a % b
    print(f"Restoring Division: Quotient={quotient}, Remainder={remainder}")
    return quotient, remainder

# ------------------ NON-RESTORING DIVISION -------------
def non_restoring_division(a, b):
    quotient = a // b
    remainder = a % b
    print(f"Non-Restoring Division: Quotient={quotient}, Remainder={remainder}")
    return quotient, remainder

# ------------------ MAIN PROGRAM ------------------------
print("===================================================")
print("        ARITHMETIC OPERATIONS PROGRAM")
print("===================================================")

# Take user input
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

print("\n--- ADDITION & SUBTRACTION ---")
addition(a, b)
subtraction(a, b)

print("\n--- MULTIPLICATIONS (Final Answer) ---")
sequential_multiplication(a, b)
bit_multiplication(a, b)
bit_pair_multiplication(a, b)
booths_multiplication(a, b)

print("\n--- DIVISIONS (Final Answer) ---")
if b != 0:
    restoring_division(a, b)
    non_restoring_division(a, b)
else:
    print("Cannot divide by zero!")
