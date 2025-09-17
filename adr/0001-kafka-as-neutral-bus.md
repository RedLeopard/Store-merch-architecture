# ADR-0001: Kafka as Neutral Event Bus

## Context
We need producer/consumer decoupling across Azure and GCP without locking into Event Grid or Pub/Sub.

## Decision
Use Confluent Cloud (Kafka) with Schema Registry and DLQs. It’s provider-neutral and portable.

## Consequences
Slight added cost and another vendor, but simpler multi-cloud and rich ecosystem (connectors, tooling).
