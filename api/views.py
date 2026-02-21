from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from django.core.cache import cache
from time import time  


class GameLeaderboardAnalytics(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        cache_key = "leaderboard_data"

        # 🔹 Check cache first
        cached_data = cache.get(cache_key)

        if cached_data:
            print("CACHE HIT")
            return Response(cached_data)

        print("CACHE MISS - Executing Query")

        start = time()
        query = """
        SELECT 
            u.username,
            s.game,
            SUM(s.score) AS total_score,
            DENSE_RANK() OVER (
                PARTITION BY s.game 
                ORDER BY SUM(s.score) DESC
            ) AS rank
        FROM scores_score s
        JOIN auth_user u ON s.user_id = u.id
        GROUP BY u.username, s.game
        ORDER BY s.game, rank;
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

        data = [
            {
                "username": row[0],
                "game": row[1],
                "total_score": row[2],
                "rank": row[3],
            }
            for row in rows
        ]

        cache.set(cache_key, data, timeout=60)

        print("Query time:", time() - start)

        return Response(data)

class RollingAverageAnalytics(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = """
        SELECT 
            u.username,
            s.game,
            s.score,
            s.date,
            ROUND(
                AVG(s.score) OVER (
                    PARTITION BY s.user_id
                    ORDER BY s.date
                    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
                ), 2
            ) AS rolling_avg
        FROM scores_score s
        JOIN auth_user u ON s.user_id = u.id
        ORDER BY u.username, s.date;
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

        data = [
            {
                "username": row[0],
                "game": row[1],
                "score": row[2],
                "date": row[3],
                "rolling_avg": row[4],
            }
            for row in rows
        ]

        return Response(data)


class PercentileRankAnalytics(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = """
        SELECT 
            u.username,
            s.game,
            SUM(s.score) AS total_score,
            ROUND(
                PERCENT_RANK() OVER (
                    PARTITION BY s.game
                    ORDER BY SUM(s.score)
                ), 2
            ) AS percentile_rank
        FROM scores_score s
        JOIN auth_user u ON s.user_id = u.id
        GROUP BY u.username, s.game
        ORDER BY s.game, percentile_rank;
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

        data = [
            {
                "username": row[0],
                "game": row[1],
                "total_score": row[2],
                "percentile_rank": row[3],
            }
            for row in rows
        ]

        return Response(data)

class DailyActiveUsersAnalytics(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = """
        SELECT 
            DATE(s.date) AS day,
            COUNT(DISTINCT s.user_id) AS active_users
        FROM scores_score s
        GROUP BY day
        ORDER BY day;
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

        data = [
            {
                "day": row[0],
                "active_users": row[1],
            }
            for row in rows
        ]

        return Response(data)
