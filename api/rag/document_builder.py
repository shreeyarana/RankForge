# api/rag/document_builder.py

from api.services.analytics_service import (
    get_game_leaderboard,
    get_rolling_average,
    get_percentile_rank_analytics,
    get_daily_active_users,
)


def generate_documents():
    """
    Generate rich documents from existing analytics.
    These documents are later embedded and stored in FAISS.
    """

    leaderboard = get_game_leaderboard()
    rolling = get_rolling_average()
    percentiles = get_percentile_rank_analytics()
    daily_active = get_daily_active_users()

    documents = []

    # -----------------------------------------
    # Create lookup dictionaries
    # -----------------------------------------

    rolling_lookup = {}

    for row in rolling:
        key = (row["username"], row["game"])

        # Keep latest rolling average
        rolling_lookup[key] = row["rolling_avg"]

    percentile_lookup = {}

    for row in percentiles:
        key = (row["username"], row["game"])

        percentile_lookup[key] = row["percentile_rank"]

    # -----------------------------------------
    # Player Documents
    # -----------------------------------------

    for player in leaderboard:

        username = player["username"]
        game = player["game"]

        key = (username, game)

        rolling_avg = rolling_lookup.get(key, "N/A")

        percentile = percentile_lookup.get(key, "N/A")

        document = f"""
Player Name: {username}

Game: {game}

Current Rank: {player['rank']}

Total Score: {player['total_score']}

Rolling Average Score: {rolling_avg}

Percentile Rank: {percentile}
"""

        documents.append(
            {
                "type": "player",
                "username": username,
                "game": game,
                "content": document.strip(),
            }
        )

    # -----------------------------------------
    # Daily Active User Documents
    # -----------------------------------------

    for day in daily_active:

        document = f"""
Date: {day['day']}

Daily Active Users: {day['active_users']}
"""

        documents.append(
            {
                "type": "daily_activity",
                "day": str(day["day"]),
                "content": document.strip(),
            }
        )

    return documents