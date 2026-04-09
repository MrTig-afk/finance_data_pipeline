# 📈 Stock Pipeline - Automated Global Stock Data Platform

An end-to-end automated data pipeline that collects, stores, and tracks hourly stock prices for 50+ global stocks across multiple markets.

## 📊 Architecture Visualization

```
Yahoo Finance API → GitHub Actions → Supabase (PostgreSQL)
    (free)           (every hour)         (cloud DB)

                         │
                         ▼
                   Historical Data
                   (50+ stocks, hourly)
```

## 🔄 Data Flow

| Step | Component | Action |
|------|-----------|--------|
| 1 | Yahoo Finance API | Free, no API key required |
| 2 | GitHub Actions | Scheduled workflow runs at 10 minutes past every hour |
| 3 | Python Script | Fetches hourly data for 50+ global stocks |
| 4 | Supabase | Cloud PostgreSQL database stores all historical prices |
| 5 | Weekend Detection | Pipeline automatically skips Saturday/Sunday runs |

## 🌍 Global Stock Coverage

| Market | Count | Examples |
|--------|-------|----------|
| 🇺🇸 NYSE/NASDAQ | 10 | AAPL, MSFT, GOOGL, AMZN, META, NVDA |
| 🇮🇳 NSE (India) | 10 | RELIANCE, TCS, INFY, HDFCBANK |
| 🇦🇺 ASX (Australia) | 10 | CBA, BHP, CSL, WBC |
| 🇯🇵 Nikkei (Japan) | 10 | 7203.T (Toyota), 6758.T (Sony) |
| 🇬🇧 LSE (London) | 10 | HSBA, AZN, SHEL, BP |
| 🇨🇳 Shanghai | 10 | 600519.SS (Kweichow Moutai) |

**Total: 50+ stocks across 6 global markets**

## 🛠️ Technology Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| Orchestration | GitHub Actions | Schedule and run pipeline every hour |
| Data Extraction | yfinance | Fetch stock data from Yahoo Finance |
| Database | Supabase (PostgreSQL) | Cloud storage for historical prices |
| Language | Python | ETL logic and data processing |
| Secrets Management | GitHub Secrets | Secure database credentials |

## 📁 Project Structure

```
stock-pipeline/
├── stock_pipeline.py    # Main pipeline script
├── stocks.txt           # List of 50+ stock symbols
├── requirements.txt     # Python dependencies
└── .github/workflows/
    └── stock-pipeline.yml  # GitHub Actions automation
```

## 📈 Sample Data Schema

```sql
CREATE TABLE stock_prices (
    id BIGINT PRIMARY KEY,
    symbol TEXT,
    timestamp TIMESTAMP,
    open_price DECIMAL(10,4),
    high_price DECIMAL(10,4),
    low_price DECIMAL(10,4),
    close_price DECIMAL(10,4),
    volume BIGINT,
    ingested_at TIMESTAMP
);
```

## 🔧 Key Features

- **🌍 Global Coverage** - 50+ stocks from 6 major markets
- **⏰ Fully Automated** - Runs hourly during trading days
- **📊 Historical Tracking** - Every price point stored with timestamp
- **🚫 Weekend Detection** - Automatically skips Saturday/Sunday runs
- **☁️ Cloud-Native** - No local dependencies, runs entirely on GitHub
- **🛡️ Error Resilient** - Per-stock error handling prevents complete failures

## 📊 Sample Output

```json
{
    "symbol": "AAPL",
    "timestamp": "2026-04-09 14:30:00",
    "open_price": 258.51,
    "high_price": 259.75,
    "low_price": 256.53,
    "close_price": 258.13,
    "volume": 10222566
}
```

## 🚀 Deployment

### GitHub Actions Schedule

The pipeline runs at **10 minutes past every hour** (e.g., 1:10, 2:10, 3:10):

```yaml
on:
  schedule:
    - cron: "10 * * * *"
```

### Required Secrets

Add these to your GitHub repository (Settings → Secrets and Variables → Actions):

| Secret | Purpose |
|--------|---------|
| `SUPABASE_URL` | Your Supabase project URL |
| `SUPABASE_KEY` | Your Supabase service role key |

## 🏗️ Architecture Decisions

| Decision | Rationale |
|----------|-----------|
| **yfinance over paid APIs** | Free, no API key required, reliable |
| **Supabase over local DB** | Cloud persistence allows future API access |
| **10 minutes past hour** | Avoids top-of-hour GitHub Actions traffic |
| **Weekend detection** | Saves compute time when markets are closed |
| **Per-stock error handling** | Prevents one failed stock from blocking others |

## 🔜 Future Improvements

- [ ] Add FastAPI endpoint to serve stock data
- [ ] Implement moving averages (7-day, 30-day)
- [ ] Add top gainers/losers endpoint
- [ ] Create real-time alerts for price movements
- [ ] Add more stocks and markets
- [ ] Build simple frontend dashboard

## 👨‍💻 Author

Built as a data engineering learning project demonstrating:

- API integration (yfinance)
- Cloud database management (Supabase)
- CI/CD pipelines (GitHub Actions)
- Multi-market data collection
- Error handling and resilience

---

**Live Demo:** API coming soon (FastAPI deployment in progress)
