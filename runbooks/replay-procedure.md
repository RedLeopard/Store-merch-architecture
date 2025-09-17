# Replay Procedure
1. Identify time window & partitions in Kafka.
2. Copy events to `*.replay` topic; consumers read with `replay=true` header.
3. Verify idempotent upserts in projections; reconcile counts.
