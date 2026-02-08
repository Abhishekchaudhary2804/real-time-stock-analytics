# 📈 Real-Time Stock Analytics Dashboard

A full-stack stock market analytics platform built with Python that fetches live stock data, computes technical indicators, generates trading signals, and visualizes everything on an interactive Streamlit dashboard.

---

## 🌐 Live Project

👉 https://abhishek-chaudhary-hjgpsfelq3st24alwvcrus.streamlit.app/

---

## 🚀 Features

- Live stock data using Yahoo Finance (yfinance)
- Candlestick charts with Plotly
- Technical indicators:
  - RSI
  - MACD
  - SMA / EMA
- Automated BUY / SELL signals
- SQLite database for historical storage
- Telegram alerts for signals
- Interactive Streamlit dashboard
- Multi-stock support (AAPL, TSLA, MSFT, NVDA, GOOGL, etc.)
- REST API built with FastAPI

---

## 🧠 Tech Stack

- Python  
- FastAPI  
- Streamlit  
- SQLite  
- Pandas / NumPy  
- Plotly  
- SQLAlchemy  
- yfinance  
- Requests  

---

## ⚙️ Run Locally

### 1. Clone repository

```bash
git clone https://github.com/Abhishekchaudhary2804/real-time-stock-analytics.git
cd real-time-stock-analytics
 
#### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt

▶ Start Backend (FastAPI)
uvicorn app.main:app --reload


Backend runs at:

http://127.0.0.1:8000

▶ Start Dashboard (Streamlit)

Open new terminal:

streamlit run dashboard.py


Dashboard opens in browser.

📌 Example Symbols
AAPL
TSLA
MSFT
GOOGL
NVDA
AMZN
META


Indian stocks:

INFY.NS
TCS.NS
RELIANCE.NS

📡 API Endpoints

/stock/{symbol} → Stock data + indicators

/signals/{symbol} → Trading signals

/top-movers → Top moving stocks

.

👨‍💻 Author

Abhishek