"use client";

import React, { useState } from "react";
import { Table, Pagination } from "semantic-ui-react";

import Image from "next/image";
import RootLayout from "@/app/layout";

interface Log {
  log_level: string;
  message: string;
  timestamp: string;
}

export default function logs() {
  const [activePage, setActivePage] = useState(1);
  const logsPerPage = 10;

  const [loading, setLoading] = useState(false);
  // Example logs data
  const [logs, setLogs] = useState<Log[]>([]);
  const getLog = async () => {
    setLoading(true);
    try {
      const crypto = (
        document.getElementById("crypto-select") as HTMLSelectElement
      ).value;
      const period = (
        document.getElementById("period-select") as HTMLSelectElement
      ).value;
      const response = await fetch("http://localhost:8000/api/logs", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });
      if (!response.ok) {
        throw new Error("Erro ao treinar o modelo");
      }
      const data = await response.json();
      setLogs(data ?? []);
    } catch (error) {
      console.error(error);
      alert("An error occurred while getting the prediction.");
    } finally {
      setLoading(false);
    }
  };

  const totalPages = Math.ceil(logs.length / logsPerPage);
  const displayedLogs = logs.slice(
    (activePage - 1) * logsPerPage,
    activePage * logsPerPage
  );

  const handlePageChange = (e: any, { activePage }: any) => {
    setActivePage(activePage);
  };

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <h1 className="text-4xl font-bold">Crypto Previewer</h1>
      <div className="w-2/4">
        <h1>Logs</h1>
        {loading && <p>Loading...</p>}
        <Table celled>
          <Table.Header>
            <Table.Row>
              <Table.HeaderCell>Log_Level</Table.HeaderCell>
              <Table.HeaderCell>Message</Table.HeaderCell>
              <Table.HeaderCell>Timestamp</Table.HeaderCell>
            </Table.Row>
          </Table.Header>
          <Table.Body>
            {displayedLogs.map((log, index) => (
              <Table.Row key={index}>
                <Table.Cell>{log.log_level}</Table.Cell>
                <Table.Cell>{log.message}</Table.Cell>
                <Table.Cell>{log.timestamp}</Table.Cell>
              </Table.Row>
            ))}
          </Table.Body>
        </Table>
        <Pagination
          activePage={activePage}
          totalPages={totalPages}
          onPageChange={(e, { activePage = 1 }) =>
            handlePageChange(e, { activePage })
          }
        />
      </div>
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
