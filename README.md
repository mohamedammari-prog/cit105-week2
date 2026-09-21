# CIT 105 Week 2 — Function Library

## Assignment 1: Function Library Exercise Set

This repository contains six Python functions that demonstrate reusable functions, return values, input validation, and docstrings.

## Functions

### 1. `celsius_to_fahrenheit(c)`

**Takes:** A Celsius temperature as a number.

**Returns:** The temperature converted to Fahrenheit.

**Rejects:** Non-numeric input with a `TypeError`.

---

### 2. `line_total(price, qty)`

**Takes:** A numeric price and a numeric quantity.

**Returns:** The price multiplied by the quantity.

**Rejects:** Non-numeric price or quantity and negative quantities.

---

### 3. `initials(full_name)`

**Takes:** A person's full name as a string.

**Returns:** The person's uppercase initials.

**Example:**

`"Luis De Leon"` returns `"LDL"`.

**Rejects/handles:** Extra spaces and an empty string.

---

### 4. `is_valid_url(text)`

**Takes:** A string containing a possible URL.

**Returns:** `True` for HTTP or HTTPS URLs and `False` for invalid input.

**Rejects/handles:** Empty strings and strings containing only spaces by returning `False`.

---

### 5. `truncate(text, limit=20)`

**Takes:** A string and an optional character limit.

**Returns:** The original text if it fits within the limit, or shortened text followed by an ellipsis if it is longer.

**Rejects:** Non-string text, non-integer limits, and negative limits.

---

### 6. `safe_filename(text)`

**Takes:** Arbitrary text.

**Returns:** Text formatted for use as a filename without spaces, slashes, or quotation marks.

**Rejects:** Non-string input.

## Demo

The `demo.py` file imports all six functions and demonstrates valid input and rejected/invalid input where appropriate.

The functions themselves do not print results. They return values, while `demo.py` is responsible for printing them.

## AI Disclosure

GitHub Copilot was used as permitted by the assignment to assist with the code. The final code was reviewed and tested by the student.
