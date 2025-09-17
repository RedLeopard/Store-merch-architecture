# ADR-0003: Immutable Audit in BigQuery

## Context
Cheap analytics + long-term audit for all committed events.

## Decision
Stream events to partitioned tables in BigQuery for audit and BI; exportable to other lakes if needed.

## Consequences
Analytics lives in GCP, but data is portable and schematized; costs managed via partitioning/TTL.
