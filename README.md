# 🌤️ Weather Pipeline - Automated Data Engineering Platform

An end-to-end automated weather data pipeline that collects, stores, and serves live weather data for major cities around the world.

## 📊 Architecture Visualization

```
[Weather API]  -->  [GitHub Actions]  -->  [Supabase]  -->  [FastAPI]  -->  [Vercel]  -->  [Browser]
   (live)            (every hour)          (PostgreSQL)     (API)         (host)         (JSON)
                                                
                    ┌─────────────────────────────────────────┐
                    │                                         │
                    ▼                                         │
              [GitHub Actions]                                │
              (scheduled trigger)                             │
                    │                                         │
                    ▼                                         │
              [Python Script]                                 │
              (fetch + transform)                             │
                    │                                         │
                    ▼                                         │
              [Supabase DB]                                   │
              (store records)                                 │
                    │                                         │
                    ▼                                         │
              [FastAPI on Vercel]                             │
              (REST endpoint)                                 │
                    │                                         │
                    ▼                                         │
              [Browser / Mobile]                              │
              (JSON response)                                 │
```

## 🔄 Data Flow Table

| Step | Component | Action |
|------|-----------|--------|
| 1 | WeatherAPI.com | Live weather data source (temp, humidity, timestamp) |
| 2 | GitHub Actions | Scheduled workflow runs every hour, executes Python script |
| 3 | Python Script | Fetches data for 4 cities, handles errors, prepares records |
| 4 | Supabase | Cloud PostgreSQL database stores all historical readings |
| 5 | FastAPI | REST API endpoint queries database and returns JSON |
| 6 | Vercel | Hosts the FastAPI application, auto-deploys on git push |
| 7 | Browser | Any device can access the live API endpoint |

## 🚀 Live Demo

**API Endpoint:** `https://weather-automation-wine.vercel.app/`

Returns real-time weather data for:
- Paris, France
- London, UK
- Tokyo, Japan
- New York, USA

## 🛠️ Technology Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| Orchestration | GitHub Actions | Schedule and run pipeline every hour |
| Data Extraction | Python + Requests | Fetch data from WeatherAPI |
| Database | Supabase (PostgreSQL) | Cloud storage for historical data |
| API Layer | FastAPI | RESTful endpoint for data access |
| Hosting | Vercel | Serverless deployment of FastAPI |
| Secrets Management | GitHub Secrets & .env | Secure API key storage |

## 📁 Project Structure

```
weather_automation/
├── api/
│   └── index.py          # FastAPI application (Vercel entry point)
├── .github/
│   └── workflows/
│       └── pipeline.yml  # GitHub Actions automation
├── app.py                 # Main pipeline script
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel deployment config
└── .env                  # Local environment variables (not committed)
```

## 🔧 Key Features

- Fully Automated - Runs every hour without manual intervention
- Cloud-Native - No local dependencies, runs entirely on cloud infrastructure
- Error Resilient - Per-city retry logic prevents single failures from stopping the pipeline
- Historical Tracking - Every reading stored with timestamp for trend analysis
- Accessible API - JSON endpoint accessible from any device worldwide

## 📈 Sample API Response

```json
[
  {
    "id": 1,
    "city": "Paris",
    "temperature": 23,
    "humidity": 36,
    "timestamp": "2026-04-08 14:52",
    "ingested_at": "2026-04-08T22:52:31.755765"
  },
  {
    "id": 2,
    "city": "London",
    "temperature": 23.3,
    "humidity": 41,
    "timestamp": "2026-04-08 13:52",
    "ingested_at": "2026-04-08T22:52:32.683956"
  }
]
```

## 🏗️ Architecture Decisions

| Decision | Rationale |
|----------|-----------|
| Supabase over local DB | Cloud persistence allows API access from anywhere |
| FastAPI over Flask | Automatic JSON serialization, built-in async support |
| Vercel over Render | Simpler deployment, automatic HTTPS, GitHub integration |
| GitHub Actions over Cron | Free, logs are built-in, manual trigger capability |
| Per-city error handling | Prevents one failed city from blocking others |

## 🔜 Future Improvements

- Add data visualization frontend (React/Next.js)
- Implement temperature trend alerts
- Add more cities and weather metrics (wind, pressure)
- Create historical aggregation endpoints
- Add API authentication for production use

## 👨‍💻 Author

Built as a data engineering learning project demonstrating:
- API integration
- Cloud database management
- CI/CD pipelines
- Serverless deployment
- REST API development

---

**Live API:** `https://weather-automation-wine.vercel.app/`

---

