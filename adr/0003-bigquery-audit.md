# ADR-0003: Immutable Audit in BigQuery

## Context
Analytics and compliance require tamper-proof event logs.

## Decision
Stream events to partitioned tables in BigQuery for audit and BI.

## Consequences
Analytics centralized in GCP, but data is portable and cost-effective at scale.
