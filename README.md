# Pi Day Programming Contest Template
This project implements a template you can use for the Pi day programming contest. It uses the [mpmath](https://mpmath.org/) library for arbitrary-precision arithmetic.
## Getting Started
 To get ready, do the following:
1. Fork this repository to your own Github account. (Make one if you don't have one!)
2. Clone the repository on your own computer using VSCode.
3. Create a virtual environment by running `python -m venv venv` in the terminal.
4. Activate the virtual environment with `source venv/bin/activate` in the terminal.
5. Install the required library with `pip install -r requirements.txt`.
## Contest Rules
1. Implement your algorithm in the `compute_pi` function. The only other modifications you make make to the code are to change the `mp.dps` parameter, which controls the number of digits the `mpmath` library uses.
2. Your algorithm can use addition/subtraction, multiplication/division, power/roots, logarithms, and integrals (using `mpmath`'s `quad` function). You may not use trigonometric or inverse trigonometric functions.
3. You may do research and set up your environment as per the above instructions before the contest, but you must implement and run your algorithm during the time set aside for the contest.
4. The winner will be decided based on the number of accurate digits reported by the `main` function.

