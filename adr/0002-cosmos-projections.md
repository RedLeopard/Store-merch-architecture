# ADR-0002: Cosmos DB Read Projections

## Context
Downstream apps need fast reads of current price and inventory in Azure.

## Decision
Maintain read-optimized projections in Cosmos DB (per item/location) built from events.

## Consequences
Eventual consistency but scalable reads and easy rebuilds from Kafka events.
