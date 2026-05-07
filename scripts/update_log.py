from datetime import datetime
import random
import json
import os

STATE_FILE = "logs/activity-state.json"
LOG_FILE = "logs/daily-log.md"

ideas = [
    "Refined project documentation",
    "Improved algorithm understanding",
    "Reviewed system architecture notes",
    "Studied optimization techniques",
    "Reviewed ML evaluation metrics",
    "Read research papers",
    "Improved code structure",
    "Explored new tooling",
    "Updated learning notes",
    "Reviewed open-source implementations",
    "Tested data preprocessing pipeline",
    "Improved feature engineering approach",
    "Analyzed model performance",
    "Updated project architecture",
    "Reviewed API integration flow",
    "Optimized workflow execution",
    "Worked on deployment planning",
    "Explored cloud deployment options",
    "Improved logging system",
    "Studied satellite data processing"
]

# -------------------------
# CURRENT DATE/TIME
# -------------------------
now = datetime.now()
today = now.strftime("%Y-%m-%d")
current_hour = now.hour
weekday = now.weekday()  # 0 = Monday

# -------------------------
# LOAD STATE
# -------------------------
if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        state = json.load(f)
else:
    state = {}

# -------------------------
# RESET DAILY COUNTER
# -------------------------
if state.get("date") != today:

    # Weekday behavior
    if weekday < 5:
        daily_target = random.choices(
            [0,1,2,3,4,5,6,7,8],
            weights=[5,8,15,20,20,15,10,5,2]
        )[0]

    # Weekend behavior
    else:
        daily_target = random.choices(
            [0,1,2,3,4],
            weights=[35,30,20,10,5]
        )[0]

    state = {
        "date": today,
        "commits_today": 0,
        "daily_target": daily_target
    }

# -------------------------
# STOP IF TARGET REACHED
# -------------------------
if state["commits_today"] >= state["daily_target"]:
    print("Daily target already reached")

    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

    exit()

# -------------------------
# ACTIVE HOURS LOGIC
# -------------------------

# More human-like active hours
active_probability = {
    6: 20,
    7: 35,
    8: 55,
    9: 70,
    10: 80,
    11: 85,
    12: 75,
    13: 65,
    14: 70,
    15: 80,
    16: 85,
    17: 90,
    18: 85,
    19: 75,
    20: 65,
    21: 50,
    22: 35,
    23: 20
}

chance = active_probability.get(current_hour, 5)

roll = random.randint(1, 100)

if roll > chance:
    print("Skipping this hour naturally")

    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

    exit()

# -------------------------
# RANDOM HUMAN DELAY
# -------------------------
delay_seconds = random.randint(10, 180)

print(f"Human-like delay: {delay_seconds} seconds")

# -------------------------
# GENERATE LOG ENTRY
# -------------------------
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

entry = f"""## {timestamp}
- {random.choice(ideas)}

"""

with open(LOG_FILE, "a", encoding="utf-8") as f:
    f.write(entry)

# -------------------------
# UPDATE STATE
# -------------------------
state["commits_today"] += 1

with open(STATE_FILE, "w") as f:
    json.dump(state, f, indent=2)

print("Activity generated successfully")
