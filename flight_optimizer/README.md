# ✈️ Flight Optimizer Backend (FastAPI + CLI)

This is the backend component of the Flight Optimizer project.  
It provides:
- A **Python CLI tool** to find the cheapest flight per kilometer
- A **FastAPI microservice** exposing the same functionality via HTTP API

---

## 🚀 Features
- Find cheapest flights by **$/km**
- Query multiple destinations at once
- CLI and REST API supported
- API key stored securely in `.env`

---

## 📂 Project Structure
```
flight_optimizer/
│── app.py                  # FastAPI app
│── flight_optimizer.py     # Core flight logic + CLI
│── requirements.txt        # Python dependencies
│── .env.example            # Example env file (no real key)
│── tests/
    └── test_flight_optimizer.py
```

---

## 🔧 Installation

### 1. Clone repo & create virtual environment
```bash
git clone <your-repo-url>
cd flight_optimizer
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
# OR
.venv\Scripts\activate      # Windows
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure `.env`
Copy `.env.example` to `.env` and add your Kiwi API key:
```env
KIWI_API_KEY=your_kiwi_api_key_here
```

---

## 🖥️ Usage

### CLI
```bash
python flight_optimizer.py --from London --to Paris Berlin Madrid
```

### API (FastAPI)
Start the server:
```bash
uvicorn app:app --reload
```

API endpoint:
```
GET http://127.0.0.1:8000/optimize-flight?origin=London&destinations=Paris&destinations=Berlin
```

---

## ✅ Testing
```bash
pytest -v
```

---

## 🛠️ Tech Stack
- Python 3.10+
- FastAPI
- httpx
- pytest
- python-dotenv
