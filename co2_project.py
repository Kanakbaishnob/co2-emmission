import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample data: Engine Size vs CO2 Emissions
# (This is illustrative data, real-world data would be more complex)
data = {
    'Engine_Size_L': [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0],
    'CO2_Emissions_g_km': [100, 102.4, 107, 109.3428, 111, 115, 118.76, 120, 140, 160, 180]
}

df = pd.DataFrame(data)

# Show first 7 rows
print("Data Preview:")
print(df.head(7))

# Step 3: Train a simple model
x = df[['Engine_Size_L']]  
y = df['CO2_Emissions_g_km'] 

# Create and train the model
model = LinearRegression()
model.fit(x, y)

# Take user input for engine size
try:
    engine_size = float(input("Enter the car's engine size in liters (e.g., 2.0): \n"))

    # Predict CO2 emissions for the given engine size
    predicted_emissions = model.predict([[engine_size]])

    # Print the predicted CO2 emissions with two different formats
    print(f"\nPredicted CO2 Emissions: {predicted_emissions[0]:,.2f} g/km")
    print(f"Predicted CO2 Emissions: {int(predicted_emissions[0])} g/km")

except ValueError:
    print("Invalid input. Please enter a numerical value for engine size.")
