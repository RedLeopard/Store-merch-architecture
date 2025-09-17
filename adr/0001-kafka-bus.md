# ADR-0001: Kafka as Neutral Event Bus

## Context
We need producer/consumer decoupling across Azure and GCP without relying on cloud-specific pub/sub services.

## Decision
Use Confluent Cloud (Kafka) with Schema Registry and DLQs. This ensures multi-cloud portability.

## Consequences
Adds cost and another vendor, but simplifies integration and provides mature tooling.
