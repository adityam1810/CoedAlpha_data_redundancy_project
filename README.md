# Data Redundancy Removal System (Cloud Version)

This project is part of my Cloud Computing Internship at CodeAlpha.  
It ensures only unique user data is stored in a simulated cloud database.

## 🛠 Built With:
- Python
- Flask
- CSV (simulated database)

## Features:
- Checks for duplicate entries
- Appends only unique data
- Cloud deployable via Render

## How to Use:
Send a POST request to `/add` endpoint with `name` and `email`.

```json
{
  "name": "John",
  "email": "john@example.com"
}
