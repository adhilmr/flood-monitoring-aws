import random
import time
import winsound


# -----------------------------
# FLOOD THRESHOLDS
# -----------------------------

RAINFALL_WARNING = 60
RAINFALL_DANGER = 80

WATER_WARNING = 5
WATER_DANGER = 7


# -----------------------------
# GENERATE SENSOR DATA
# -----------------------------

def generate_sensor_data():
    rainfall = random.randint(0, 100)
    water_level = round(random.uniform(0, 10), 2)

    return rainfall, water_level


# -----------------------------
# ANALYZE FLOOD RISK
# -----------------------------

def check_flood_risk(rainfall, water_level):

    if rainfall >= RAINFALL_DANGER or water_level >= WATER_DANGER:
        return "CRITICAL"

    elif rainfall >= RAINFALL_WARNING or water_level >= WATER_WARNING:
        return "WARNING"

    else:
        return "NORMAL"


# -----------------------------
# DISPLAY RESULT
# -----------------------------

def display_result(rainfall, water_level, status):

    print("\n" + "=" * 50)
    print("          🌧️ FLOOD MONITORING SYSTEM")
    print("=" * 50)

    print(f"Rainfall      : {rainfall} mm")
    print(f"Water Level   : {water_level} m")
    print(f"Status        : {status}")

    if status == "CRITICAL":

        print("\n🚨🚨 FLOOD ALERT 🚨🚨")
        print("⚠️ IMMEDIATE ACTION REQUIRED")
        print("🔊 ALARM ACTIVATED")

        # Three short alarm sounds
        for i in range(3):
            winsound.Beep(1000, 500)

    elif status == "WARNING":

        print("\n⚠️ WARNING")
        print("Flood conditions are increasing.")

    else:

        print("\n✅ NORMAL")
        print("No immediate flood risk detected.")

    print("=" * 50)


# -----------------------------
# MAIN MONITORING LOOP
# -----------------------------

print("🌧️ Starting Flood Monitoring System...")
print("Monitoring sensors...\n")

while True:

    rainfall, water_level = generate_sensor_data()

    status = check_flood_risk(rainfall, water_level)

    display_result(rainfall, water_level, status)

    # Wait 5 seconds before next reading
    time.sleep(5)