# Startup Incubator Platform: API & gRPC Reference

This document covers the REST and internal gRPC definitions for the Startup Incubator Platform.

## 1. REST Gateway Endpoints

### 1.1. Pitch Deck S3 Pre-sign API
* **Endpoint:** `POST /api/v1/pitches/upload`
* **Headers:** `Authorization: Bearer <JWT_TOKEN>`
* **Role required:** `Founder`
* **Request Body:**
  ```json
  {
    "filename": "pitch_deck_veloce.pdf",
    "content_type": "application/pdf"
  }
  ```
* **Response (200 OK):**
  ```json
  {
    "upload_url": "https://s3.us-east-1.amazonaws.com/incubator-pitches/pitch_deck_veloce.pdf?AWSAccessKeyId=...",
    "file_key": "pitches/pitch_deck_veloce.pdf"
  }
  ```

---

## 2. Internal gRPC Services

To ensure fast internal communications, services share details using protobuf-defined gRPC methods:

```protobuf
syntax = "proto3";

package matchmaking;

service MatchmakingService {
    rpc CalculateMatch (MatchRequest) returns (MatchResponse);
}

message MatchRequest {
    string startup_id = 1;
    string thesis_id = 2;
}

message MatchResponse {
    double compatibility_score = 1;
    repeated string matched_tags = 2;
}
```
