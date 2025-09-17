# ADR-0002: Cosmos DB Read Projections

## Context
Downstream apps need fast reads of current price/inventory in Azure regions.

## Decision
Maintain read-optimized projections in Cosmos DB (per item/location) built from events.

## Consequences
Eventual consistency, but simple, scalable reads and easy replay from Kafka for rebuilds.
