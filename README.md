# Galois Field Calculator

This script emulates a Galois Field Calculator for GF(2<sup>m</sup>) written in Python 2.7.13. This is a requirement for the subject CS 153: Introduction to Computer Security.

Reference: http://www.ee.unb.ca/cgi-bin/tervo/calc2.pl

### Features

- Input Validation. The format for the input must be entered as decimal coefficients separated by spaces.
- Computation of A(x) + B(x)
- Computation of A(x) - B(x)
- Computation of A(x) * B(x)
- Computation of A(x) / B(x)
- Detailed computation/ solution

# Instructions

### Installation

Clone the repository.

```
git clone https://github.com/ptsimon/CS153-Galois-Field-Calculator.git
```

### Run
Go to the cloned directory.

```
cd CS153-Galois-Field-Calculator
```

Execute the python script.

```
python GFcalculator.py
```

Note that Python is required to run this program.

# Example

The user will input A(x), B(x) and an irreducible polynomial P(x). The input polynomials would be entered as decimal coefficients separated by spaces. For example, x<sup>3</sup> + 7x + 6 would be entered as 1 0 7 6.

The user can then choose from these six:
1. A(x) + B(x) - Addition
2. A(x) - B(x) - Subtraction
3. A(x) * B(x) - Multiplication
4. A(x) / B(x) - Division
5. c  - Change the values of A(x), B(x), and P(x)
6. q  - Exit the program