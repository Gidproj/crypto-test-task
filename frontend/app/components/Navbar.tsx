"use client";

export default function Navbar() {
  return (
    <nav className="flex items-center justify-between mb-12">
      
      {/* LOGO */}
      <div className="flex items-center gap-3">
        <div className="w-4 h-4 rounded-full bg-orange-500 shadow-[0_0_20px_rgba(255,120,0,0.9)]" />

        <h1 className="text-2xl font-bold tracking-wide">
          Coinio
        </h1>
      </div>

      {/* LINKS */}
      <div className="hidden md:flex items-center gap-10 text-white/70">
        <a
          href="#"
          className="hover:text-orange-400 transition-all"
        >
          Market
        </a>

        <a
          href="#"
          className="hover:text-orange-400 transition-all"
        >
          Features
        </a>

        <a
          href="#"
          className="hover:text-orange-400 transition-all"
        >
          Analytics
        </a>

        <a
          href="#"
          className="hover:text-orange-400 transition-all"
        >
          Portfolio
        </a>
      </div>

      {/* BUTTON */}
      <button className="px-6 py-3 rounded-full bg-white text-black font-semibold hover:scale-105 transition-all">
        Login
      </button>
    </nav>
  );
}