Costco Merchandising Multi-Cloud Architecture
Overview
This project demonstrates a solution architecture for Costco’s Merchandising domain, focusing on how to keep price and inventory synchronized across channels and regions. The design leverages Azure and GCP together with an event-driven backbone to ensure real-time updates, auditability, disaster recovery, and cost efficiency.
I built this repo to showcase how I approach architecture problems as a Solutions Architect: starting with the business challenge, designing the target state, capturing trade-offs in Architecture Decision Records (ADRs), and providing runbooks, security guidance, and cost considerations.
Goals
Ensure real-time propagation of price and inventory updates across multiple channels (stores, e-commerce, mobile).
Provide auditability with an immutable event log and replay capabilities.
Align with a multi-cloud direction (Azure + GCP) using portable, standards-based components.
Meet non-functional requirements for availability, scalability, security, and cost control.
Deliver a demo-ready solution that can be shown locally (no spend) or lightly in cloud trials.
Repo Contents
diagrams/ — Context, Logical, and Sequence diagrams (Mermaid).
adr/ — Architecture Decision Records documenting trade-offs.
iac/ — Terraform stubs (safe: no resources created until uncommented).
services/ — Lightweight mock services to simulate producers/consumers.
runbooks/ — Disaster recovery, replay, and incident response playbooks.
security/ — IAM and key-management guidelines.
samples/ — Example price/inventory payloads.
Demo Options
Local (FREE) → Run everything locally with Docker. Publish sample events, watch consumers update projections, and query results.
Screenshot Walkthrough (FREE) → Use the diagrams and runbooks to walk through the architecture, governance, and DR strategy.
Lite Cloud (Trial Credits) → Deploy a single Kafka topic (Confluent free tier) and one Function (Azure/GCP). Publish an event, show it flows, then tear down immediately.
See runbooks/demo-playbook.md for step-by-step instructions.
Why This Matters for Costco
Directly addresses Merchandising needs: price accuracy, inventory visibility, fewer manual errors.
Showcases multi-cloud design leadership across Azure and GCP.
Demonstrates governance, security, and DR practices that scale at enterprise level.
Provides a concrete, interview-ready artifact I can discuss in detail.


See `runbooks/demo-playbook.md`.
