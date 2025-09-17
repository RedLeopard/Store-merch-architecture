# 🏬 Costco Merchandising Multi-Cloud Architecture

![Architecture](https://img.shields.io/badge/Role-Solutions%20Architect-blueviolet?style=for-the-badge)
![Cloud](https://img.shields.io/badge/Multi--Cloud-Azure%20%7C%20GCP-00aaff?style=for-the-badge)
![Focus](https://img.shields.io/badge/Domain-Merchandising-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Demo-Ready-brightgreen?style=for-the-badge)

---

## 📖 Overview
This project demonstrates a **solution architecture** for **Costco’s Merchandising domain**, tackling the challenge of keeping **price and inventory synchronized across channels and regions**.  
The design leverages **Azure + GCP** together with an **event-driven backbone** to ensure **real-time updates**, **auditability**, **disaster recovery**, and **cost efficiency**.

I built this repo to highlight how I approach **architecture challenges** as a Solutions Architect:  
👉 Start with the business problem → design the target state → capture trade-offs in ADRs → deliver with governance, security, and DR in mind.

---

## 🎯 Goals
- ⚡ **Real-time propagation** of price & inventory changes across stores, e-commerce, and mobile  
- 🗂️ **Auditability & replay** with an immutable event log  
- ☁️ **Multi-cloud alignment** (Azure + GCP) using portable, standards-based components  
- 🔒 **Non-functional excellence**: availability, scalability, security, and cost control  
- 🛠️ **Demo-ready**: works locally (no spend) or lightly in cloud trials  

---

## 📂 Repo Contents
- 📊 **`diagrams/`** — Context, Logical, and Sequence diagrams (Mermaid)  
- 📜 **`adr/`** — Architecture Decision Records  
- 🏗️ **`iac/`** — Terraform stubs (safe: no apply by default)  
- 🔧 **`services/`** — Mock producer/consumer services  
- 📑 **`runbooks/`** — DR, replay, and incident response guides  
- 🔐 **`security/`** — IAM and key-management guidelines  
- 🧾 **`samples/`** — Example price/inventory payloads  

---

## 🚀 Demo Options
1. **Local (FREE)** → Run with Docker, publish sample events, and query results  
2. **Screenshot Walkthrough (FREE)** → Use diagrams + runbooks to explain governance & DR strategy  
3. **Lite Cloud (Trial Credits)** → Deploy one Kafka topic + one Function (Azure/GCP), publish an event, then **tear down immediately**  

👉 See **[`runbooks/demo-playbook.md`](runbooks/demo-playbook.md)** for full step-by-step instructions  

---

## 💡 Why This Matters for Costco
- 🏬 Directly addresses **Merchandising pain points**: price accuracy & inventory visibility  
- 🌐 Showcases **multi-cloud leadership** across Azure + GCP  
- 🔒 Demonstrates **governance, security, and DR practices** at enterprise scale  
- 🧑‍💼 Provides a **concrete, interview-ready artifact** for discussion  

---

## 👤 Author
**Edward Thornton**  
AWS Certified Solutions Architect – Professional   

---
