"use client";
"use client";

import { useState } from "react";
import { Chart as ChartJS } from "chart.js";
import { Chart, Line } from "react-chartjs-2";
import {
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

interface PredictionData {
  value: number;
  date: string;
}

import TrainButton from "@/components/train_buttton";
import Image from "next/image";
export default function Home() {
  const [predictionData, setPredictionData] = useState<PredictionData[]>([]);

  console.log(predictionData);
  const handlePredictClick = () => {
    const cryptoSelect = document.getElementById(
      "crypto-select"
    ) as HTMLSelectElement;
    const periodSelect = document.getElementById(
      "period-select"
    ) as HTMLSelectElement;

    const selectedCrypto = cryptoSelect.value;
    const selectedPeriod = parseInt(periodSelect.value);

    if (!selectedCrypto || !selectedPeriod) {
      alert("Please select both a cryptocurrency and a prediction period.");
      return;
    }

    fetch("http://localhost:8000/api/model/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        crypto: selectedCrypto,
        days: selectedPeriod,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
        setPredictionData(data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
        <h1 className="text-4xl font-bold">Crypto Previewer</h1>
        <div className="flex flex-row gap-4">
          <div className="flex flex-col gap-4">
            <label htmlFor="crypto-select" className="text-sm font-medium">
              Choose a cryptocurrency:
            </label>
            <select
              id="crypto-select"
              className="p-2 border rounded text-black"
            >
              <option value="SOL-USD">Solana (SOL-USD)</option>
              <option value="BTC-USD">Bitcoin (BTC-USD)</option>
              <option value="ETH-USD">Ethereum (ETH-USD)</option>
              <option value="LTC-USD">Litecoin (LTC-USD)</option>
              <option value="XRP-USD">Ripple (XRP-USD)</option>
              <option value="ADA-USD">Cardano (ADA-USD)</option>
              <option value="DOT-USD">Polkadot (DOT-USD)</option>
            </select>
          </div>
          <div className="flex flex-col gap-4">
            <label htmlFor="period-select" className="text-sm font-medium">
              Choose a prediction period:
            </label>
            <select
              id="period-select"
              className="p-2 border rounded text-black"
            >
              <option value="1">1 Day</option>
              <option value="7">1 Week</option>
              <option value="14">2 Weeks</option>
              <option value="30">1 Month</option>
              {/* Add more options as needed */}
            </select>
          </div>
        </div>
        {predictionData.length > 0 && (
          <div className="w-full mt-8">
            <h2 className="text-xl font-bold mb-4">Prediction Result</h2>
            <Chart
              type="line"
              data={{
                labels: Array.isArray(predictionData)
                  ? predictionData.map((data) => {
                      const date = new Date(data.date);
                      return `${
                        date.getMonth() + 1
                      }/${date.getDate()}/${date.getFullYear()}`;
                    })
                  : [],
                datasets: [
                  {
                    label: "Price",
                    data: Array.isArray(predictionData)
                      ? predictionData.map((data) => data.value)
                      : [],
                    borderColor: "rgba(75, 192, 192, 1)",
                    backgroundColor: "rgba(75, 192, 192, 0.2)",
                  },
                ],
              }}
              options={{
                responsive: true,
                plugins: {
                  legend: {
                    position: "top",
                  },
                  title: {
                    display: true,
                    text: "Cryptocurrency Price Prediction",
                  },
                },
              }}
            />
          </div>
        )}
        <div className="flex flex-row align-middle w-full justify-center gap-5">
          <button
            className="mt-4 w-[9vw] h-[4vh] bg-blue-500 text-white rounded hover:bg-blue-600"
            onClick={handlePredictClick}
          >
            Predict
          </button>
          <TrainButton />
        </div>
      </main>
      <footer className="row-start-3 flex gap-6 flex-wrap items-center justify-center">
        <a
          className="flex items-center gap-2 hover:underline hover:underline-offset-4"
          href="/logs"
          rel="noopener noreferrer"
        >
          <Image
            aria-hidden
            src="https://nextjs.org/icons/file.svg"
            alt="File icon"
            width={16}
            height={16}
          />
          Logs
        </a>
        <a
          className="flex items-center gap-2 hover:underline hover:underline-offset-4"
          href="/"
          rel="noopener noreferrer"
        >
          <Image
            aria-hidden
            src="https://nextjs.org/icons/window.svg"
            alt="Window icon"
            width={16}
            height={16}
          />
          Predict
        </a>
      </footer>
    </div>
  );
}
