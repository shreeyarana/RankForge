from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from django.core.cache import cache
from time import time  
from api.rag.rag_pipeline import (
    rag_query
)

from rest_framework.views import APIView
from rest_framework.response import Response
from api.rag.build_index import (
    build_index
)

from api.services.analytics_service import (
    get_game_leaderboard
)

from api.services.analytics_service import (
    get_rolling_average
)

from api.services.analytics_service import (
    get_percentile_rank_analytics
)

from api.services.analytics_service import (
    get_daily_active_users
)

build_index()

class GameLeaderboardAnalytics(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response(
            get_game_leaderboard()
        )

class RollingAverageAnalytics(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        return Response(
            get_rolling_average()
        )


class PercentileRankAnalytics(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        return Response(
            get_percentile_rank_analytics()
        )

class DailyActiveUsersAnalytics(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response(
            get_daily_active_users()
        )

class RAGInsights(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(
        self,
        request
    ):

        query = request.data.get(
            "query"
        )

        answer = rag_query(
            query
        )

        return Response(
            {
                "answer": answer
            }
        )