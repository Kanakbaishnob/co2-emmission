

# 🚗 CO2 Emission Predictor

This is a simple Python project using **Pandas** and **Scikit-learn** to predict a car's CO2 emissions based on its engine size using a **Linear Regression** model.

## 📊 Overview

Given a dataset containing engine sizes (in liters) and corresponding CO2 emissions (in g/km), this program:

* Trains a linear regression model
* Takes user input for a car's engine size
* Predicts the corresponding CO2 emission
* Displays the prediction in a readable format

---

## 🧠 Technologies Used

* Python 🐍
* Pandas 📊
* Scikit-learn 🤖

---

## 🗂️ Project Structure

```
CO2_Predictor/
│
├── co2_predictor.py      # Main script
├── README.md             # This file
```

---

## ▶️ How to Run

1. **Clone or download** this repository.

2. **Install required packages** (if not already installed):

   ```bash
   pip install pandas scikit-learn
   ```

3. **Run the script**:

   ```bash
   python co2_predictor.py
   ```

4. **Enter engine size** (e.g., `2.0`) when prompted.

---

## 📝 Sample Output

```
Data Preview:
   Engine_Size_L  CO2_Emissions_g_km
0            1.0              100.0000
1            1.2              102.4000
2            1.4              107.0000
3            1.6              109.3428
4            1.8              111.0000
5            2.0              115.0000
6            2.2              118.7600

Enter the car's engine size in liters (e.g., 2.0): 
2.4

Predicted CO2 Emissions: 126.80 g/km
Predicted CO2 Emissions: 126 g/km
```

---

## ⚠️ Notes

* This model is trained on a small, illustrative dataset. Accuracy may not be reliable for real-world use.
* You can expand the dataset with real emission data for better predictions.

---

## 📌 Future Improvements

* Add data visualization using Matplotlib or Seaborn
* Include a GUI for ease of use
* Train with real-world datasets (e.g., from EPA or Kaggle)

---

## 📧 Contact

For suggestions or contributions, feel free to reach out!
kanak01537339244@gmail.com
---


