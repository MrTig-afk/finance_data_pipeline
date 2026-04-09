from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
import yfinance as yf
from supabase import create_client
today = datetime.now().weekday()
if today >= 5:
    print("Weekend detected. Pipeline stopping.")
    exit(0)
    
symbols=[]
# Got to get parse the text from the .txt file
with open('stocks.txt', 'r') as file:
    for line in file:
        # 1. Clean the line
        clean_line = line.strip()
        
        # 2. Skip empty lines or comments
        if not clean_line or clean_line.startswith('#'):
            continue
        symbols.append(clean_line)
print(f"Loaded {len(symbols)} symbols")

SUPABASE_URL=os.getenv("SUPABASE_URL")
SUPABASE_KEY=os.getenv("SUPABASE_KEY")

client= create_client(SUPABASE_URL,SUPABASE_KEY)
for symbol in symbols:
    ticker= yf.Ticker(symbol)
    data= ticker.history(period="1d", interval="1h")
    for index, row in data.iterrows():
        record= {
            "symbol": symbol,
            "timestamp": index.isoformat(),
            "open_price":row['Open'],
            "close_price": row['Close'],
            "low_price": row['Low'],
            "volume": int(row['Volume']),
            "high_price": row['High']
        }
        client.table("stock_prices").insert(record).execute()
    print(f"Inserted {len(data)} rows for {symbol}")