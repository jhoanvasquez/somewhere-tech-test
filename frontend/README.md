# ✈️ Flight Optimizer Frontend (React + TypeScript)

This is the frontend interface for the Flight Optimizer project.  
It allows users to input departure and destination cities and displays the best flight in **$/km**.

---

## 🚀 Features
- Input for departure city
- Input for multiple destination cities (comma-separated)
- Calls FastAPI backend to compute best flight
- Displays best destination, price, distance, and $/km value
- Configurable backend URL via `.env`

---

## 📂 Project Structure
```
frontend/
│── src/
│   ├── App.tsx
│   ├── components/
│   │   ├── FlightForm.tsx
│   │   └── ResultCard.tsx
│   └── main.tsx
│── package.json
│── tsconfig.json
│── vite.config.ts
│── .env.example
```

---

## 🔧 Installation

### 1. Clone repo
```bash
cd frontend
```

### 2. Install dependencies
```bash
npm install
```

### 3. Configure `.env`
Copy `.env.example` to `.env` and set the backend URL:
```env
VITE_API_URL=http://127.0.0.1:8000
```

---

## 🖥️ Usage

### Run development server
```bash
npm run dev
```

Visit 👉 http://localhost:5173

### Build for production
```bash
npm run build
npm run preview
```

---

## 🛠️ Tech Stack
- React 18
- TypeScript
- Vite
- Axios
- TailwindCSS (for styling)
