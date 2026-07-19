# HistoraGraph-AI Project Context Document

> **Vietnam Modern History Knowledge Graph Explorer**
> An AI-powered historical knowledge platform using Knowledge Graphs, Hybrid GraphRAG, and Large Language Models.

---

## Project Overview

### Project Description

**Vietnam Modern History Knowledge Graph Explorer** là một nền tảng web ứng dụng AI, giúp người dùng khám phá và tìm hiểu lịch sử Việt Nam hiện đại giai đoạn **1945–1975** thông qua mô hình tri thức có cấu trúc kết hợp với Generative AI.

Dự án tập trung xây dựng một **AI-powered Knowledge Exploration Platform**, trong đó dữ liệu lịch sử được:

- Thu thập từ các nguồn có xuất xứ rõ ràng.
- Chuẩn hóa và xử lý thành tài liệu có cấu trúc.
- Trích xuất thực thể và quan hệ lịch sử.
- Xây dựng thành Knowledge Graph.
- Kết hợp với Vector Database để phục vụ hệ thống Hybrid GraphRAG.

Hệ thống cho phép người dùng:

- Khám phá các sự kiện lịch sử.
- Quan sát mối quan hệ giữa các thực thể.
- Tìm hiểu dòng thời gian lịch sử.
- Đặt câu hỏi với AI Historical Assistant.
- Nhận câu trả lời có ngữ cảnh và nguồn tham khảo.

Dự án không hướng tới xây dựng một chatbot lịch sử đơn thuần. Mục tiêu là tổ chức, liên kết, khám phá và giải thích tri thức lịch sử dựa trên dữ liệu có cấu trúc cùng nguồn tham khảo minh bạch.

## Problem Definition

Thông tin lịch sử hiện nay thường tồn tại dưới dạng văn bản riêng lẻ, tài liệu PDF dài, website lưu trữ, timeline cố định và các nguồn dữ liệu chưa được liên kết. Điều này gây khó khăn cho người dùng khi:

- Hiểu mối quan hệ nguyên nhân – kết quả giữa các sự kiện.
- Theo dõi diễn biến của một giai đoạn lịch sử.
- Khám phá liên hệ giữa nhân vật, tổ chức và sự kiện.
- Tổng hợp thông tin từ nhiều nguồn khác nhau.

Việc dùng trực tiếp Large Language Model để hỏi đáp lịch sử cũng tiềm ẩn các vấn đề:

- Hallucination.
- Không đảm bảo nguồn thông tin.
- Không thể hiện cấu trúc tri thức phía sau câu trả lời.

Vì vậy, hệ thống kết hợp các thành phần sau để tạo câu trả lời có thể giải thích và truy xuất nguồn gốc:

```text
Reliable Historical Data
          +
Knowledge Graph
          +
Vector Retrieval
          +
Large Language Model
          +
Source Citation
```

## Project Objectives

### Main Objective

Xây dựng một nền tảng AI giúp người dùng khám phá lịch sử Việt Nam hiện đại giai đoạn 1945–1975 dựa trên Knowledge Graph và Hybrid GraphRAG.

### Technical Objectives

**Data Engineering**

- Thu thập dữ liệu lịch sử từ các nguồn đáng tin cậy.
- Xây dựng pipeline xử lý dữ liệu.
- Chuẩn hóa văn bản và metadata.
- Lưu trữ tài liệu phục vụ truy xuất.

**Knowledge Engineering**

- Thiết kế ontology cho lĩnh vực lịch sử.
- Xây dựng Knowledge Graph.
- Mô hình hóa quan hệ giữa các thực thể.
- Sử dụng LLM hỗ trợ trích xuất entity và relationship.

**Generative AI Engineering**

- Xây dựng hệ thống Hybrid GraphRAG.
- Kết hợp Graph Retrieval, Vector Retrieval và LLM Generation.
- Áp dụng Prompt Engineering.
- Điều chỉnh câu trả lời theo nhóm người dùng.

**Software Engineering**

- Xây dựng web application hoàn chỉnh.
- Thiết kế backend API.
- Xây dựng giao diện khám phá tri thức.
- Triển khai hệ thống bằng Docker.
- Hỗ trợ cloud deployment.

## Project Scope

### Historical Domain

Phạm vi dữ liệu tập trung vào **lịch sử Việt Nam hiện đại, giai đoạn 1945–1975**.

Các chủ đề chính gồm:

- Cách mạng tháng Tám năm 1945.
- Thành lập nước Việt Nam Dân chủ Cộng hòa.
- Kháng chiến chống Pháp.
- Chiến dịch Điện Biên Phủ.
- Hiệp định Genève năm 1954.
- Quan hệ quốc tế liên quan đến Việt Nam.
- Chiến tranh Việt Nam.
- Hiệp định Paris năm 1973.
- Sự kiện thống nhất đất nước năm 1975.

### Dataset Scope

Do giới hạn thời gian triển khai, hệ thống không hướng tới xây dựng toàn bộ cơ sở dữ liệu lịch sử Việt Nam. Thay vào đó, dự án tạo một **Historical Knowledge Base Prototype** với phạm vi dự kiến:

| Thành phần | Quy mô | Ghi chú |
| --- | ---: | --- |
| Events | 100–200 | Sự kiện lịch sử |
| Entities | 500–1.000 | Person, Organization, Location, Document và Event |

## Data Source Strategy

### Data Requirements

Dữ liệu sử dụng phải có:

- Nguồn gốc rõ ràng.
- Metadata đầy đủ.
- Khả năng truy xuất nguồn tham khảo.
- Thông tin thời gian và không gian.

### Primary Data Sources

**Vietnamese Historical Sources**

Ưu tiên các nguồn như:

- Thư viện Quốc gia.
- Trung tâm Lưu trữ Quốc gia.
- Kho văn kiện lịch sử.
- Các tổ chức nghiên cứu lịch sử.

**International Historical Archives**

Ví dụ:

- National Archives.
- Library of Congress.
- US Department of State Historical Documents.
- French digital archives.

Các nguồn này có thể cung cấp văn kiện, báo cáo, hình ảnh và tài liệu nghiên cứu.

### Supporting Knowledge Sources

**Wikidata**

Sử dụng cho entity identification, standard ID và metadata enrichment.

**Wikipedia**

Chỉ sử dụng cho discovery và bổ sung thông tin tham khảo; không dùng Wikipedia làm nguồn tri thức chính.

## Data Processing Pipeline

```text
Historical Data Sources
          │
          ▼
Data Collection (Crawler / API)
          │
          ▼
Document Processing
  ├─ Cleaning
  ├─ Parsing
  └─ Metadata Extraction
          │
          ▼
LLM-assisted Information Extraction
  ├─ Entity Extraction
  └─ Relationship Extraction
          │
          ▼
Knowledge Graph Construction
          │
    ┌─────┴─────┐
    ▼           ▼
  Neo4j     Vector Database
    └─────┬─────┘
          ▼
   Hybrid GraphRAG
          │
          ▼
     LLM Generation
          │
          ▼
   Answer + Citation
```

## Knowledge Graph Design

### Entity Types

| Entity type | Ví dụ |
| --- | --- |
| Event | Cách mạng tháng Tám, Chiến dịch Điện Biên Phủ, Hiệp định Paris |
| Person | Hồ Chí Minh, Võ Nguyên Giáp, các nhân vật ngoại giao |
| Organization | Chính phủ VNDCCH, Việt Minh, các tổ chức quốc tế |
| Location | Hà Nội, Điện Biên Phủ, Genève |
| Document | Hiệp định, văn kiện, báo cáo |

### Relationship Types

| Nguồn | Quan hệ | Đích |
| --- | --- | --- |
| Person | `COMMANDS` | Event |
| Person | `PARTICIPATED_IN` | Event |
| Event | `CAUSES` | Event |
| Event | `OCCURRED_AT` | Location |
| Document | `DESCRIBES` | Event |
| Event | `FOLLOWED_BY` | Event |

## System Architecture

```text
Frontend: React / Next.js
          │
          ▼
Backend: FastAPI
          │
          ▼
AI Service Layer
  ├─ Question Understanding
  ├─ Entity Linking
  ├─ Graph Retrieval
  ├─ Vector Retrieval
  ├─ Prompt Engineering
  └─ Response Generation
          │
          ▼
Data Layer
  ├─ PostgreSQL
  ├─ Neo4j
  └─ Vector Database
          │
          ▼
External AI: OpenAI API / Gemini API / Claude API
```

## Core User Features

### Knowledge Graph Explorer

Người dùng có thể:

- Tìm kiếm thực thể lịch sử.
- Xem các quan hệ liên quan.
- Mở rộng Knowledge Graph.
- Khám phá mạng lưới lịch sử.

Ví dụ luồng khám phá: **Điện Biên Phủ → Hiệp định Genève → Việt Nam sau 1954 → Chiến tranh Việt Nam**.

### AI Historical Assistant

Người dùng có thể đặt các câu hỏi lịch sử, chẳng hạn:

> “Vì sao chiến dịch Điện Biên Phủ dẫn tới Hiệp định Genève?”

Luồng xử lý:

```text
Question → Entity Detection → Graph Retrieval → Vector Retrieval
         → Context Combination → LLM Generation → Answer + Citation
```

### Adaptive AI Explanation

Hệ thống hỗ trợ các chế độ giải thích:

| Chế độ | Đặc điểm |
| --- | --- |
| Student Mode | Ngôn ngữ đơn giản, giải thích cơ bản, có ví dụ |
| General Mode | Cân bằng giữa dễ hiểu và chuyên sâu |
| Research Mode | Phân tích sâu, kèm nhiều nguồn tham khảo |

### Timeline Explorer

- Xem lịch sử theo thời gian.
- Sinh timeline theo câu hỏi.
- Liên kết timeline với Knowledge Graph.

### Source Explorer

Mỗi câu trả lời AI bao gồm nguồn dữ liệu, văn bản liên quan, metadata và citation. Mục tiêu là tăng tính minh bạch, khả năng kiểm chứng và giảm hallucination.

## AI Technologies

### Large Language Models

Hệ thống có thể sử dụng OpenAI API, Gemini API hoặc Claude API. Dự án không thực hiện fine-tuning.

### Retrieval-Augmented Generation

RAG cung cấp context chính xác và giảm sự phụ thuộc vào kiến thức pretrained của mô hình.

### Hybrid GraphRAG

Hybrid GraphRAG kết hợp **Knowledge Graph + Vector Retrieval + LLM**, hỗ trợ:

- Multi-hop reasoning.
- Relationship exploration.
- Context-aware answering.

### Prompt Engineering

Prompt được điều chỉnh theo user mode, answer style, explanation depth và citation format.

## Evaluation Plan

### Retrieval Evaluation

Đánh giá bằng các chỉ số: Precision@K, Recall@K và MRR.

### RAG Evaluation

So sánh baseline **Question → LLM → Answer** với phương án đề xuất **Question → Hybrid GraphRAG → LLM → Answer**.

Các tiêu chí đánh giá:

- Answer relevance.
- Faithfulness.
- Citation correctness.

### System Evaluation

Theo dõi response latency, token usage và API cost.

### User Evaluation

Đánh giá mức độ dễ hiểu, độ hữu ích và độ tin cậy.

## Technology Stack

| Layer | Technologies |
| --- | --- |
| Frontend | React / Next.js, TypeScript, Tailwind CSS, Cytoscape.js |
| Backend | FastAPI, Python, PostgreSQL, SQLAlchemy, JWT Authentication |
| AI / Data | LangChain hoặc LlamaIndex, Neo4j, Qdrant / ChromaDB, OpenAI API, Gemini API |
| Deployment | Docker, Docker Compose, Cloud Platform (optional) |

## Expected Outcome

Sản phẩm cuối cùng là một AI-powered Historical Knowledge Platform có khả năng:

- Thu thập và quản lý dữ liệu lịch sử.
- Xây dựng Knowledge Graph.
- Trực quan hóa mạng lưới tri thức.
- Trả lời câu hỏi dựa trên dữ liệu truy xuất.
- Cung cấp nguồn tham khảo.
- Hỗ trợ người dùng khám phá lịch sử.

Dự án thể hiện các kỹ năng: Fullstack Development, Data Engineering, Knowledge Graph Engineering, Generative AI Application Development, RAG / Hybrid GraphRAG và AI System Evaluation.

## Project Positioning

Dự án không được định vị là:

> “Một chatbot lịch sử sử dụng GPT API.”

Mà là:

> “Một AI-powered Knowledge Exploration Platform sử dụng Knowledge Graph và Hybrid GraphRAG để tổ chức, khám phá và giải thích tri thức lịch sử Việt Nam dựa trên dữ liệu có nguồn gốc minh bạch.”

Tài liệu này là **tài liệu gốc xuyên suốt dự án**. Các quyết định về database, folder structure, roadmap, report và implementation nên bám theo tài liệu này để tránh scope creep.
