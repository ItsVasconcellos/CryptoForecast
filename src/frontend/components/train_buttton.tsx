"use client";

import { useState } from "react";

export default function TrainButton() {
  
    const [loading, setLoading] = useState(false);
    const handleTrain = async () => {
        setLoading(true);
        try {
        const crypto = (document.getElementById("crypto-select") as HTMLSelectElement).value;
        const period = (document.getElementById("period-select") as HTMLSelectElement).value;
        const response = await fetch("http://localhost:8000/api/model/train", {
            method: "GET",
            headers: {
            "Content-Type": "application/json",
            },      });
        if (!response.ok) {
            throw new Error("Erro ao treinar o modelo");
        }
        const data = await response.json();
        alert(`Modelo treinado com sucesso!`);
        } catch (error) {
        console.error(error);
        alert("An error occurred while getting the prediction.");
        } finally {
        setLoading(false);
        }
    };
    return(<button
        className="mt-4 w-[10vw] h-[4vh] bg-green-500 text-white rounded hover:bg-green-600"
        onClick={handleTrain}
        disabled={loading}
      >
        {loading ? "Retraining..." : "Retrain Models"}
      </button>)}