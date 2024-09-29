import Image from "next/image";

export default function Home() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
      <h1 className="text-2xl font-bold">Crypto Previewer</h1>
      <div className="flex flex-row gap-4">
      <div className="flex flex-col gap-4">
        <label htmlFor="crypto-select" className="text-sm font-medium">Choose a cryptocurrency:</label>
        <select id="crypto-select" className="p-2 border rounded text-black">
        <option value="bitcoin">Bitcoin</option>
        <option value="ethereum">Ethereum</option>
        <option value="litecoin">Litecoin</option>
        {/* Add more options as needed */}
        </select>
      </div>
      <div className="flex flex-col gap-4">
        <label htmlFor="period-select" className="text-sm font-medium">Choose a prediction period:</label>
        <select id="period-select" className="p-2 border rounded text-black">
        <option value="1d">1 Day</option>
        <option value="1w">1 Week</option>
        <option value="1m">1 Month</option>
        {/* Add more options as needed */}
        </select>
      </div>
      </div>
      <div className="flex flex-row align-middle w-full justify-center gap-5">
      <button className="mt-4 w-[9vw] h-[4vh] bg-blue-500 text-white rounded hover:bg-blue-600">
        Predict
      </button>
      <button className="mt-4 w-[10vw] h-[4vh] bg-green-500 text-white rounded hover:bg-green-600">
        Retrain Models
      </button>
      </div>
      </main>
      <footer className="row-start-3 flex gap-6 flex-wrap items-center justify-center">
      <a
        className="flex items-center gap-2 hover:underline hover:underline-offset-4"
        href="https://nextjs.org/learn?utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app"
        target="_blank"
        rel="noopener noreferrer"
      >
        <Image
        aria-hidden
        src="https://nextjs.org/icons/file.svg"
        alt="File icon"
        width={16}
        height={16}
        />
        Learn
      </a>
      <a
        className="flex items-center gap-2 hover:underline hover:underline-offset-4"
        href="https://vercel.com/templates?framework=next.js&utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app"
        target="_blank"
        rel="noopener noreferrer"
      >
        <Image
        aria-hidden
        src="https://nextjs.org/icons/window.svg"
        alt="Window icon"
        width={16}
        height={16}
        />
        Examples
      </a>
      <a
        className="flex items-center gap-2 hover:underline hover:underline-offset-4"
        href="https://nextjs.org?utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app"
        target="_blank"
        rel="noopener noreferrer"
      >
        <Image
        aria-hidden
        src="https://nextjs.org/icons/globe.svg"
        alt="Globe icon"
        width={16}
        height={16}
        />
        Go to nextjs.org →
      </a>
      </footer>
    </div>
  );
}
