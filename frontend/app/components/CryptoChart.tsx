"use client";

import {
  AreaChart,
  Area,
  ResponsiveContainer,
} from "recharts";

const data = [
  { value: 120 },
  { value: 210 },
  { value: 180 },
  { value: 260 },
  { value: 240 },
  { value: 320 },
  { value: 280 },
  { value: 390 },
  { value: 420 },
  { value: 460 },
];

export default function CryptoChart() {
  return (
    <div className="glass rounded-3xl p-6 h-[320px]">
      <div className="flex justify-between items-center mb-6">
        <div>
          <p className="text-white/50 text-sm">
            Market Analytics
          </p>

          <h2 className="text-3xl font-bold mt-2">
            BTC Trend
          </h2>
        </div>

        <div className="text-right">
          <p className="text-green-400 text-lg font-semibold">
            +18.4%
          </p>

          <p className="text-white/40 text-sm">
            this month
          </p>
        </div>
      </div>

      <ResponsiveContainer width="100%" height="80%">
        <AreaChart data={data}>
          <defs>
            <linearGradient id="colorValue" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#ff7b00" stopOpacity={0.8} />
              <stop offset="100%" stopColor="#ff7b00" stopOpacity={0} />
            </linearGradient>
          </defs>

          <Area
            type="monotone"
            dataKey="value"
            stroke="#ff7b00"
            strokeWidth={4}
            fill="url(#colorValue)"
          />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
}