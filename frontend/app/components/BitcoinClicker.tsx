"use client";
import { useState } from 'react';

export default function BitcoinClicker() {
  const [count, setCount] = useState(0);

  return (
    <div className="flex flex-col items-center justify-center min-h-[60vh] p-8">
      {/* Контейнер монеты */}
      <div 
        className="cursor-pointer transition-transform duration-150 active:scale-95"
        onClick={() => setCount(count + 1)}
      >
        {/* Здесь используйте ваше изображение (изображение.jpg) */}
        <img 
          src="/bitcoin-coin.png" 
          alt="Bitcoin" 
          className="w-64 h-64 drop-shadow-[0_0_15px_rgba(247,147,26,0.5)]"
        />
      </div>

      {/* Счетчик */}
      <div className="mt-8 backdrop-blur-md bg-white/10 border border-white/20 p-6 rounded-2xl shadow-xl">
        <h2 className="text-white text-lg opacity-80 uppercase tracking-widest">Balance</h2>
        <p className="text-5xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-orange-600">
          {count.toLocaleString()} BTC
        </p>
      </div>
    </div>
  );
}