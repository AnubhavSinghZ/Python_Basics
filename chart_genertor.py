import matplotlib.pyplot as plt
import pandas as pd

# Create a Dummy Data Set directly in the code 
data = {
    "Product": ["Laptops", " Smartphone", "Headphones", "Tablets", "Monitors"],
    "Units_sold": [120, 350, 480, 90, 150],
    "Revenue": [96000, 175000, 24000, 27000, 45000],
}

# Save this data as a CSV file to simulate reading an external file
df_initial=pd.DataFrame(data)
df_initial.too_csv("sales_data.csv", index=False)
print("Step 1: 'sales_data.csv' successfully created!")

# Load the CSV file
df=pd.read_csv("sales_data.csv")

# Create a bar chart : Product name on X Axix, units sold on Y Axis
plt.bar(df["Product"],df["Units_Sold"], color='skyblue', edgecolor='black')

# Add Title 
plt.title("Product Sales Performance", fontsize=14, fontweight="bold")
plt.xlabel("Product Categories", fontsize=12)
plt.ylabel("Units Sold", fontsize=12)
plt.grid(axos='y', linestyle='--', alpha=0.7)

# Display the chart 
print("Step 2: Dsiplaying the chart page")
plt.tight_layout()
plt.show()