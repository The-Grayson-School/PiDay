from mpmath import *

mp.dps = 50 # Set decimal preision, the maximum number of digits to compute.
# Increasing this will make your calculations take more time!

def main():
    # Do not modify this function!
    comp_pi = compute_pi()
    digits = round(-log10(abs(comp_pi - pi)))
    print(comp_pi)
    print(f'Your calculation is accurate to {digits} digits.')

def compute_pi():
    # Implement your algorithm here!
    return mpf('22/7') # A well-known approximation to pi.

if __name__ == '__main__':
    main()