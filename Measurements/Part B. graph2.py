#This code produces a bar graph for the measurements lab
import matplotlib.pyplot as plt
import numpy as np

# Measurements
measurements = np.array([1, 2, 3, 4])

# Mass of water in grams (net mass, beaker already subtracted)
mass = np.array([9.20, 9.52, 9.44, 9.50])

# Volume of water in milliliters (measured via volumetric pipette)
volume = np.array([10.00, 10.00, 10.00, 10.00])

# Calculate density for each measurement
density = mass / volume

# Calculate the average experimental density
average_density = np.mean(density)

# Calculate sample standard deviation for the error bars
standard_deviation = np.std(density, ddof=1)

# True/reference density of water at 23 °C
true_density = 0.9976  # g/mL

# Create the bar graph
fig, ax = plt.subplots(figsize=(9, 6))

bars = ax.bar(
    measurements,
    density,
    width=0.65,
    label="Experimental density"
)

# Add error bars (±1 standard deviation)
ax.errorbar(
    measurements,
    density,
    yerr=standard_deviation,
    fmt="none",
    capsize=5,
    linewidth=1.5,
    label=f"Error bars (\u00b11 SD = {standard_deviation:.2f} g/mL)"
)

# Horizontal average density line
# NOTE: average is rounded to match the decimal place of the rounded SD,
# which is standard convention for reporting mean ± uncertainty
ax.axhline(
    average_density,
    linestyle="-",
    linewidth=2,
    label=f"Average density = {average_density:.2f} \u00b1 {standard_deviation:.2f} g/mL"
)

# Horizontal true/reference density line
ax.axhline(
    true_density,
    linestyle="--",
    linewidth=2,
    label=f"True density at 23 \u00b0C = {true_density:.4f} g/mL"
)

# Display density value above each bar
for bar, value in zip(bars, density):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + standard_deviation + 0.01,
        f"{value:.4f}",
        ha="center",
        va="bottom"
    )

# Axis labels
ax.set_xlabel("Measurement")
ax.set_ylabel("Density of water (g/mL)")

# Title
ax.set_title("Experimental Density of Water at 23 \u00b0C (Volumetric Pipette)")

# X-axis measurements
ax.set_xticks(measurements)

# Y-axis: start at 0.0 and increase by 0.2
ax.set_ylim(0.0, 1.08)
ax.set_yticks(np.arange(0.0, 1.01, 0.2))

# Horizontal gridlines
ax.grid(axis="y", alpha=0.25)

# Legend
ax.legend(loc="lower left")

# Make everything fit neatly
plt.tight_layout()

# Save the figure for the lab report
plt.savefig("water_density_23C_bar_graph.png", dpi=200)

# Display the graph
plt.show()

# Print calculated values
print("Individual densities:")

for i, d in zip(measurements, density):
    print(f"Measurement {i}: {d:.4f} g/mL")

print(f"\nAverage experimental density: {average_density:.4f} g/mL (reported as {average_density:.2f})")
print(f"Sample standard deviation (error bar): \u00b1{standard_deviation:.4f} g/mL (reported as \u00b1{standard_deviation:.2f})")
print(f"True density at 23 \u00b0C: {true_density:.4f} g/mL")
