# 13nov01

## Project Description

This is a Node.js tutorial project demonstrating how to build a simple HTTP server using the Express.js framework. The server implements two GET endpoints that return plain text responses.

## Features

- Express.js web server
- Two GET endpoints:
  - `/` - Returns "Hello world"
  - `/evening` - Returns "Good evening"
- Runs on port 3000

## Installation

1. Clone this repository
2. Install dependencies:

```bash
npm install
```

## Usage

Start the server:

```bash
node server.js
```

Or use the npm script:

```bash
npm start
```

The server will start and display: `Server is running on http://localhost:3000`

## Testing the Endpoints

### Test the root endpoint:

```bash
curl http://localhost:3000/
```

Expected response: `Hello world`

### Test the evening endpoint:

```bash
curl http://localhost:3000/evening
```

Expected response: `Good evening`

You can also test the endpoints by opening the following URLs in your web browser:
- http://localhost:3000/
- http://localhost:3000/evening

## Technical Details

- **Node.js Version**: v20.19.5
- **Express.js Version**: ^4.18.2
- **Server Port**: 3000