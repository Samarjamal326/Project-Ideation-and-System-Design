# DevSphere: API Reference Specifications

This folder contains API definition files and documentation. Below is the detailed specification of the critical backend REST and WebSockets API endpoints.

---

## 1. Global Specifications
* **Base URL:** `https://api.devsphere.io/v1`
* **Response Format:** `application/json`
* **Auth Scheme:** Bearer Token JWT in headers (`Authorization: Bearer <JWT_TOKEN>`)

---

## 2. API Endpoints Catalog

### 2.1. Authentication Services

#### `POST /auth/register`
* **Description:** Register a new account.
* **Payload:**
  ```json
  {
    "email": "developer@domain.com",
    "password": "SecurePassword123!",
    "role": "Developer"
  }
  ```
* **Success Response (201 Created):**
  ```json
  {
    "message": "User registered successfully",
    "user_id": "a90f11c3-6379-4672-9721-6b80151c8901"
  }
  ```

#### `POST /auth/login`
* **Description:** Access credential validation.
* **Payload:**
  ```json
  {
    "email": "developer@domain.com",
    "password": "SecurePassword123!"
  }
  ```
* **Success Response (200 OK):**
  ```json
  {
    "access_token": "eyJhbGciOi...",
    "refresh_token": "d7b2a95c...",
    "token_type": "bearer"
  }
  ```

---

### 2.2. Ingestion Services

#### `POST /profiles/sync`
* **Description:** Trigger repository scanning and AI indexing.
* **Headers:** `Authorization: Bearer <JWT>`
* **Payload:**
  ```json
  {
    "github_username": "octocat"
  }
  ```
* **Success Response (202 Accepted):**
  ```json
  {
    "task_id": "job_d98f121a_6c",
    "status": "Processing",
    "estimated_seconds": 45
  }
  ```

---

### 2.3. Search Services

#### `GET /search/candidates`
* **Description:** Search candidate database using natural language vector queries.
* **Query Parameters:**
  - `q`: Natural language search query (e.g. `Experienced python developer with fastapi experience`)
  - `limit`: Number of records to return (default: `10`)
* **Success Response (200 OK):**
  ```json
  {
    "results": [
      {
        "profile_id": "c10f82c4-3329-4d62-a212-612b18acfa01",
        "full_name": "Jane Doe",
        "github_username": "janedoe",
        "match_score": 0.895,
        "bio": "Building microservices using FastAPI and Go. Love Postgres tuning.",
        "top_languages": ["Python", "Go", "TypeScript"]
      }
    ]
  }
  ```
