import { useState } from "react";
import FlightForm from "./components/FlightForm";
import ResultCard from "./components/ResultCard";

function App() {
  const [result, setResult] = useState<any>(null);

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-6">
      <h1 className="text-3xl font-bold mb-6">✈️ Flight Optimizer</h1>
      <FlightForm onResult={setResult} />
      {result && <ResultCard result={result} />}
    </div>
  );
}

export default App;
