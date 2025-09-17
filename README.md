# Merchandising Multi‑Cloud Harmonization (GCP + Azure) — Interview Project

**Goal:** Show an *architecture-first* solution for near‑real‑time price & inventory sync across channels/countries with auditability, governance, and DR — using *portable* components that fit Costco’s multi‑cloud (GCP + Azure) direction.

> This repo is interview‑ready and cost‑safe: you can demo locally with Docker (no cloud spend), or optionally light‑touch in cloud and then **tear down** immediately.

## Contents
- `diagrams/` — Mermaid diagrams (context, logical, sequence)
- `adr/` — Architecture Decision Records
- `iac/` — Terraform stubs (no apply by default)
- `services/` — Mock services (no cloud deps)
- `runbooks/` — DR, replay, incident checklists
- `security/` — IAM & key‑management guidelines
- `samples/` — Example events & API payloads

## Demo Paths
1) **Local-Only (FREE):** Dockerized Redpanda (Kafka‑compatible) + FastAPI normalizer + Python consumer + SQLite (as Cosmos proxy).2) **Screenshot-Only (FREE):** Use diagrams + curl to local mocks; talk through ops & DR.
3) **Lite Cloud (Trial Credits):** Create 1 topic in Confluent Cloud and a serverless function in Azure or Cloud Run in GCP; publish 1 event; **delete immediately**.

See `runbooks/demo-playbook.md`.
