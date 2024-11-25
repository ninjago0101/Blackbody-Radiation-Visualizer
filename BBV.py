import numpy as np
import matplotlib.pyplot as plt

def planck_law(wavelength, T):
    """
    Planck's law of blackbody radiation.
    Gives the spectral radiance as a function of wavelength and temperature.
    """
    h = 6.626e-34  # Planck constant 
    c = 3.0e8      # Speed of light 
    k = 1.38e-23   # Boltzmann constant 
    return (2 * h * c**2 / wavelength**5) / (np.exp(h * c / (wavelength * k * T)) - 1)

def wien_displacement(T):
    """
    Calculates the peak wavelength using Wien's law.
    """
    b = 2.897e-3  # Wien's  constant 
    return b / T

def stefan_boltzmann(T):
    """
    Calculates total radiated power using Stefan-Boltzmann law.
    """
    sigma = 5.67e-8  # S-B constant 
    return sigma * T**4

def plot_blackbody(temperatures):
    """
    Plots blackbody radiation curves for a given list of temperatures.
    Displays key trends like Wien's peak wavelength and total emitted power.
    """
    wavelengths = np.linspace(1e-9, 3e-6, 500)  # Wavelength range (1 nm to 3000 nm)

    plt.figure(figsize=(10, 8))
    for T in temperatures:
        intensity = planck_law(wavelengths, T)
        peak_wavelength = wien_displacement(T) * 1e9  # Convert to nm
        total_power = stefan_boltzmann(T)

        plt.plot(wavelengths * 1e9, intensity, label=f"T = {T} K\nPeak λ = {peak_wavelength:.1f} nm\nPower = {total_power:.2e} W/m²")

    plt.title("Interactive Blackbody Radiation Visualizer")
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Intensity")
    plt.legend(loc="upper right", fontsize=8)
    plt.grid()
    plt.show()

def main():
    """
    Main function to interactively take user input and plot blackbody radiation.
    """
    print("Blackbody Radiation Visualizer!")
    print("This tool plots radiation curves for objects.")
    try:
        n = int(input("numer of temperatures would you like to plot? "))
        temperatures = []
        for i in range(n):
            T = float(input(f"Enter temperature {i + 1} in Kelvin (e.g., 3000): "))
            temperatures.append(T)

        print("\nGenerating the plot... Please wait!")
        plot_blackbody(temperatures)

    except ValueError:
        print("Please enter numbers only.")

if __name__ == "__main__":
    main()
