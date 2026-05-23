"use client";

import {
  LineChart,
  Line,
  XAxis,
  Tooltip,
} from "recharts";

const data = [
  { name: "Mon", price: 92000 },
  { name: "Tue", price: 94000 },
  { name: "Wed", price: 91000 },
  { name: "Thu", price: 98000 },
  { name: "Fri", price: 102000 },
  { name: "Sat", price: 104000 },
];

export default function CryptoChart() {
  return (
    <div className="bg-[#18181b] rounded-[32px] p-6 h-[320px]">
      <div className="flex items-start justify-between mb-6">
        <div>
          <p className="text-gray-400 text-sm">Market Analytics</p>
          <h3 className="text-2xl font-bold text-white">BTC Trend</h3>
        </div>

        <div className="text-right">
          <p className="text-green-400 text-2xl font-bold">+18.4%</p>
          <p className="text-gray-500 text-sm">this month</p>
        </div>
      </div>

      <div className="flex justify-center">
        <LineChart
          width={420}
          height={180}
          data={data}
        >
          <XAxis
            dataKey="name"
            stroke="#888"
          />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="price"
            stroke="#f97316"
            strokeWidth={4}
            dot={false}
          />
        </LineChart>
      </div>
    </div>
  );
}