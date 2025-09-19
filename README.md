# pmd

Professional Member Directory (PMD)
An MVP for AI-Based Directory Project that enable professional member discovery, profile management, and semantic search. Built with speed, clarity, and principled architecture.

MVP Goals
- Enable public and member-facing profile discovery
- Support semantic search via FAISS + MiniLM
- Provide secure registration and role-based profile management
- Showcase ethical orchestration and transparent design
- Deploy a live demo with storytelling and stakeholder-ready documentation

| DFD Process                        | Tech Choice                                                                        | Why This Fits (Bare Minimum)                                                              |
|------------------------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Directory Search                   | FastAPI (Python) + PostgreSQL profiles table + optional FAISS (local index)        | FastAPI is lightweight and async-ready; FAISS enables vector/semantic search without GPU. |
| Search Query Handling & Refinement | FastAPI endpoint with sentence-transformers MiniLM model                           | Efficient embeddings, low RAM/CPU impact.                                                 |
| System Logs (Analytics)            | PostgreSQL logging table + Python structlog or built-in logging                    | Single DB instance; metadata-only log entries keep storage lean.                          |
| Directory List UI                  | React (if SPA needed) or Alpine.js (for ultra-light DOM binding)                   | Minimizes backend load, only pulls partial data until expanded.                           |
| Profile Summary Retrieval          | REST API in FastAPI + in-memory cache (Redis optional, local dictionary for start) | Serves summaries fast without hitting DB every time.                                      |
| Public Facing Profile UI           | UI framework above + lazy-loaded detail view                                       | Improves perceived performance, low server strain.                                        |
| Member Registration                | FastAPI endpoint → PostgreSQL users table                                          | One DB instance handles both auth and content.                                            |
| User Authentication                | JWT tokens (PyJWT) + bcrypt hashing                                                | Stateless auth → minimal DB traffic.                                                      |
| Subscription Checkout              | Stripe API integration                                                             | Outsources payment security and compliance.                                               |
| Payment Processor                  | Stripe (reuses above integration)                                                  | No separate process; single API call from backend.                                        |
| Create Profile                     | FastAPI endpoint → PostgreSQL profiles table                                       | Fits existing schema; avoids separate microservice.                                       |
| Profile Management                 | FastAPI service layer + role-based access checks                                   | Keeps business logic centralized and lean.                                                |
| Profile Edit (Timestamp Logging)   | PATCH endpoint + edit_events table for timestamps                                  | Minimal metadata, avoids bloat from storing diffs.                                        |
| Member Facing Profile UI           | Same lightweight frontend approach as public UI                                    | Maintains shared component base.                                                          |

