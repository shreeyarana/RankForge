from django.urls import path
from .views import (
    GameLeaderboardAnalytics,
    RollingAverageAnalytics,
    PercentileRankAnalytics,
    DailyActiveUsersAnalytics
)

urlpatterns = [
    path("analytics/leaderboard/", GameLeaderboardAnalytics.as_view()),
    path("analytics/rolling/", RollingAverageAnalytics.as_view()),
    path("analytics/percentile/", PercentileRankAnalytics.as_view()),
    path("analytics/daily-active/", DailyActiveUsersAnalytics.as_view()),


]
