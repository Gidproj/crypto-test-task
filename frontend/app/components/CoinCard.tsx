interface Props {
  name: string;
  symbol: string;
  price?: number;
  color: "orange" | "purple";
}

export default function CoinCard({
  name,
  symbol,
  price,
  color,
}: Props) {
  return (
    <div className="glass rounded-3xl p-6 flex items-center justify-between">
      <div>
        <p className="text-gray-400">{name}</p>

        <h2 className="text-5xl font-bold mt-2">{symbol}</h2>
      </div>

      <div className="text-right">
        <p className="text-gray-400">Current Price</p>

        <h3
          className={`text-3xl font-bold mt-2 ${
            color === "orange" ? "text-orange-400" : "text-purple-400"
          }`}
        >
          {price ? `$${price.toLocaleString()}` : "..."}
        </h3>
      </div>
    </div>
  );
}