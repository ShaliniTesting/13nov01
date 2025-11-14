# 13nov01

A simple Node.js tutorial project demonstrating how to create a web server using Express.js framework with multiple endpoints.

## Project Description

This project implements a basic Express.js server with two GET endpoints that return plain text responses. It serves as an educational example for learning Express.js fundamentals, including:

- Setting up an Express.js application
- Defining multiple route handlers
- Responding to HTTP GET requests
- Running a Node.js server on localhost

## Prerequisites

- Node.js (v12 or higher)
- npm (Node Package Manager)

## Installation

1. Clone this repository or navigate to the project directory

2. Install the required dependencies:

```bash
npm install
```

This will install Express.js and all necessary dependencies listed in `package.json`.

## Usage

Start the server by running:

```bash
node server.js
```

You should see a confirmation message indicating the server is running on `http://localhost:3000`.

## API Endpoints

The server provides the following endpoints:

### 1. Root Endpoint

- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns a simple greeting message
- **Response**: `Hello world`

### 2. Evening Endpoint

- **URL**: `/evening`
- **Method**: `GET`
- **Description**: Returns an evening greeting message
- **Response**: `Good evening`

## Testing the Endpoints

You can test the endpoints using curl commands in your terminal:

### Test the root endpoint:

```bash
curl http://localhost:3000/
```

Expected output: `Hello world`

### Test the evening endpoint:

```bash
curl http://localhost:3000/evening
```

Expected output: `Good evening`

Alternatively, you can open these URLs in your web browser:
- http://localhost:3000/
- http://localhost:3000/evening

## Project Structure

```
.
├── README.md          # This file
├── package.json       # Project configuration and dependencies
├── server.js          # Main server implementation
└── .gitignore        # Git ignore patterns
```

## Learning Objectives

This tutorial demonstrates:
- How to initialize an Express.js application
- How to define route handlers for different endpoints
- How to send text responses to HTTP requests
- How to start a server and listen on a specific port

## License

This is a tutorial project for educational purposes.

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