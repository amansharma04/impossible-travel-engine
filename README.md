# 🛡️ Impossible Travel: Velocity-Based Fraud Detection
**A Python-based engine for identifying high-risk geographic anomalies in FinTech transactions.**

### 📊 Project Overview
In financial services, "Impossible Travel" occurs when two consecutive transactions are made from locations so far apart that the distance could not have been traveled in the time between them. This project simulates a transaction stream and uses a **Velocity-Based Heuristic** to flag potential account takeovers.

### 🧠 Logic & Features
* **Geospatial Analytics**: Calculates the distance and time delta between transaction points.
* **Velocity Thresholding**: Implements a rule-based engine where speeds > 600 MPH (10 miles/min) are flagged as `is_fraud = 1`.
* **Automated Visualization**: Generates a scatter plot highlighting legitimate vs. impossible travel patterns.

### 🛠️ Tech Stack
* **Python**: Core logic and object-oriented structure.
* **Pandas**: Data manipulation and feature engineering.
* **Matplotlib**: Data visualization for risk reporting.
* **NumPy**: Efficient conditional labeling and mathematical operations.

### 📈 Results
The engine successfully identified a fraudulent transaction involving a 4,000-mile jump from Chicago to Paris in under 15 minutes, as seen in the generated `travel_risk_chart.png`.

---
*Developed as part of my Data Engineering portfolio.*
