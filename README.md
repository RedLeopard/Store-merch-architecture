# Costco Merchandising Multi-Cloud Architecture

## Overview
This project explores a multi-cloud solution for synchronizing price and inventory across Costco’s merchandising systems.  
The architecture uses Azure and Google Cloud Platform (GCP) together with Kafka (Confluent Cloud) to provide reliable, real-time updates while maintaining auditability, scalability, and security.

<img width="4828" height="584" alt="Image" src="https://github.com/user-attachments/assets/52779285-517d-4785-8238-ae4a98f8808f" />

```mermaid
flowchart LR
    sor[(System of Record<br/>(ERP, Merch DB))] --> normalizer[Normalizer<br/>(GCP Cloud Run)]
    normalizer --> kafka((Event Bus<br/>(Confluent Kafka)))
    kafka --> consumer[Consumer<br/>(Azure Function)]
    consumer --> cosmos[(Cosmos DB<br/>(Projections))]
    cosmos --> apim[API Management]
    apim --> apps((Downstream Apps<br/>Web, Mobile, POS))

    kafka --> bq[(Audit Store<br/>(BigQuery))]
    consumer --> bq
    bq -.-> consumer

    normalizer -.-> monitor[Observability<br/>(Azure Monitor, Grafana)]
    consumer -.-> monitor
    kafka -.-> monitor


## Goals
- Real-time propagation of price and inventory changes  
- Immutable audit logs with replay support  
- Multi-cloud alignment with Azure + GCP  
- Resilient design meeting availability, scalability, security, and cost requirements  

## Architecture
- **Producers (GCP):** Cloud Run services normalize and publish events  
- **Event Backbone:** Confluent Cloud Kafka with schema registry, DLQs, and replay topics  
- **Consumers (Azure):** Azure Functions process events and update Cosmos DB projections  
- **Audit & Analytics:** BigQuery provides immutable event logs and analytics  
- **Security:** TLS in transit, KMS encryption at rest, least-privilege IAM roles, workload identity federation  

## Repository Layout
- diagrams/ — Context, logical, and sequence diagrams  
- adr/ — Architecture decision records  
- iac/ — Terraform stubs for infrastructure (safe: not applied by default)  
- services/ — Example producer/consumer services  
- runbooks/ — Operational guides (failover, replay, incident handling)  
- security/ — IAM and key management notes  
- samples/ — Example price/inventory payloads  

## Architecture Decisions
- ADR-0001: Kafka selected as neutral event bus across Azure + GCP  
- ADR-0002: Cosmos DB chosen for read projections in Azure  
- ADR-0003: BigQuery used as the audit log and analytics store  

## Cost Considerations
The design minimizes costs by relying on managed, serverless services:  
- Local setup runs free with Docker + SQLite  
- Trial credits cover light deployments in Azure/GCP  
- All cloud resources should be removed immediately after testing  

## Runbooks
- Disaster Recovery / Failover steps  
- Event replay procedure  
- Incident response checklist  
