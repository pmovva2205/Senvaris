import time
import random
import json


# Senvaris: Driver Behavior Monitoring System


# Thresholds for "unsafe" driving
THRESHOLDS = {
    "speed_kph": 120, # Above this = too fast
    "acceleration_mps2": 4.0, # Above this = harsh accel
    "brake_force": 7.0, # Above this = harsh brake
    "steering_angle_deg": 45 # Above this = harsh turn
}

# Function: generate random vehicle data
def generate_vehicle_data():
    return {
    "speed_kph": random.randint(0, 180),
    "acceleration_mps2": round(random.uniform(0, 6), 2),
    "brake_force": round(random.uniform(0, 10), 2),
    "steering_angle_deg": random.randint(0, 90)
}

# Function: check data against thresholds
def check_driving_behavior(data):
    alerts = []
    if data["speed_kph"] > THRESHOLDS["speed_kph"]:
        alerts.append(f"High speed: {data['speed_kph']} kph")
    if data["acceleration_mps2"] > THRESHOLDS["acceleration_mps2"]:
        alerts.append(f"Harsh acceleration: {data['acceleration_mps2']} m/s²")
    if data["brake_force"] > THRESHOLDS["brake_force"]:
        alerts.append(f"Harsh braking: {data['brake_force']}")
    if data["steering_angle_deg"] > THRESHOLDS["steering_angle_deg"]:
        alerts.append(f"Harsh cornering: {data['steering_angle_deg']}°")
    return alerts

# Function: run the system
def run():
    print("🚗 Starting Senvaris...")
    for _ in range(10): # Run 10 cycles
        data = generate_vehicle_data()
        alerts = check_driving_behavior(data)
        print("Data:", data)
        if alerts:
            print("⚠️ ALERTS:", "; ".join(alerts))
        else:
            print("✅ OK: Safe driving")
        time.sleep(1)

# Log to file
        with open("senvaris_log.jsonl", "a") as f:
            f.write(json.dumps({"data": data, "alerts": alerts}) + "\n")

# Run program
if __name__ == "__main__":
    run()
