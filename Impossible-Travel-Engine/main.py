import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =================================================================
# THE ENGINE CLASS 
# =================================================================
class TravelTracker:
    def __init__(self):
        # This is our 'Database' - a simple list of transactions
        self.raw_data = {
            'user_id': ['U1', 'U1', 'U2', 'U2', 'U3', 'U3', 'U4', 'U4'],
            'city': ['San Francisco', 'New York', 'Miami', 'Miami Beach', 'Chicago', 'Paris', 'Austin', 'Dallas'],
            'dist_miles': [0, 2500, 0, 5, 0, 4000, 0, 200], # Distance from last city
            'time_diff_min': [0, 30, 0, 60, 0, 15, 0, 180], # Minutes since last city
            'amount': [10, 500, 20, 15, 50, 2000, 30, 45]
        }

    def process_velocity(self):
        """Calculates the physical speed of the user's transactions."""
        df = pd.DataFrame(self.raw_data)
        
        # Logic: Speed = Distance / Time
        # We use .replace(0, np.nan) to avoid 'Division by Zero' errors (Engineering best practice)
        df['miles_per_min'] = df['dist_miles'] / df['time_diff_min'].replace(0, np.nan)
        
        # Logic: A commercial plane flies at ~9 miles per minute (540 mph).
        # If speed > 10 miles per minute, it is 'Impossible Travel'.
        df['is_fraud'] = np.where(df['miles_per_min'] > 10, 1, 0)
        return df

    def create_dashboard(self, df):
        """Visualizes the travel anomalies using Matplotlib."""
        plt.figure(figsize=(10, 6))
        
        # We split the data into 'Safe' and 'Fraud' for the chart colors
        safe = df[df['is_fraud'] == 0]
        fraud = df[df['is_fraud'] == 1]

        # Create the Scatter Plot
        plt.scatter(safe['time_diff_min'], safe['dist_miles'], color='blue', label='Normal Travel', s=100)
        plt.scatter(fraud['time_diff_min'], fraud['dist_miles'], color='red', label='Impossible Travel', s=200, marker='x')

        # Add labels so a manager can understand the chart
        plt.title('Fraud Detection: Physical Velocity Check')
        plt.xlabel('Minutes Between Transactions')
        plt.ylabel('Miles Traveled')
        plt.legend()
        
        # Add a 'Danger Zone' line (Engineering threshold)
        plt.plot([0, 400], [0, 4000], color='gray', linestyle='--', alpha=0.5) 
        
        plt.savefig('travel_risk_chart.png')
        print("📈 Visual Dashboard generated: travel_risk_chart.png")
        plt.show()

# =================================================================
# EXECUTION (The 'Main' Pipeline)
# =================================================================
if __name__ == "__main__":
    # 1. Initialize the Engine
    engine = TravelTracker()
    
    # 2. Run the math
    results_df = engine.process_velocity()
    
    # 3. Show the Table
    print("\n--- TRANSACTION VELOCITY REPORT ---")
    print(results_df[['user_id', 'city', 'miles_per_min', 'is_fraud']])
    
    # 4. Generate the Chart
    engine.create_dashboard(results_df)