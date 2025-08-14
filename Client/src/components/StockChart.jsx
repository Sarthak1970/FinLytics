import React, { useEffect, useState } from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";
import { fetchStock } from "../utils/api";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const StockChart = ({ symbol }) => {
  const [chartData, setChartData] = useState(null);
  const [summary, setSummary] = useState(null);

  useEffect(() => {
    if (!symbol) return;

    const fetchData = async () => {
      try {
        const data = await fetchStock(symbol);

        const labels = data.historical.map((s) => s.date);
        const closes = data.historical.map((s) => s.close);

        // Add prediction as next day label
        const lastDate = new Date(labels[labels.length - 1]);
        const nextDate = new Date(lastDate);
        nextDate.setDate(nextDate.getDate() + 1);
        const nextDateStr = nextDate.toISOString().split("T")[0];

        const lineDataset = {
          label: "Close Price",
          data: [...closes, null], // leave prediction for separate dataset
          borderColor: "rgba(75, 192, 192, 1)",
          backgroundColor: "rgba(75, 192, 192, 0.2)",
          tension: 0.4,
        };

        const smaDataset = {
          label: "SMA 50",
          data: Array(labels.length + 1).fill(data.sma_50),
          borderColor: "rgba(153, 102, 255, 1)",
          borderDash: [5, 5],
          pointRadius: 0,
          tension: 0.4,
        };

        const weekHighDataset = {
          label: "52 Week High",
          data: Array(labels.length + 1).fill(data["52_week"].high),
          borderColor: "rgba(255, 99, 132, 0.8)",
          borderDash: [10, 5],
          pointRadius: 0,
        };

        const weekLowDataset = {
          label: "52 Week Low",
          data: Array(labels.length + 1).fill(data["52_week"].low),
          borderColor: "rgba(54, 162, 235, 0.8)",
          borderDash: [10, 5],
          pointRadius: 0,
        };

        const predictionDataset = {
          label: "Next Day Prediction",
          data: Array(labels.length).fill(null).concat([data.prediction]),
          borderColor: "rgba(255, 206, 86, 1)",
          backgroundColor: "rgba(255, 206, 86, 0.5)",
          pointRadius: 6,
          pointStyle: "rectRot",
          showLine: false,
        };

        setChartData({
          labels: [...labels, nextDateStr],
          datasets: [
            lineDataset,
            smaDataset,
            weekHighDataset,
            weekLowDataset,
            predictionDataset,
          ],
        });

        setSummary({
          sma_50: data.sma_50,
          weekHigh: data["52_week"].high,
          weekLow: data["52_week"].low,
          prediction: data.prediction,
        });
      } catch (err) {
        console.error("Error fetching stock data:", err);
      }
    };

    fetchData();
  }, [symbol]);

  const options = {
    responsive: true,
    plugins: {
      legend: { position: "top" },
      title: { display: true, text: `Stock Chart: ${symbol}` },
      tooltip: { mode: "index", intersect: false },
    },
    scales: {
      x: { type: "category" },
      y: { beginAtZero: false },
    },
  };

  return (
    <>
      {chartData ? (
        <>
          <Line options={options} data={chartData} />
          {summary && (
            <div className="mt-2 text-gray-700">
              <p>SMA 50: {summary.sma_50}</p>
              <p>52 Week High: {summary.weekHigh}</p>
              <p>52 Week Low: {summary.weekLow}</p>
              <p>Next Day Prediction: {summary.prediction}</p>
            </div>
          )}
        </>
      ) : (
        <p>Loading...</p>
      )}
    </>
  );
};

export default StockChart;
