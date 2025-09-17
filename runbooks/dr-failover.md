# Disaster Recovery / Failover Runbook

1. Verify backbone health (Kafka lag, DLQ size == 0).  
2. If a region outage occurs, switch traffic for Functions/API via traffic manager.  
3. Promote consumer in secondary region and validate lag.  
4. Run synthetic checks (price GET) and record timestamps.  
5. Replay missing events from Kafka if required.  
