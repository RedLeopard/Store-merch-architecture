# DR / Failover Runbook (Condensed)
1. Verify backbone health (Kafka lag, DLQ size == 0).
2. If region outage: switch traffic for Functions/API via traffic manager.
3. Promote consumer in secondary region; validate lag < threshold.
4. Run synthetic checks (price GET) and record timestamps.
5. Post-incident: replay from Kafka for the impacted window.
