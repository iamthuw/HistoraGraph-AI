\# Project Context Document (PCD)



\# Vietnam Modern History Knowledge Graph Explorer



\## AI-powered Historical Knowledge Platform using Knowledge Graph, Hybrid GraphRAG and Large Language Models



\---



\# 1. Project Overview



\## 1.1 Project Description



\*\*Vietnam Modern History Knowledge Graph Explorer\*\* là một nền tảng web ứng dụng AI nhằm hỗ trợ người dùng khám phá và tìm hiểu lịch sử Việt Nam hiện đại giai đoạn \*\*1945–1975\*\* thông qua mô hình tri thức có cấu trúc kết hợp với công nghệ Generative AI.



Dự án tập trung xây dựng một \*\*AI-powered Knowledge Exploration Platform\*\*, trong đó dữ liệu lịch sử được:



\* Thu thập từ các nguồn dữ liệu có nguồn gốc rõ ràng.

\* Chuẩn hóa và xử lý thành các tài liệu có cấu trúc.

\* Trích xuất thực thể và quan hệ lịch sử.

\* Xây dựng thành Knowledge Graph.

\* Kết hợp với Vector Database để phục vụ hệ thống Hybrid GraphRAG.



Hệ thống cho phép người dùng:



\* Khám phá các sự kiện lịch sử.

\* Quan sát mối quan hệ giữa các thực thể.

\* Tìm hiểu dòng thời gian lịch sử.

\* Đặt câu hỏi với AI Historical Assistant.

\* Nhận câu trả lời có ngữ cảnh và nguồn tham khảo.



Dự án không định hướng xây dựng một chatbot lịch sử đơn thuần.



Mục tiêu chính là xây dựng một nền tảng AI có khả năng:



> Tổ chức, liên kết, khám phá và giải thích tri thức lịch sử dựa trên dữ liệu có cấu trúc và nguồn tham khảo minh bạch.



\---



\# 2. Problem Definition



Các nguồn thông tin lịch sử hiện nay thường tồn tại dưới dạng:



\* Văn bản riêng lẻ.

\* Tài liệu PDF dài.

\* Website lưu trữ thông tin.

\* Timeline cố định.

\* Các nguồn dữ liệu chưa được liên kết.



Điều này gây khó khăn cho người dùng trong việc:



\* Hiểu mối quan hệ nguyên nhân - kết quả giữa các sự kiện.

\* Theo dõi sự phát triển của một giai đoạn lịch sử.

\* Khám phá mối liên hệ giữa nhân vật, tổ chức và sự kiện.

\* Tổng hợp thông tin từ nhiều nguồn khác nhau.



Ngoài ra, việc sử dụng trực tiếp Large Language Model để hỏi đáp lịch sử tồn tại các vấn đề:



\* Hallucination.

\* Không đảm bảo nguồn thông tin.

\* Không thể hiện được cấu trúc tri thức phía sau câu trả lời.



Do đó, dự án xây dựng hệ thống kết hợp:



```

Reliable Historical Data



&#x20;       +



Knowledge Graph



&#x20;       +



Vector Retrieval



&#x20;       +



Large Language Model



&#x20;       +



Source Citation

```



nhằm tạo ra hệ thống AI có khả năng giải thích và truy xuất tri thức minh bạch.



\---



\# 3. Project Objectives



\## 3.1 Main Objective



Xây dựng một nền tảng AI giúp người dùng khám phá lịch sử Việt Nam hiện đại giai đoạn 1945–1975 dựa trên Knowledge Graph và Hybrid GraphRAG.



\---



\# 3.2 Technical Objectives



\## Data Engineering



\* Thu thập dữ liệu lịch sử từ các nguồn đáng tin cậy.

\* Xây dựng pipeline xử lý dữ liệu.

\* Chuẩn hóa văn bản và metadata.

\* Lưu trữ tài liệu phục vụ truy xuất.



\## Knowledge Engineering



\* Thiết kế ontology cho lĩnh vực lịch sử.

\* Xây dựng Knowledge Graph.

\* Mô hình hóa quan hệ giữa các thực thể.

\* Sử dụng LLM hỗ trợ trích xuất entity và relationship.



\## Generative AI Engineering



\* Xây dựng hệ thống Hybrid GraphRAG.



\* Kết hợp:



&#x20; \* Graph Retrieval.

&#x20; \* Vector Retrieval.

&#x20; \* LLM Generation.



\* Áp dụng Prompt Engineering.



\* Điều chỉnh câu trả lời theo nhóm người dùng.



\## Software Engineering



\* Xây dựng web application hoàn chỉnh.

\* Thiết kế backend API.

\* Xây dựng giao diện khám phá tri thức.

\* Triển khai hệ thống bằng Docker.

\* Hỗ trợ deployment cloud.



\---



\# 4. Project Scope



\## 4.1 Historical Domain



Phạm vi dữ liệu:



```

Vietnam Modern History



1945 - 1975

```



Các chủ đề chính:



\* Cách mạng tháng Tám 1945.

\* Thành lập nước Việt Nam Dân chủ Cộng hòa.

\* Kháng chiến chống Pháp.

\* Chiến dịch Điện Biên Phủ.

\* Hiệp định Genève 1954.

\* Quan hệ quốc tế liên quan đến Việt Nam.

\* Chiến tranh Việt Nam.

\* Hiệp định Paris 1973.

\* Sự kiện thống nhất đất nước 1975.



\---



\# 4.2 Dataset Scope



Do giới hạn thời gian triển khai, hệ thống không hướng tới xây dựng toàn bộ cơ sở dữ liệu lịch sử Việt Nam.



Mục tiêu:



\## Historical Knowledge Base Prototype



Bao gồm:



\### Events



Khoảng:



\* 100–200 sự kiện lịch sử.



\### Entities



Khoảng:



\* 500–1000 thực thể.



Bao gồm:



\* Person.

\* Organization.

\* Location.

\* Document.

\* Event.



\---



\# 5. Data Source Strategy



\## 5.1 Data Requirements



Dữ liệu sử dụng phải:



\* Có nguồn gốc rõ ràng.

\* Có metadata.

\* Có khả năng truy xuất nguồn tham khảo.

\* Có thông tin thời gian và không gian.



\---



\# 5.2 Primary Data Sources



Ưu tiên các nguồn:



\## Vietnamese Historical Sources



Ví dụ:



\* Thư viện quốc gia.

\* Trung tâm lưu trữ quốc gia.

\* Kho văn kiện lịch sử.

\* Các tổ chức nghiên cứu lịch sử.



\## International Historical Archives



Ví dụ:



\* National Archives.

\* Library of Congress.

\* US Department of State Historical Documents.

\* French digital archives.



Các nguồn này cung cấp:



\* Văn kiện.

\* Báo cáo.

\* Hình ảnh.

\* Tài liệu nghiên cứu.



\---



\# 5.3 Supporting Knowledge Sources



\## Wikidata



Sử dụng cho:



\* Entity identification.

\* Standard ID.

\* Metadata enrichment.



\## Wikipedia



Chỉ sử dụng cho:



\* Discovery.

\* Bổ sung thông tin tham khảo.



Không sử dụng Wikipedia làm nguồn tri thức chính.



\---



\# 6. Data Processing Pipeline



Pipeline tổng thể:



```

Historical Data Sources



&#x20;         |



&#x20;         v



Data Collection



(Crawler/API)



&#x20;         |



&#x20;         v



Document Processing



Cleaning

Parsing

Metadata extraction



&#x20;         |



&#x20;         v



LLM-assisted Information Extraction



Entity Extraction



Relationship Extraction



&#x20;         |



&#x20;         v



Knowledge Graph Construction





&#x20;         |



&#x20;    ----------------



&#x20;    |              |



&#x20;    v              v





&#x20;Neo4j          Vector DB



Graph Store     Embeddings





&#x20;    |              |



&#x20;    ----------------



&#x20;            |



&#x20;            v



&#x20;      Hybrid GraphRAG



&#x20;            |



&#x20;            v



&#x20;           LLM



&#x20;            |



&#x20;            v



&#x20;    Answer + Citation

```



\---



\# 7. Knowledge Graph Design



\## 7.1 Entity Types



\### Event



Ví dụ:



\* Cách mạng tháng Tám.

\* Chiến dịch Điện Biên Phủ.

\* Hiệp định Paris.



\### Person



Ví dụ:



\* Hồ Chí Minh.

\* Võ Nguyên Giáp.

\* Các nhân vật ngoại giao.



\### Organization



Ví dụ:



\* Chính phủ VNDCCH.

\* Việt Minh.

\* Các tổ chức quốc tế.



\### Location



Ví dụ:



\* Hà Nội.

\* Điện Biên Phủ.

\* Genève.



\### Document



Ví dụ:



\* Hiệp định.

\* Văn kiện.

\* Báo cáo.



\---



\# 7.2 Relationship Types



Ví dụ:



```

Person



COMMANDS



Event

```



```

Person



PARTICIPATED\_IN



Event

```



```

Event



CAUSES



Event

```



```

Event



OCCURRED\_AT



Location

```



```

Document



DESCRIBES



Event

```



```

Event



FOLLOWED\_BY



Event

```



\---



\# 8. System Architecture



```

&#x20;                Frontend



&#x20;             React / Next.js



&#x20;                   |



&#x20;                   |



&#x20;                Backend



&#x20;                FastAPI



&#x20;                   |



&#x20;       --------------------------------





&#x20;             AI Service Layer





&#x20;       Question Understanding



&#x20;       Entity Linking



&#x20;       Graph Retrieval



&#x20;       Vector Retrieval



&#x20;       Prompt Engineering



&#x20;       Response Generation





&#x20;       --------------------------------





&#x20;             Data Layer





&#x20;       PostgreSQL



&#x20;       Neo4j



&#x20;       Vector Database





&#x20;       --------------------------------





&#x20;             External AI





&#x20;       OpenAI API



&#x20;       Gemini API



&#x20;       Claude API



```



\---



\# 9. Core User Features



\# 9.1 Knowledge Graph Explorer



Người dùng có thể:



\* Tìm kiếm thực thể lịch sử.

\* Xem các quan hệ liên quan.

\* Mở rộng knowledge graph.

\* Khám phá mạng lưới lịch sử.



Ví dụ:



```

Điện Biên Phủ



&#x20;     |



Hiệp định Genève



&#x20;     |



Việt Nam sau 1954



&#x20;     |



Chiến tranh Việt Nam

```



\---



\# 9.2 AI Historical Assistant



Người dùng đặt câu hỏi lịch sử.



Ví dụ:



> "Vì sao chiến dịch Điện Biên Phủ dẫn tới Hiệp định Genève?"



Pipeline:



```

Question



↓



Entity Detection



↓



Graph Retrieval



↓



Vector Retrieval



↓



Context Combination



↓



LLM Generation



↓



Answer + Citation

```



\---



\# 9.3 Adaptive AI Explanation



Hệ thống hỗ trợ nhiều chế độ:



\## Student Mode



\* Ngôn ngữ đơn giản.

\* Giải thích cơ bản.

\* Có ví dụ.



\## General Mode



\* Cân bằng giữa dễ hiểu và chuyên sâu.



\## Research Mode



\* Phân tích sâu.

\* Có nhiều nguồn tham khảo.



\---



\# 9.4 Timeline Explorer



Cho phép:



\* Xem lịch sử theo thời gian.

\* Sinh timeline theo câu hỏi.

\* Liên kết timeline với Knowledge Graph.



\---



\# 9.5 Source Explorer



Mỗi câu trả lời AI bao gồm:



\* Nguồn dữ liệu.

\* Văn bản liên quan.

\* Metadata.

\* Citation.



Mục tiêu:



\* Minh bạch.

\* Kiểm chứng.

\* Giảm hallucination.



\---



\# 10. AI Technologies



\## Large Language Model



Sử dụng:



\* OpenAI API.

\* Gemini API.

\* Claude API.



Không thực hiện fine-tuning.



\---



\# Retrieval-Augmented Generation



Mục tiêu:



\* Cung cấp context chính xác.

\* Giảm phụ thuộc kiến thức pretrained.



\---



\# Hybrid GraphRAG



Hệ thống kết hợp:



```

Knowledge Graph



&#x20;       +



Vector Retrieval



&#x20;       +



LLM

```



Hỗ trợ:



\* Multi-hop reasoning.

\* Relationship exploration.

\* Context-aware answering.



\---



\# Prompt Engineering



Điều chỉnh:



\* User mode.

\* Answer style.

\* Explanation depth.

\* Citation format.



\---



\# 11. Evaluation Plan



\## Retrieval Evaluation



Đánh giá:



\* Precision@K.

\* Recall@K.

\* MRR.



\---



\## RAG Evaluation



So sánh:



Baseline:



```

Question



↓



LLM



↓



Answer

```



Proposed:



```

Question



↓



Hybrid GraphRAG



↓



LLM



↓



Answer

```



Đánh giá:



\* Answer relevance.

\* Faithfulness.

\* Citation correctness.



\---



\## System Evaluation



Theo dõi:



\* Response latency.

\* Token usage.

\* API cost.



\---



\## User Evaluation



Đánh giá:



\* Mức độ dễ hiểu.

\* Độ hữu ích.

\* Độ tin cậy.



\---



\# 12. Technology Stack



\## Frontend



\* React / Next.js.

\* TypeScript.

\* Tailwind CSS.

\* Cytoscape.js.



\## Backend



\* FastAPI.

\* Python.

\* PostgreSQL.

\* SQLAlchemy.

\* JWT Authentication.



\## AI / Data



\* LangChain hoặc LlamaIndex.

\* Neo4j.

\* Qdrant / ChromaDB.

\* OpenAI API.

\* Gemini API.



\## Deployment



\* Docker.

\* Docker Compose.

\* Cloud Platform (optional).



\---



\# 13. Expected Outcome



Sản phẩm cuối cùng là:



Một AI-powered Historical Knowledge Platform có khả năng:



\* Thu thập và quản lý dữ liệu lịch sử.

\* Xây dựng Knowledge Graph.

\* Trực quan hóa mạng lưới tri thức.

\* Trả lời câu hỏi dựa trên dữ liệu truy xuất.

\* Cung cấp nguồn tham khảo.

\* Hỗ trợ người dùng khám phá lịch sử.



Dự án thể hiện các kỹ năng:



\* Fullstack Development.

\* Data Engineering.

\* Knowledge Graph Engineering.

\* Generative AI Application Development.

\* RAG / Hybrid GraphRAG.

\* AI System Evaluation.



\---



\# 14. Project Positioning



Dự án không định hướng như:



> "Một chatbot lịch sử sử dụng GPT API."



Mà là:



> "Một AI-powered Knowledge Exploration Platform sử dụng Knowledge Graph và Hybrid GraphRAG để tổ chức, khám phá và giải thích tri thức lịch sử Việt Nam dựa trên dữ liệu có nguồn gốc minh bạch."



\---



Đây sẽ là bản PCD mình khuyến nghị dùng làm \*\*tài liệu gốc xuyên suốt dự án\*\*. Các quyết định sau này (database, folder structure, roadmap, report, implementation) nên bám theo bản này để tránh scope creep.



