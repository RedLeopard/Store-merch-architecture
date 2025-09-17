# Replay Procedure

1. Identify affected time window in Kafka topics.  
2. Copy events to a replay topic; consumers read with replay flag.  
3. Validate projections after replay and reconcile counts.  
