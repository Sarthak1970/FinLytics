# 📈 Stock Dashboard Project

A real-time stock dashboard built with React and Node.js, visualizing stock prices, technical indicators, and predictive analytics. The app allows users to select companies, view historical stock charts, and analyze predictions and 52-week statistics.

---

## Features ✨

### 1. Company Selection
- Dynamic list of companies fetched from the backend.
- Click on a company to view its stock chart and details.
- Currently selected company is highlighted in the sidebar.


### 2. Stock Charts 📊
- Line chart displaying **historical closing prices**.
- Overlay of **50-day Simple Moving Average (SMA 50)**.
- Visual markers for **52-week high, low, and average**.
- Highlighted **predicted next-day closing price**.

### 3. Data Summary 📑
- Below the chart, displays:
  - 52 Week Max 📈
  - 52 Week Min 📉
  - 52 Week Average ⚖️
  - SMA 50 (if available)
  - Next day prediction (from AI/ML model 🤖)

### 4. Interactive Sidebar
- Sidebar background gray (`bg-gray-800`) with company list.
- Company heading background yellow (`bg-yellow-500`).
- Currently selected company highlighted with bold text and gray background.
- Hover effects on other companies for better UX.

### 5. AI/ML Prediction 🤖
- Backend provides next-day price prediction using a simple predictive model.
- Visualization included on chart as a horizontal marker (optional).

---

## Tech Stack 🛠️

- **Frontend:** React, Tailwind CSS, Chart.js (via `react-chartjs-2`)
- **Backend:** Node.js, Express (or any backend framework you are using)
- **Data:** Stock historical data + AI/ML predictions
- **Deployment:** Docker / Docker Compose support

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/stock-dashboard.git
cd stock-dashboard
```
2. **Installing Dependencies**
```bash
cd server
npm install


cd client
npm install
```

3. **Running Locally**
```bash
cd server
npm run dev

cd client
npm start
```

4.Using Docker
```bash
docker build -t stock-dashboard .
docker run -p 3000:3000 stock-dashboard

docker-compose up --build
```

## Contributing

1. Fork the repository.

2. Create a new branch:

   ```bash
   git checkout -b feature/xyz
3.Commit your changes:

```bash
Copy
Edit
git commit -m "Add your message here"
```

4.Push to the branch and create a pull request:
```bash
Copy
Edit
git push origin feature/xyz
```
