// Import Express.js framework
const express = require('express');

// Initialize Express application
const app = express();

// Define port number
const PORT = 3000;

// Route handler for root endpoint
// Returns "Hello world" when accessing http://localhost:3000/
app.get('/', (req, res) => {
  res.send('Hello world');
});

// Route handler for evening endpoint
// Returns "Good evening" when accessing http://localhost:3000/evening
app.get('/evening', (req, res) => {
  res.send('Good evening');
});

// Start server and listen on specified port
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
