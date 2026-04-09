from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
import yfinance as yf
from supabase import create_client

# 1. Weekend Check
today = datetime.now().weekday()
if today >= 5:
    print("Weekend detected. Pipeline stopping.")
    exit(0)

# 2. Load Symbols from .txt
symbols = []
try:
    with open('stocks.txt', 'r') as file:
        for line in file:
            clean_line = line.strip()
            if not clean_line or clean_line.startswith('#'):
                continue
            symbols.append(clean_line)
    print(f"Loaded {len(symbols)} symbols")
except FileNotFoundError:
    print("Error: stocks.txt not found.")
    exit(1)

# 3. Setup Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
client = create_client(SUPABASE_URL, SUPABASE_KEY)

# 4. Collect Data into a List (The Bulk Strategy)
all_records = []

for symbol in symbols:
    try:
        ticker = yf.Ticker(symbol)
        # period="1d" interval="1h" pulls the full trading day history
        data = ticker.history(period="1d", interval="1h")
        
        if data.empty:
            print(f"No data found for {symbol}")
            continue

        for index, row in data.iterrows():
            record = {
                "symbol": symbol,
                "timestamp": index.isoformat(),
                "open_price": row['Open'],
                "close_price": row['Close'],
                "low_price": row['Low'],
                "high_price": row['High'],
                "volume": int(row['Volume'])
            }
            all_records.append(record)
        
        print(f"Fetched {len(data)} rows for {symbol}")
    except Exception as e:
        print(f"Error fetching {symbol}: {e}")

# 5. The Big Push (Single Request)
if all_records:
    try:
        # Passing a list to .insert() performs a single Bulk Insert
        client.table("stock_prices").insert(all_records).execute()
        print(f"\nSuccessfully bulk inserted {len(all_records)} total records.")
    except Exception as e:
        print(f"\nDatabase Insert Failed: {e}")
else:
    print("No data collected to insert.")