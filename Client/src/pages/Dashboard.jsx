import { useState } from "react";
import Sidebar from "../components/Sidebar";
import StockChart from "../components/StockChart";

export default function Dashboard() {
  const [selected, setSelected] = useState(null);

  return (
    <div className="flex">
      <Sidebar selected={selected} onSelect={setSelected} />
      <main className="flex-1 p-4">
        {selected ? (
          <StockChart symbol={selected} />
        ) : (
          <p className="text-gray-500">Select a company to see the stock chart</p>
        )}
      </main>
    </div>
  );
}
