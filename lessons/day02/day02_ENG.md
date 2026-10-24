# Day 02 — Number Systems, Digital Logic, and Computer Memory

**Level:** Beginner, with in-depth explanation  
**Core Topics:** Bit and byte, binary logic, transistor, SRAM/DRAM, number systems, conversion, floating-point numbers.

In this lesson, we begin with questions that are invisible in everyday life but crucial for a deeper understanding of programming: why do computers typically use the binary system? How are electric current and voltage interpreted as `0` or `1`? How is a bit stored in memory? Why can $1010_2$, $12_8$, $A_{16}$, and $10_{10}$ represent the exact same quantity despite different notations? Finally, why doesn't $0.1 + 0.2$ exactly equal $0.3$ in some programming languages?

The main idea of the lesson is this: **a number system is a method of writing a value; digital electronics is a method of reliably coding physical states as logical values.** These two concepts are interconnected, but they are not the same thing.

## 1. Why do we need number systems?

Imagine you have 27 books. You can write this quantity as $27$. In another number system, the same quantity is written differently: $11011_2$ in binary, $33_8$ in octal, $1B_{16}$ in hexadecimal. The notations are different, but the number of books remains unchanged.

Therefore, it is necessary to distinguish the **value** of a number from its **notation**. A number system is a set of rules for denoting and writing numbers. It helps express, compare, calculate quantities, and write data compactly.

Humans commonly use the decimal number system in everyday life. There are various historical reasons for this; a widespread explanation is that humans have ten fingers. But decimal is not the only possible system. We encounter base-60 in timekeeping, base-360 in ancient angle measurements, and binary and hexadecimal in computing.

The base of a number system determines how many different digit symbols we use and how the positional values increase. In the decimal system, the base is $10$; digits range from $0$ to $9$. In binary, the base is $2$; digits are only $0$ and $1$. Octal uses $0$–$7$, and hexadecimal uses $0$–$9$ and $A$–$F$.

General rule: **in a positional system with base $b$, every digit must be between $0$ and $b - 1$.** For example, $102_2$ is an invalid notation because there is no digit $2$ in binary. Similarly, $8_8$ is invalid because the digit $8$ is not used in octal.

## 2. Positional notation: Why does a digit's place matter?

Consider the number $583$ in decimal. It is not just three symbols. Its value is constructed as follows:

$$583 = 5 \times 10^2 + 8 \times 10^1 + 3 \times 10^0$$

Meaning:
- the left $5$ — five hundreds;
- the middle $8$ — eight tens;
- the right $3$ — three ones.

A digit's value is determined in conjunction with its position. This is the primary characteristic of a **positional number system**. The rightmost integer digit is multiplied by $b^0$, the one to its left by $b^1$, the next by $b^2$, and so on.

The exact same method applies to binary:

$$101101_2 = 1 \times 2^5 + 0 \times 2^4 + 1 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0$$
$$= 32 + 0 + 8 + 4 + 0 + 1 = 45_{10}$$

Here, $_2$ indicates the number is written in binary, and $_{10}$ in decimal. The subscript is used because the same notation like $101$ can have different values in different bases. For instance, $101_2 = 5_{10}$, but $101_3 = 10_{10}$.

General formula:

$$(d_n d_{n-1} \dots d_2 d_1 d_0)_b = d_n \times b^n + d_{n-1} \times b^{n-1} + \dots + d_1 \times b^1 + d_0 \times b^0$$

Here, $b$ is the base of the number system, and the $d$'s are valid digits in that system. The formula provides the most important rule of the number system: each digit is multiplied by the base raised to the power of its position, and the results are summed.

## 3. Why 0 and 1? Are there really 0s and 1s inside a computer?

To answer this clearly, we must separate two layers: the **physical device** and the **logical model**.

Electrical voltage in nature does not have only two values. It can take many intermediate values (e.g., $0.7$ V, $1.2$ V, or $2.8$ V). Such continuous or multi-valued physical quantities are considered analog. The physical behavior of a transistor is also more complex than a magical "on/off" switch: it controls current flow based on voltage.

However, digital electronics uses this physical behavior to separate many states into two logical classes. When designing an electronic circuit, a low voltage range is interpreted as a logical $0$, and a high voltage range as a logical $1$. Crucial point: **$0$ and $1$ are not the voltages themselves, but the logical meaning assigned to a voltage or other physical state.**

For example, for a specific circuit, $0$ might represent very low voltages, and $1$ sufficiently high voltages. But $0$ does not always mean exactly $0.000$ V, nor does $1$ always mean exactly $5.000$ V. Modern circuits do not necessarily operate at $5$ V; $3.3$ V or lower values are common. The exact thresholds depend on the electrical specifications of the device and logic family.

### Why not use every voltage as a distinct number?

Theoretically, a multi-valued system using multiple voltage levels can be built. There is even research on ternary (three-state) or other multi-valued logic. Thus, binary is not nature's only path.

However, a real electronic circuit is subject to noise, temperature fluctuations, manufacturing variances, wire resistance, cross-talk from other circuits, and signal degradation over time. If we assigned a distinct meaning to every small voltage difference, noise would likely alter the signal's meaning. Distinguishing between two widely separated states is generally much more reliable.

Having just one sharp threshold in a digital circuit is not enough either. For reliable operation, a low range guaranteed to be recognized as $0$ and a high range guaranteed to be recognized as $1$ are defined. The area between them might be indeterminate for some circuits; in normal operation, circuits should not fall into this ambiguous gap. The gap between output and input thresholds is called the **noise margin**.

### "Is all data just electrical current values?"

Part of this idea is true, but it needs refinement. Inside an electronic computer, data is represented by physical device states. Many digital circuits use voltages to represent signals, while memory elements use voltage and electrical charge. Other storage devices might store data via magnetic states, charge traps in flash memory, or other physical properties.

Therefore, saying all memory consists "only of electrical current values" is an oversimplification. A more accurate statement: **data itself is abstract; the hardware encodes it using physical states that can be stored and processed.** Concepts in a program like `True`, `False`, `45`, or `"Hello"` are represented in hardware through bits and various encodings.

## 4. The Transistor and the Digital Switch Concept

The transistor is one of the fundamental components of modern electronics. One of its functions is to control current flow using a controlling electrical signal. In digital circuits, transistors are often used as electronic switches: under certain conditions, they allow current to flow, and under others, they block it.

This can be compared to a wall light switch, but with limits. A mechanical switch is operated by hand; a transistor is controlled by a tiny electrical signal and can be packed in massive quantities inside a microchip.

Transistors allow the creation of logic gates — such as NOT, AND, OR. Logic gates perform operations on bits. By combining many gates, complex circuits are built that perform tasks like addition, comparison, value selection, memory management, and processor calculations.

## 5. Bit, Byte, and Data Encoding

**Bit** stands for binary digit. It represents one of two logical values: $0$ or $1$.

A single bit can represent two states. Two bits have four combinations: $00$, $01$, $10$, $11$. Three bits can represent $2^3 = 8$ combinations, and eight bits can represent $2^8 = 256$ combinations.

Generally, $n$ bits can form $2^n$ combinations. Therefore, 8 bits provide 256 possible patterns to encode a value. However, the meaning of these 256 patterns depends on the encoding used. For instance, they could be integers from 0 to 255, character codes, or other data.

A **Byte** typically consists of 8 bits. Thus:
- 1 bit — one of two states;
- 1 byte — 8 bits;
- 1 byte can represent 256 distinct bit patterns.

Important distinction: an eight-bit pattern is not automatically a "number" or a "letter". Its meaning depends on interpretation. For example, $01000001_2$ is equal to $65_{10}$ as a binary number; in ASCII encoding, it corresponds to the letter `A`.

## 6. SRAM and DRAM: How is a bit stored in memory?

Not all computer memory has the same structure. Two common types of random-access memory are **SRAM (Static RAM)** and **DRAM (Dynamic RAM)**. The main difference lies in how the bit is physically stored.

### SRAM — A state-retaining circuit

An SRAM cell typically stores a bit state using a bistable circuit called a latch, built from interconnected transistors. A common 6T SRAM cell uses six transistors. The feedback property of the circuit helps retain one of the states as long as power is supplied.

An SRAM cell requires more transistors than a DRAM cell, meaning fewer bits can fit into the same chip area. However, SRAM is usually very fast and is therefore widely used in processor caches and small, high-speed memories.

The word "Static" does not mean data is saved after the computer is turned off. SRAM is also **volatile**, meaning it loses data when power is removed. "Static" refers to its method of holding a bit while power is on, without needing periodic refreshing.

### DRAM — Storage via charge

A standard DRAM cell typically consists of one transistor and one capacitor. The capacitor stores electrical charge; the charge state is used to represent the bit value. 

The charge in the capacitor can leak over time. For this reason, the data in DRAM cells must be periodically updated — **refreshed**. DRAM has high density and requires relatively few elements to store one bit; this is why it is widely used as main RAM. However, refresh management is required, and DRAM is generally slower than SRAM.

### Brief Comparison of SRAM and DRAM

| Feature | SRAM | DRAM |
|---|---|---|
| Bit storage method | Latch built with transistors | Capacitor charge and access transistor |
| Refresh | Not required during normal operation | Periodic refresh required |
| Speed | Usually faster | Usually slower |
| Density | Larger cell, lower density | Smaller cell, higher density |
| Typical use | CPU cache and fast local memory | Main system memory (RAM) |
| On power loss | Data is lost | Data is lost |

## 7. Why is the binary system convenient for computers?

If memory and logic circuits can reliably distinguish two states, the binary number system is the natural choice to represent them. One bit signifies a $0$ or $1$ state. Multiple bits together can encode larger numbers, characters, instructions, or data structures.

Why is binary convenient? Because physically distinguishing two logical states, regenerating them through circuits, and making them noise-resilient is generally easier than differentiating multi-level states. It is a highly effective engineering choice in modern digital computers.

## 8. Binary, Octal, Decimal, and Hexadecimal Systems

| Number System | Base | Digits Used | Example |
|---|---:|---|---|
| Binary | 2 | $0, 1$ | $101101_2$ |
| Octal | 8 | $0$–$7$ | $55_8$ |
| Decimal | 10 | $0$–$9$ | $45_{10}$ |
| Hexadecimal | 16 | $0$–$9, A$–$F$ | $2D_{16}$ |

In hexadecimal, letters act as additional digits: $A = 10$, $B = 11$, $C = 12$, $D = 13$, $E = 14$, $F = 15$.

## 9. Converting from any base to decimal

Use the positional formula. Multiply each digit by the base raised to its positional power and sum the results.

### Example 1: Convert $110101_2$ to decimal

$$110101_2 = 1 \times 2^5 + 1 \times 2^4 + 0 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0$$
$$= 32 + 16 + 0 + 4 + 0 + 1 = 53_{10}$$

### Example 2: Convert $2D7_{16}$ to decimal

In Hex, $D = 13$:
$$2D7_{16} = 2 \times 16^2 + 13 \times 16^1 + 7 \times 16^0$$
$$= 2 \times 256 + 13 \times 16 + 7 = 727_{10}$$

## 10. Converting a decimal integer to another base: Division and remainder

To convert a decimal integer to another base, successively divide the number by the new base. Record the **remainder** at each step. Stop when the quotient is 0. Read the remainders from **bottom to top** (reverse order).

### Example: Convert $156_{10}$ to base 7

| Operation | Quotient | Remainder |
|---|---:|---:|
| $156 \div 7$ | 22 | 2 |
| $22 \div 7$ | 3 | 1 |
| $3 \div 7$ | 0 | 3 |

Read in reverse: $312_7$.

## 11. Converting between any two bases

To convert $243_5$ to base 3, use a two-step process:
1. Convert the source base to decimal ($243_5 = 73_{10}$).
2. Convert the decimal result to the target base ($73_{10} \div 3 \dots \rightarrow 2201_3$).

Result: **$243_5 = 2201_3$**.

## 12. Triads: Binary to Octal

The base of octal is $8$, and binary is $2$:
$$8 = 2^3$$
Thus, exactly three bits map to one octal digit. This 3-bit group is called a **triad**. Group bits from right to left in threes.

### Example
$1101011_2 \rightarrow 001\ 101\ 011_2 \rightarrow 153_8$

## 13. Tetrads: Binary to Hexadecimal

Hex base is $16$, binary is $2$:
$$16 = 2^4$$
Four bits map to one hex digit. This 4-bit group is a **tetrad** (or nibble). Group from right to left in fours.

### Example
$1101011011_2 \rightarrow 0011\ 0101\ 1011_2 \rightarrow 35B_{16}$

## 15. Fractional numbers in positional systems

Fractional bits represent negative powers of the base: $2^{-1} (0.5)$, $2^{-2} (0.25)$, $2^{-3} (0.125)$, etc.

$$101.101_2 = 4 + 0 + 1 + 0.5 + 0 + 0.125 = 5.625_{10}$$

## 16. Converting decimal fractions to binary

Multiply the fractional part by $2$. The integer part of the result becomes the next binary digit.

### Example: $0.625_{10}$ to binary
- $0.625 \times 2 = 1.25 \rightarrow 1$
- $0.25 \times 2 = 0.5 \rightarrow 0$
- $0.5 \times 2 = 1.0 \rightarrow 1$
Result: $0.101_2$

## 17. Why do some fractions repeat infinitely in binary?

If we convert $0.1_{10}$ to binary:
$$0.1 \times 2 = 0.2 \rightarrow 0$$
$$0.2 \times 2 = 0.4 \rightarrow 0$$
$$0.4 \times 2 = 0.8 \rightarrow 0$$
$$0.8 \times 2 = 1.6 \rightarrow 1$$
$$0.6 \times 2 = 1.2 \rightarrow 1$$
(fraction $0.2$ repeats).
$$0.1_{10} = 0.00011001100110011\dots_2$$
A binary fraction terminates only if its simplified denominator is a power of 2. 

## 18. Impact on Programming

Standard `float` types (like IEEE 754) store numbers with a limited number of bits. Thus, infinite binary fractions are truncated to the nearest representable value.

In Python:
```python
print(0.1 + 0.2) # 0.30000000000000004
```
### Practical Solutions
Use `math.isclose()` for comparisons, or use the `Decimal` module for exact arithmetic in finance.

```python
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3")) # True
```