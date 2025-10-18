interface Props {
  result: any;
}

function ResultCard({ result }: Props) {
  if (result.error) {
    return <div className="text-red-600 font-semibold">{result.error}</div>;
  }

  return (
    <div className="bg-white shadow-lg rounded p-6 mt-4 w-full max-w-md">
      <h2 className="text-xl font-bold mb-2">Best Destination</h2>
      <p className="mb-2">🏙️ {result.best_destination}</p>
      <p className="mb-2">💵 Price: ${result.price}</p>
      <p className="mb-2">📏 Distance: {result.distance} km</p>
      <p className="font-semibold">⚖️ Value: ${result.value_usd_per_km}/km</p>
    </div>
  );
}

export default ResultCard;
