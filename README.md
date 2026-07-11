# RankForge ⚡

### Scalable Leaderboard, Analytics & Retrieval-Augmented Generation (RAG) Engine built with Django, PostgreSQL, Redis, FAISS, and Sentence Transformers

RankForge is a production-inspired backend system that simulates how large-scale gaming and competitive platforms manage leaderboards, analytics, caching, and AI-powered natural language querying. It combines advanced SQL analytics, Redis caching, semantic search using vector embeddings, and Retrieval-Augmented Generation (RAG) to deliver intelligent insights over player performance.

---

# 🚀 Tech Stack

### Backend
- Django
- Django REST Framework

### Database
- PostgreSQL

### Caching
- Redis
- django-redis

### Retrieval-Augmented Generation
- Sentence Transformers (`all-MiniLM-L6-v2`)
- FAISS Vector Database
- OpenAI API (LLM)
- Semantic Search

### DevOps
- Docker
- GitHub Actions

### Testing
- Pytest
- Django Test Framework

---

# 🏗 System Architecture

```
                    Client
                       │
                       ▼
               Django REST API
               ├──────────────┐
               │              │
               ▼              ▼
        PostgreSQL       Redis Cache
               │
               ▼
     Analytics Service Layer
               │
               ▼
        Document Generation
               │
               ▼
 Sentence Transformer Embeddings
               │
               ▼
          FAISS Vector Store
               │
               ▼
      Retrieval-Augmented Generation
               │
               ▼
        Natural Language Response
```

---

# 📊 Core Features

## Advanced SQL Analytics

Implemented using PostgreSQL Window Functions.

- Dense Ranking (`DENSE_RANK`)
- Percentile Ranking (`PERCENT_RANK`)
- Rolling Average Analytics
- Daily Active Users (DAU)
- Game-wise Leaderboards
- Position-based Ranking

---

## REST Analytics APIs

### Game Leaderboard Analytics
Returns ranked players for each game.

### Rolling Average Analytics
Computes rolling player performance using SQL window frames.

### Percentile Rank Analytics
Calculates each player's percentile within a game.

### Daily Active Users
Tracks unique daily users to measure platform engagement.

---

# 🤖 Retrieval-Augmented Generation (RAG)

RankForge includes a Retrieval-Augmented Generation pipeline that enables natural language querying over leaderboard analytics.

Instead of embedding raw database rows, the system converts analytics into structured semantic documents before indexing them.

### RAG Pipeline

```
Natural Language Query
          │
          ▼
Sentence Transformer
          │
          ▼
Query Embedding
          │
          ▼
FAISS Similarity Search
          │
          ▼
Relevant Analytics Documents
          │
          ▼
LLM Response
```

Example:

```
Who is the highest ranked player in Chess?
```

The system retrieves the most relevant leaderboard analytics before generating a natural language response.

---

# 🧠 Analytics Document Generation

Analytics documents are automatically generated from:

- Leaderboard Rankings
- Rolling Average Scores
- Percentile Rankings
- Daily Active User Metrics

Each player document includes:

- Username
- Game
- Current Rank
- Total Score
- Rolling Average
- Percentile Rank

These documents are embedded using Sentence Transformers and indexed in FAISS for semantic retrieval.

---

# ⚡ Performance Engineering

- PostgreSQL Window Functions
- Query Optimization
- Redis Caching
- FAISS Vector Indexing
- Semantic Similarity Search
- SQL Performance Benchmarking using `EXPLAIN ANALYZE`

---

# 🔐 Production Practices

- Token-Protected REST APIs
- Service Layer Architecture
- Environment Variable Configuration (`.env`)
- Redis-backed Cache Layer
- Modular RAG Components
- GitHub Actions CI
- Dockerized Redis
- Clean Git Workflow

---

# 📈 SQL Benchmarking

Example:

```sql
EXPLAIN ANALYZE
SELECT *
FROM leaderboard_scores
ORDER BY score DESC
LIMIT 10;
```

Used for evaluating:

- Query Execution Time
- Index Utilization
- Query Cost
- Sort Performance

---

# 📂 Project Structure

```
api/
│
├── rag/
│   ├── embeddings.py
│   ├── faiss_store.py
│   ├── document_builder.py
│   ├── retriever.py
│   ├── llm.py
│   ├── build_index.py
│   └── rag_pipeline.py
│
├── services/
│   └── analytics_service.py
│
├── views.py
└── urls.py
```

---

# 🛠 Setup

## Clone Repository

```bash
git clone https://github.com/shreeyarana/RankForge.git
cd RankForge
```

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment

Create a `.env` file:

```env
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

REDIS_HOST=127.0.0.1
REDIS_PORT=6379

OPENAI_API_KEY=
```

## Run Migrations

```bash
python manage.py migrate
```

## Start Redis

```bash
docker run -p 6379:6379 redis
```

## Start Server

```bash
python manage.py runserver
```

---

# ✅ Running Tests

```bash
pytest
```

---

# 🚀 Future Improvements

- Hybrid SQL + Vector Retrieval
- Local LLM Support (Ollama)
- Persistent FAISS Storage
- Streaming AI Responses
- Real-time Leaderboards using WebSockets
- Materialized View Optimizations
- Horizontal Scaling
- Prometheus & Grafana Monitoring

---

# 🎯 Project Highlights

- Built scalable leaderboard analytics using PostgreSQL Window Functions.
- Designed a modular service-layer architecture for reusable analytics.
- Integrated Redis caching to optimize high-frequency leaderboard queries.
- Implemented a Retrieval-Augmented Generation (RAG) pipeline using Sentence Transformers and FAISS.
- Generated semantic documents from computed analytics instead of raw database rows.
- Enabled natural language querying over leaderboard insights.
- Applied SQL performance benchmarking using `EXPLAIN ANALYZE`.
- Followed production-oriented engineering practices with Docker, GitHub Actions, and environment-based configuration.

---

### RankForge demonstrates modern backend engineering by combining traditional analytics with AI-powered semantic retrieval, mirroring the architecture of intelligent gaming, analytics, and engagement platforms.
