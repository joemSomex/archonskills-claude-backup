#!/usr/bin/env node

const baseUrl = process.argv[2];
const path = process.argv[3] || "/";
const concurrency = Number(process.argv[4] || 10);
const durationMs = Number(process.argv[5] || 5000);

if (!baseUrl || !Number.isSafeInteger(concurrency) || concurrency < 1 || !Number.isFinite(durationMs) || durationMs < 100) {
  console.error("usage: http-load.mjs <base-url> [path=/] [concurrency=10] [duration-ms=5000]");
  process.exit(2);
}

const user = process.env.BASIC_AUTH_USERNAME || process.env.STAGING_ACCESS_USERNAME;
const pass = process.env.BASIC_AUTH_PASSWORD || process.env.STAGING_ACCESS_PASSWORD;
const headers = user && pass
  ? { Authorization: `Basic ${Buffer.from(`${user}:${pass}`).toString("base64")}` }
  : {};
const stopAt = performance.now() + durationMs;
const latencies = [];
const statuses = new Map();
let bytes = 0;
let errors = 0;

async function worker() {
  while (performance.now() < stopAt) {
    const started = performance.now();
    try {
      const response = await fetch(`${baseUrl}${path}`, {
        headers,
        redirect: "manual",
        signal: AbortSignal.timeout(10000),
      });
      const body = await response.arrayBuffer();
      latencies.push(performance.now() - started);
      statuses.set(response.status, (statuses.get(response.status) || 0) + 1);
      bytes += body.byteLength;
    } catch {
      errors += 1;
      latencies.push(performance.now() - started);
    }
  }
}

const wallStarted = performance.now();
await Promise.all(Array.from({ length: concurrency }, worker));
const wallMs = performance.now() - wallStarted;
latencies.sort((a, b) => a - b);
const percentile = (p) => latencies.length
  ? latencies[Math.min(latencies.length - 1, Math.floor((latencies.length - 1) * p))]
  : null;
const rounded = (value) => value === null ? null : Math.round(value);

console.log(JSON.stringify({
  target: baseUrl,
  path,
  concurrency,
  duration_ms: Math.round(wallMs),
  requests: latencies.length,
  requests_per_second: Number((latencies.length / (wallMs / 1000)).toFixed(1)),
  errors,
  statuses: Object.fromEntries([...statuses.entries()].sort(([a], [b]) => a - b)),
  latency_ms: {
    p50: rounded(percentile(0.50)),
    p95: rounded(percentile(0.95)),
    p99: rounded(percentile(0.99)),
    max: latencies.length ? Math.round(latencies.at(-1)) : null,
  },
  response_mib_per_second: Number((bytes / 1048576 / (wallMs / 1000)).toFixed(2)),
}));
