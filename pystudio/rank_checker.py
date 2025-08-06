score = 85

if score >= 90:
    rank = "Gold"
elif score >= 80:
    rank = "Sliver"
elif score >= 70:
    rank = "Bronze"
else:
    rank = "No rank yet"

print(f"A score of {score} earns the rank: {rank}")