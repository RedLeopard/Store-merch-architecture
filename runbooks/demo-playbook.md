# Demo Playbook (Pick ONE path)

## A) Local-Only (FREE)
- Run `docker compose up` (Redpanda, normalizer, consumer).
- `curl -X POST http://localhost:8080/price-change -d @samples/price-change.json`
- Show consumer log and SQLite row created; run the sample query.

## B) Screenshot-Only (FREE)
- Open `diagrams/*.mmd` in GitHub preview.
- Run the curl to local mock; show logs; talk through sequence.

## C) Lite Cloud (Trial Credits; TEAR DOWN)
- Create a single Kafka topic in Confluent Cloud (free tier if available).
- Deploy one Azure Function (Consumption) **or** one GCP Cloud Run service.
- Publish one event; show it in the console; **delete resources immediately**.
