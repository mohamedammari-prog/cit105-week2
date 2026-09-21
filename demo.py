from functions import (
    celsius_to_fahrenheit,
    line_total,
    initials,
    is_valid_url,
    truncate,
    safe_filename
)


print("Celsius to Fahrenheit:")
print(celsius_to_fahrenheit(25))

try:
    print(celsius_to_fahrenheit("hot"))
except TypeError as error:
    print("Rejected:", error)


print("\nLine Total:")
print(line_total(10.50, 3))

try:
    print(line_total(10.50, -2))
except ValueError as error:
    print("Rejected:", error)


print("\nInitials:")
print(initials("Luis De Leon"))
print(initials("  luis   de   leon  "))

try:
    print(initials(""))
except Exception as error:
    print("Rejected:", error)


print("\nValid URL:")
print(is_valid_url("https://example.com"))
print(is_valid_url("   "))


print("\nTruncate:")
print(truncate("This is a long sentence", 10))
print(truncate("Short", 10))


print("\nSafe Filename:")
print(safe_filename('My "Important" File/test.txt'))
print(safe_filename("homework file"))
