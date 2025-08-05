Lagrange Interpolation in Python

This project implements Lagrange Interpolation, a fundamental numerical method used to estimate unknown values between known data points using polynomials.

Features

Clean and beginner-friendly Python implementation
Custom input for any number of data points
Evaluates interpolated value at a desired x
Optional plotting of the interpolation curve using matplotlib

Files
lagrange_interpolation.py — Main script
README.md — Project documentation

How to Run
Clone the repository:
git clone https://github.com/your-username/lagrange-interpolation.git
cd lagrange-interpolation

Run the script:
python lagrange_interpolation.py

Input:
Number of data points
x and y values
x value to interpolate

How It Works
The program uses the Lagrange polynomial:
P(x) = Σ [ yᵢ × Lᵢ(x) ]
Lᵢ(x) = Π [ (x - xⱼ) / (xᵢ - xⱼ) ] for j ≠ i

Each Lᵢ(x) is a basis polynomial, ensuring the interpolation passes through all given points.

Example
Enter number of data points: 3  
Enter x values: 1 2 4  
Enter y values: 1 4 16  
Enter x to interpolate: 3  
Estimated value at x = 3 is: 9.0
Optional Visualization
Install matplotlib (if not already installed):

pip install matplotlib
Running with plotting enabled will display:
Original data points

Smooth interpolation curve

Applications
Reconstructing missing signal values
Estimating sensor data in control systems
Interpolating experimental data (e.g., in thermodynamics)
Useful in graphics, engineering, and more

Pros and Cons

Pros:
Simple and intuitive
Useful for small datasets

Cons:
Becomes unstable for large datasets
High-degree polynomials can oscillate (Runge’s phenomenon)

Author
Rohit Singh
School of Engineering, Kathmandu University
Feel free to fork, use, or contribute!
