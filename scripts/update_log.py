from datetime import datetime
import random
import time

ideas = [
    "Reviewed system design concepts",
    "Worked on algorithm optimization",
    "Improved project documentation",
    "Refactored utility functions",
    "Explored model evaluation techniques",
    "Reviewed research papers",
    "Improved code readability",
    "Experimented with small code changes",
    "Updated notes on AI concepts",
    "Checked open-source repositories"
]

today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for i in range(12):  # 🔥 12 commits per day
    entry = f"## {today}\n- {random.choice(ideas)} (update {i+1})\n\n"

    with open("logs/daily-log.md", "a", encoding="utf-8") as f:
        f.write(entry)

    # Small delay so commits look natural
    time.sleep(20)
