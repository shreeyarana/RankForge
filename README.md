# RankForge ⚡  
### Scalable Leaderboard & Analytics Engine built with Django, PostgreSQL, and Redis

RankForge is a production-style ranking infrastructure designed to simulate real-world leaderboard systems at scale. It combines advanced SQL analytics, caching strategies, performance benchmarking, and CI automation to model how high-performance backend systems are engineered.

---

## 🚀 Tech Stack

- **Backend:** Django + Django REST Framework  
- **Database:** PostgreSQL  
- **Caching Layer:** Redis (Dockerized)  
- **Authentication:** Token-protected API endpoints  
- **CI/CD:** GitHub Actions  
- **Containerization:** Docker  
- **Testing:** Pytest / Django Test Framework  

---

## 🏗 Architecture Overview

Client → Django REST API → PostgreSQL  
                             ↘  
                             Redis Cache  

- PostgreSQL handles ranking logic and analytics.
- Redis caches leaderboard responses for low-latency retrieval.
- `EXPLAIN ANALYZE` is used to benchmark and validate query performance.
- CI pipeline validates tests and code integrity on every push.

---

## 📊 Core Features

### Advanced Leaderboard Analytics

Implemented using SQL window functions and ranking constructs:

- `RANK()` / `DENSE_RANK()`
- `PERCENT_RANK()`
- Rolling averages using window frames
- Position-based lookups
- Game-level ranking segmentation

---

## 📈 Analytics Modules

- **GameLeaderboardAnalytics**  
  Computes dynamic ranking per game.

- **RollingAverageAnalytics**  
  Time-based rolling performance metrics using window frames.

- **PercentileRankAnalytics**  
  Calculates relative user performance distribution.

- **DailyActiveUsersAnalytics (DAU)**  
  Computes distinct daily active users for engagement tracking.

---

## ⚡ Performance Engineering

- Query optimization using indexes
- Window-function-based ranking
- `EXPLAIN ANALYZE` benchmarking
- Redis caching for high-frequency leaderboard queries

---

## 🔐 Production-Level Practices

- Auth-protected API endpoints  
- Automated test coverage  
- GitHub Actions CI pipeline  
- Dockerized Redis setup  
- Clean Git history  

---

## 📊 Benchmarking Example
```sql
EXPLAIN ANALYZE
SELECT *
FROM leaderboard_scores
ORDER BY score DESC
LIMIT 10;
```

### Used to evaluate:

Query execution time

Index usage

Cost estimation

Sorting performance

## 🛠 Setup
1. Clone the repository
```bash   
git clone https://github.com/shreeyarana/RankForge.git
cd RankForge
```
2. Start Redis via Docker
```bash
docker run -p 6379:6379 redis
```
3. Configure PostgreSQL

Update .env with your database credentials.

4. Run migrations
```bash
python manage.py migrate
```

5. Start the server
```bash
python manage.py runserver
```
✅ Running Tests

pytest

## 🚀 Future Improvements
- Horizontal scaling simulation

- Sharded leaderboard model

- Real-time WebSocket updates

- Materialized view optimizations

- Rate limiting

- Observability (Prometheus/Grafana)

## 🎯 Project Objective
### RankForge demonstrates:

- Backend system design thinking

- Advanced SQL proficiency

- Data-driven ranking algorithms

- Caching strategies for scalability

- Performance optimization methodology

- Production-style engineering discipline

### This project models the type of ranking and analytics infrastructure used in gaming systems, competitive platforms, and engagement-driven applications.
