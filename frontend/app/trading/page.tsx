"use client";
import { useState } from "react";

export default function TradingPage() {
  const [count, setCount] = useState(0);

  return (
    <main className="relative min-h-[calc(100vh-80px)] bg-black text-white flex flex-col items-center justify-center p-6 overflow-hidden">
      {/* Декоративное свечение */}
      <div className="orange-glow top-[-200px] right-[-100px]" />
      <div className="orange-glow bottom-[-250px] left-[-150px]" />

      <div className="z-10 flex flex-col items-center w-full max-w-2xl">
        <h1 className="text-4xl font-black mb-12 uppercase tracking-tighter">
          Bitcoin Clicker
        </h1>

        {/* Монета */}
        <div
          className="relative group cursor-pointer transition-transform duration-100 active:scale-95"
          onClick={() => setCount(count + 1)}
        >
          {/* Свечение под монетой */}
          <div className="absolute inset-0 bg-orange-500/20 blur-[80px] rounded-full group-hover:bg-orange-500/30 transition-all" />
          
          <img 
            src="/bitcoin.png" 
            alt="Bitcoin" 
            className="w-64 h-64 md:w-80 md:h-80 relative z-10 drop-shadow-[0_0_30px_rgba(247,147,26,0.3)] transition-all hover:scale-105"
          />
        </div>

        {/* Счетчик */}
        <div className="mt-16 backdrop-blur-md bg-white/5 border border-white/10 p-8 rounded-3xl shadow-2xl text-center w-full">
          <p className="text-gray-400 uppercase tracking-[0.2em] text-sm mb-2">
            Balance
          </p>
          <div className="text-6xl md:text-7xl font-black text-transparent bg-clip-text bg-gradient-to-b from-white to-gray-500">
            {count.toLocaleString()} <span className="text-orange-500">BTC</span>
          </div>
        </div>
      </div>
    </main>
  );
}