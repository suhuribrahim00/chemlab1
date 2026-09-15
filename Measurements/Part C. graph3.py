#This code produces a bar graph for the measurements lab
import matplotlib.pyplot as plt
import numpy as np

# Measurements
measurements = np.array([1, 2, 3])

# Mass of the penny in grams
mass = np.array([2.50, 2.51, 2.49])

# Diameter of the penny in centimeters
diameter = np.array([1.8, 1.8, 1.8])

# Height of the penny in centimeters
height = np.array([0.1, 0.1, 0.1])

# Calculate volume assuming a cylinder: V = pi * r^2 * h
radius = diameter / 2
volume = np.pi * radius**2 * height

# Calculate density for each measurement
density = mass / volume

# Calculate the average experimental density
average_density = np.mean(density)

# Calculate sample standard deviation for the error bars
standard_deviation = np.std(density, ddof=1)

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
    ecolor="black",
    capsize=8,
    capthick=2.5,
    elinewidth=2.5,
    zorder=5,
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

# Display density value above each bar
for bar, value in zip(bars, density):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + standard_deviation + 0.1,
        f"{value:.4f}",
        ha="center",
        va="bottom"
    )

# Axis labels
ax.set_xlabel("Measurement")
ax.set_ylabel("Density of penny (g/mL)")

# Title
ax.set_title("Experimental Density of a Penny")

# X-axis measurements
ax.set_xticks(measurements)

# Y-axis: start at 0.0, increase by 2.2
y_max = (average_density + standard_deviation) * 1.3
ax.set_ylim(0.0, y_max)
ax.set_yticks(np.arange(0.0, y_max + 0.01, 2.2))

# Horizontal gridlines
ax.grid(axis="y", alpha=0.25)

# Legend
ax.legend(loc="lower left")

# Make everything fit neatly
plt.tight_layout()

# Save the figure for the lab report
plt.savefig("penny_density_bar_graph.png", dpi=200)

# Display the graph
plt.show()

# Print calculated values
print("Individual densities:")

for i, d in zip(measurements, density):
    print(f"Measurement {i}: {d:.4f} g/mL")

print(f"\nVolume per trial (cylinder): {volume[0]:.4f} mL")
print(f"Average experimental density: {average_density:.4f} g/mL (reported as {average_density:.2f})")
print(f"Sample standard deviation (error bar): \u00b1{standard_deviation:.4f} g/mL (reported as \u00b1{standard_deviation:.2f})")
