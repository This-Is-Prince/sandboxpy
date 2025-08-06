players = ["Knight_Rider", "Lara_Croft", "Master_Chief"]

print("--- Player Rankings ---")
for index, player in enumerate(players):
    rank = index + 1
    print(f"Rank #{rank}: {player}")

players_with_scores = {"Knight_Rider": 30, "Lara_Croft": 230, "Master_Chief": 5234}

print("--- Player with Scores ---")
for player in players_with_scores:
    print(f"Player: {player}, Score: {players_with_scores[player]}")


print("\n--- Getting keys and values together ---")
for player, score in players_with_scores.items():
    print(f"Player: {player}, Score: {score}")
    if score > 100:
        break
    else:
        continue