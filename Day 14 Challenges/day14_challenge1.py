players = [
    {"name": "A", "score": 45}, 
    {"name": "B", "score": 90}, 
    {"name": "C", "score": 75}
]
winner = players[0]
for player in players:
    if player["score"] > winner["score"]:
        winner = player
print(f"The winner is {winner['name']} with {winner['score']} points.")
