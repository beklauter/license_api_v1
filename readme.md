# License API System

This project provides a simple license management system with an API. It enables the creation of users and licenses with API keys.

## Features

- Simple User management with licenses
- API for license verification
- Automatic generation of license keys and API keys

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install flask python-dotenv
pip install flask flask
```

## Configuration

The application uses a `.env` file for configuration settings:

```
PORT=8080
HOST="0.0.0.0"
DEBUG=True
TEST_PRINT=True
```

## Usage

Start the application with:

```bash
python main.py
```

On startup, a test user ("testuser") with a license is automatically created and the API is launched.

## API Documentation

### License Verification

**Endpoint:** `/license/<license_key>`

**Method:** GET

**Parameters:**
- `license_key`: License key in the URL path
- `api_key`: (optional) as query parameter or header `X-API-Key`

**Request variants:**
1. With license key only:
   ```
   GET /license/YOUR-LICENSE-KEY
   ```

2. With API key as query parameter:
   ```
   GET /license/YOUR-LICENSE-KEY?api_key=YOUR-API-KEY
   ```

3. With API key as header:
   ```
   GET /license/YOUR-LICENSE-KEY
   Header: X-API-Key: YOUR-API-KEY
   ```

**Success response (200):**
```json
{
  "license": "LICENSE-KEY",
  "activated": true/false,
  "user": "username",
  "api_key": "API-KEY"
}
```

**Error responses:**
- 404: `{"error": "Lizenz nicht gefunden"}`
- 403: `{"error": "API-Key stimmt nicht mit der Lizenz überein"}`

## Project Structure

- `main.py` - Main entry point
- `api.py` - REST API using Flask
- `user.py` - User management and license generation
- `start.py` - Helper functions for loading environment variables
- `.env` - Configuration file

## Note

User data is stored in a JSON file (`users.json`).