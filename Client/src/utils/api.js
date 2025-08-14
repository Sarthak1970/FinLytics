const BASE_URL =
  import.meta.env?.VITE_API_URL ||
  "https://finlytics-5zk8.onrender.com";

export async function fetchCompanies() {
  const res = await fetch(`${BASE_URL}/companies`);
  return res.json();
}

export async function fetchStock(symbol) {
  const res = await fetch(`${BASE_URL}/stock/${symbol}`);
  if (!res.ok) throw new Error("Failed to fetch stock data");
  return res.json();
}
