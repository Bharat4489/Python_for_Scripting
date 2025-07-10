def f(n):
    """Collatz function: even → n//2, odd → 3n+1."""
    return n // 2 if n % 2 == 0 else 3 * n + 1


# Test: apply f seven times to 674  → should be 190
x = 674
for _ in range(7):
    x = f(x)
print(x)          # 190

# Task: apply f fourteen times to 1071
y = 1071
for _ in range(14):
    y = f(y)
print(y)          # 3053
