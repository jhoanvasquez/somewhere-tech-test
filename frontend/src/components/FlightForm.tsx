import { useState } from "react";
import axios from "axios";

interface Props {
  onResult: (data: any) => void;
}

function FlightForm({ onResult }: Props) {
  const [origin, setOrigin] = useState("");
  const [destinations, setDestinations] = useState("");
  const apiUrl = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!origin || !destinations) return;

    try {
      const destArray = destinations.split(",").map((d) => d.trim());
      const params = new URLSearchParams();
      params.append("origin", origin);
      destArray.forEach((d) => params.append("destinations", d));

      const res = await axios.get(`${apiUrl}/optimize-flight?${params.toString()}`);

      onResult(res.data);
    } catch (err) {
      console.error(err);
      onResult({ error: "Failed to fetch flights." });
    }
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white shadow-md rounded p-6 mb-4 w-full max-w-md">
      <label className="block mb-2 font-medium">Departure City:</label>
      <input
        type="text"
        value={origin}
        onChange={(e) => setOrigin(e.target.value)}
        className="border p-2 rounded w-full mb-4"
        placeholder="e.g., London"
      />

      <label className="block mb-2 font-medium">Destination Cities (comma separated):</label>
      <input
        type="text"
        value={destinations}
        onChange={(e) => setDestinations(e.target.value)}
        className="border p-2 rounded w-full mb-4"
        placeholder="e.g., Paris, Berlin, Madrid"
      />

      <button
        type="submit"
        className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
      >
        Find Best Flight
      </button>
    </form>
  );
}

export default FlightForm;
