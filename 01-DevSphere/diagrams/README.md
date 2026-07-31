# DevSphere: Diagrams Index

This folder houses the structural and behavioral design diagrams for the DevSphere platform.

All diagrams are created using **Mermaid.js**, which can be rendered directly in GitHub markdown.

## List of Diagrams in Master README:
1. **System Architecture Diagram:** Outlines the connections between Nginx, FastAPI, Redis, PostgreSQL (pgvector), Celery Workers, and OpenAI.
2. **Collaborative Workspace Sequence Diagram:** Demonstrates WebSockets syncing changes between User A, User B, and the Redis cache backend.
3. **Database ERD (Entity-Relationship Diagram):** Maps the user, profile, repository, embedding, and workspace tables.
4. **User Journey Flowchart:** Follows a student registration path up to their first collaboration.

---

### Custom Rendering
To view these diagrams locally, use any Markdown viewer that supports Mermaid (e.g. VS Code Markdown Preview Enhanced) or copy the Mermaid code blocks from the [01-DevSphere/README.md](../README.md) into the [Mermaid Live Editor](https://mermaid.live).
