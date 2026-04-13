import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

df = pd.read_csv("smart_city_data.csv")

print("Dataset Preview:")
print(df.head())
print(os.listdir())



print("\nMissing Values:")
print(df.isnull().sum())

df = df.dropna()


df["Total Pollution"] = df["AQI"] + df["PM2.5"]

print("\nDataset with New Column:")
print(df.head())


print("\nAverage Traffic by Area:")
area_traffic = df.groupby("Area")["Traffic Volume"].mean()
print(area_traffic)

print("\nAverage Pollution by Area:")
area_pollution = df.groupby("Area")["Total Pollution"].mean()
print(area_pollution)

print("\nAverage Energy Usage by Area:")
area_energy = df.groupby("Area")["Energy (kWh)"].mean()
print(area_energy)

print("\nTop 5 High Traffic Records:")
print(df.sort_values(by="Traffic Volume", ascending=False).head())

colors = []
for a in area_traffic.index:
    if a == "Zone A":
        colors.append("red")
    elif a == "Zone B":
        colors.append("blue")
    elif a == "Zone C":
        colors.append("green")
    else:
        colors.append("gray")

plt.figure()
area_traffic.plot(kind="bar", color=colors)
plt.title("Area vs Traffic Volume")
plt.xlabel("Area")
plt.ylabel("Traffic Volume")
plt.show()

plt.figure()
plt.hist(df["AQI"], bins=5, color="orange", edgecolor="black")
plt.title("AQI Distribution")
plt.xlabel("AQI")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.scatter(df["Traffic Volume"], df["AQI"], color="purple")
plt.title("Traffic vs Pollution")
plt.xlabel("Traffic Volume")
plt.ylabel("AQI")
plt.show()

plt.figure()
area_energy.plot(kind="bar", color="cyan")
plt.title("Energy Usage by Area")
plt.xlabel("Area")
plt.ylabel("Energy (kWh)")
plt.show()

plt.figure()
corr = df.corr(numeric_only=True)
plt.imshow(corr)
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap")
plt.show()
print("\nSmart City Analysis Completed Successfully!") 