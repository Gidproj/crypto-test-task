import BitcoinClicker from "@/components/BitcoinClicker";

export default function TradingPage() {
  return (
    <div className="pt-20"> {/* Добавим отступ сверху, чтобы контент не залез под Navbar */}
      <BitcoinClicker />
    </div>
  );
}