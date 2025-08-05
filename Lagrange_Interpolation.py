import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Lagrange Interpolation Function
def lagrange_interpolation(x, y, xp):
    yp = 0
    n = len(x)
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p *= (xp - x[j]) / (x[i] - x[j])
        yp += p * y[i]
    return yp

# Manual Data Entry
def input_data_manually():
    n = int(input("Enter number of known data points: "))
    x = []
    y = []
    for i in range(n):
        xi = float(input(f"Enter x[{i+1}]: "))
        yi = float(input(f"Enter y[{i+1}]: "))
        x.append(xi)
        y.append(yi)
    return np.array(x), np.array(y)

# Excel Input
def input_data_from_excel(file_path):
    df = pd.read_excel(file_path)
    x = df.iloc[:, 0].values
    y = df.iloc[:, 1].values
    return x, y

# Main Program
def run_program():
    print("=== Lagrange Interpolation Tool ===")
    print("1. Enter data manually")
    print("2. Upload Excel file")
    choice = input("Choose input method (1 or 2): ")

    if choice == '1':
        x, y = input_data_manually()
    elif choice == '2':
        file_path = input("Enter Excel file path (e.g., data.xlsx): ")
        if not os.path.exists(file_path):
            print("\u274C File not found. Exiting.")
            return
        x, y = input_data_from_excel(file_path)
    else:
        print("\u274C Invalid choice.")
        return

    print("\n\u2705 Data Points:")
    for xi, yi in zip(x, y):
        print(f"  ({xi}, {yi})")

    xp = float(input("\nEnter x-value to interpolate (missing term): "))
    yp = lagrange_interpolation(x, y, xp)
    print(f"\nEstimated y at x = {xp}: {yp:.4f}")

    # Plotting
    x_vals = np.linspace(min(x)-5, max(x)+5, 500)
    y_vals = [lagrange_interpolation(x, y, val) for val in x_vals]

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='Interpolated Curve', color='blue')
    plt.scatter(x, y, color='red', label='Known Points')
    plt.scatter(xp, yp, color='green', label=f'Interpolated Point\n({xp}, {yp:.2f})')
    plt.xlabel('X axis (Independent Variable)')
    plt.ylabel('Y axis (Dependent Variable)')
    plt.title('Lagrange Interpolation')
    plt.legend()
    plt.grid(True)
    plt.show()
    

# Run the script
if __name__ == "__main__":
    run_program()
    

