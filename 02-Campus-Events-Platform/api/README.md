# Campus Events Platform: API Endpoints Catalog

This document defines the REST and WebSockets API signatures for the Campus Events Platform.

## 1. API Catalog

### 1.1. Event Creation Flow

#### `POST /events`
* **Headers:** `Authorization: Bearer <JWT_TOKEN>`
* **Role required:** `Club Head`
* **Request Body:**
  ```json
  {
    "title": "Hackathon 2026",
    "description": "24-hour campus hacking challenge.",
    "venue_id": "89b910fc-6e79-4d62-a521-6b80151c9a01",
    "start_time": "2026-10-15T09:00:00Z",
    "end_time": "2026-10-16T09:00:00Z"
  }
  ```
* **Response (201 Created):**
  ```json
  {
    "event_id": "c10f82c4-a312-4d62-9721-6b80151c8e11",
    "status": "Pending Approval"
  }
  ```

---

### 1.2. High-Concurrency Seating Booking

#### `POST /bookings`
* **Headers:** `Authorization: Bearer <JWT_TOKEN>`
* **Role required:** `Student`
* **Request Body:**
  ```json
  {
    "event_id": "c10f82c4-a312-4d62-9721-6b80151c8e11",
    "seat_number": "Row-G-14"
  }
  ```
* **Response (202 Accepted):**
  ```json
  {
    "booking_id": "e98f121a-6c79-4672-a212-612b18acfa01",
    "status": "Reserved",
    "ttl_remaining_seconds": 300
  }
  ```
* **Error States:**
  - `409 Conflict`: Seat is currently locked or sold.
  - `429 Too Many Requests`: User booking rate limit exceeded.
