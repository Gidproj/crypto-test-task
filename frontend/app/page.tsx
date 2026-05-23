"use client";

import Navbar from "./components/Navbar";
import CoinCard from "./components/CoinCard";
import CryptoChart from "./components/CryptoChart";

export default function Home() {
  return (
    <main className="relative overflow-hidden min-h-screen bg-black text-white">

    <div className="orange-glow top-[-200px] right-[-100px]" />
    <div className="orange-glow bottom-[-250px] left-[-150px]" />
      <Navbar />

      <section className="max-w-7xl mx-auto mt-16 grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">
        
        {/* LEFT */}
        <div>
          <p className="uppercase tracking-[0.3em] text-gray-400 mb-4">
            Crypto Platform
          </p>

          <h1 className="text-7xl font-black leading-none">
            CRYPTO
            <br />
            EXCHANGE
          </h1>

          <p className="text-gray-400 mt-6 max-w-xl text-lg leading-relaxed">
            Real-time cryptocurrency dashboard powered by
            FastAPI and Next.js.
          </p>

          <div className="flex gap-4 mt-8">
            <button className="px-8 py-4 rounded-full bg-orange-500 hover:bg-orange-400 transition-all font-semibold">
              Start Trading
            </button>

            <button className="px-8 py-4 rounded-full border border-white/20 hover:border-orange-400 transition-all">
              Learn More
            </button>
          </div>
        </div>

        {/* RIGHT */}
        <div className="glass rounded-[32px] p-6">
          <div className="grid gap-4">

            <CoinCard
              name="Bitcoin"
              symbol="BTC"
              price={104233}
              color="orange"
            />

            <CoinCard
              name="Ethereum"
              symbol="ETH"
              price={3120}
              color="purple"
            />

            <CryptoChart />

          </div>
        </div>
      </section>
    </main>
  );
}