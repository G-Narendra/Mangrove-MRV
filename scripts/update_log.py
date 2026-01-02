from datetime import datetime
import random

ideas = [
    "Reviewed system design concepts",
    "Worked on problem-solving practice",
    "Improved project documentation",
    "Refactored small code components",
    "Learned something new about APIs",
    "Explored optimization techniques",
    "Reviewed GitHub projects for inspiration",
    "Improved code readability and structure"
]

today = datetime.now().strftime("%Y-%m-%d")
entry = f"## {today}\n- {random.choice(ideas)}\n\n"

with open("logs/daily-log.md", "a", encoding="utf-8") as f:
    f.write(entry)

print("Daily log updated.")
