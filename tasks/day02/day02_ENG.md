# Day 02 — Number Systems and Number Representation in Computers

The goal of today's tasks is not simply to memorize formulas. Show each conversion step-by-step on paper and try to verify your answer using another method. When converting to decimal, write out the place values; when converting from decimal to another base, show each division and remainder step.

### Task 1 — Identify the Base

Determine which of the following notations are correctly written in the indicated base. If a notation is incorrect, explain why.

1. $101101_2$
2. $10201_2$
3. $728_8$
4. $7A_{16}$
5. $2G_{16}$
6. $1203_4$
7. $999_{10}$

### Task 2 — From Another Base to Decimal

Convert each number to decimal. Write the positional formula and show your intermediate calculations.

1. $101011_2$
2. $1110101_2$
3. $347_8$
4. $625_8$
5. $3A_{16}$
6. $2F4_{16}$
7. $132_4$
8. $243_5$

### Task 3 — From Decimal to Another Base

Convert the following decimal numbers to the indicated base. Write out the table of remainders and explain in one or two sentences why the remainders are read in reverse order.

1. $37_{10} \rightarrow ?_2$
2. $156_{10} \rightarrow ?_7$
3. $255_{10} \rightarrow ?_{16}$
4. $100_{10} \rightarrow ?_8$
5. $73_{10} \rightarrow ?_3$
6. $202_{10} \rightarrow ?_5$

### Task 4 — From One Base to Another

For each problem, first convert the source base to decimal, and then convert the decimal number to the target base. Finally, do a reverse check.

1. $243_5 \rightarrow ?_3$
2. $352_7 \rightarrow ?_4$
3. $7B_{16} \rightarrow ?_8$
4. $1101101_2 \rightarrow ?_5$

### Task 5 — Triad and Tetrad

Perform the following conversions using the grouping method, without doing any division.

1. $110101101_2 \rightarrow ?_8$
2. $1011110011_2 \rightarrow ?_{16}$
3. $724_8 \rightarrow ?_2$
4. $B3A_{16} \rightarrow ?_2$
5. $111010111101_2 \rightarrow ?_8$ and $?_{16}$

Show the groups clearly for each question. If necessary, pad the left side of the integer with zeros and explain why this does not change the value.

### Task 6 — Fractional Numbers

1. Convert $101.101_2$ to decimal.
2. Convert $110.011_2$ to decimal.
3. Convert $0.625_{10}$ to binary, showing each multiplication step.
4. Convert $13.625_{10}$ to binary.
5. Find at least the first 8 bits of the binary representation of $0.1_{10}$. Determine which part of the fraction starts repeating.
6. Explain why the binary representation of $1/10$ never terminates using the concept of a reduced fraction's denominator.

### Task 7 — Physics and Digital Logic

Answer the following questions in your own words.

1. If voltage can have multiple values, why does a digital circuit interpret it strictly as two logical states?
2. Why doesn't $0$ always mean exactly $0$ V, and $1$ exactly $5$ V?
3. What specific problem does a noise margin help to mitigate?
4. What is the fundamental physical difference between an SRAM cell and a DRAM cell?
5. Why is a DRAM refresh necessary?
6. What is meant by the statement: "$0$ and $1$ are not data themselves, but encoding values"?

### Task 8 — Checking with Python

Run the files `examples/day02/number_systems.py` and `examples/day02/base_conversion.py` in Python. Then independently try the following:

```python
print(bin(45))
print(oct(45))
print(hex(45))
print(int("101101", 2))
print(int("55", 8))
print(int("2D", 16))
```

Questions:
1. What purpose do the `bin()`, `oct()`, and `hex()` functions serve?
2. What does the second argument in `int("101101", 2)` represent?
3. Why does Python throw an error for `int("102", 2)`?
4. Choose 3 numbers of your own, represent them in two different bases, and verify that their values are identical.

### Task 9 — Floating-Point Experiment

Run the following code independently:

```python
from decimal import Decimal
from math import isclose

print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(format(0.1, ".20f"))
print((0.1).as_integer_ratio())
print(isclose(0.1 + 0.2, 0.3))
print(Decimal("0.1") + Decimal("0.2"))
```

Explain the results:
1. Which result differed from what you expected?
2. What does `as_integer_ratio()` show?
3. Why is the `math.isclose()` check different from `==`?
4. What is the difference between `Decimal("0.1")` and `Decimal(0.1)`?
5. Why is it more accurate to describe `float` as a format with "limited precision" rather than calling it "incorrect"?

### Challenge — Your Own Converter

Read the code in `examples/day02/base_conversion.py`. Then write a new program or expand the existing functions:
- Let the user input a number as text.
- Prompt for the source base and the target base.
- Have the program calculate the result.
- Output a clear error message if an invalid base or invalid digit is entered.
- Add support for negative integers.

**Bonus requirement:** Try to support bases from $2$ to $36$. In this range, the letters $A$ through $Z$ can represent values from $10$ to $35$.

### 📋 Submission Criteria
- Intermediate steps are shown for every manually solved conversion.
- Results are verified using at least one independent method.
- An explanation is provided regarding the reading order of digits in fractional conversions.
- Answers to SRAM/DRAM and digital logic questions contain logical reasoning.
- The Python experiment includes explanations of the causes behind the output, not just copy-pasted results.
