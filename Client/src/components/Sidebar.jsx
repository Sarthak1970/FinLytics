import { useEffect, useState } from "react";
import { fetchCompanies } from "../utils/api";

export default function Sidebar({ selected, onSelect }) {
  const [companies, setCompanies] = useState([]);

  useEffect(() => {
    fetchCompanies().then(setCompanies).catch(console.error);
  }, []);

  return (
<aside className="w-64 bg-gray-800 text-white overflow-y-auto h-screen">
  {/* Yellow heading area */}
  <div className="bg-yellow-500 p-4">
    <h2 className="text-xl font-semibold unique-sidebar-title ">Companies</h2>
  </div>

  {/* Company list area */}
    <ul className="p-4">
        {companies.map((c) => (
        <li
            key={c.symbol}
            onClick={() => onSelect(c.symbol)}
            className={`cursor-pointer p-2 rounded mb-1 ${
            selected === c.symbol ? "bg-gray-700 font-bold" : "hover:bg-gray-700"
            }`}
        >
            {c.name}
        </li>
        ))}
    </ul>
    </aside>

  );
}
