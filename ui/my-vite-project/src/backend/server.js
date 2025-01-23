const express = require('express');
const fs = require('fs');
const cors = require('cors');
const app = express();
const port = 5000;

app.use(cors());
app.use(express.json());

// Function to detect SQL Injection
const detectSQLInjection = (action) => {
  // Common words and patterns in SQL Injection
  const sqlPatterns = [
    /(\bOR\b|\bAND\b).*?=.*?/i,  // OR/AND logic operator
    /' OR '1'='1/i,              // Typical SQL Injection
    /--/i,                       // SQL Comments
    /;/i,                        // Multiple statements
    /DROP|SELECT|INSERT|DELETE/i, // SQL Commands
    /'.*?=.*?'/i,                // Comparison with quotes
  ];

  // Check if the action contains any SQL Injection pattern
  return sqlPatterns.some(pattern => pattern.test(action));
};

// Root endpoint
app.get('/', (req, res) => {
  res.send('Backend server is running');
});

// Endpoint to get logs
app.get('/log', (req, res) => {
  fs.readFile('userActions.txt', 'utf8', (err, data) => {
    if (err) {
      return res.status(500).json({ message: 'Error reading log' });
    }

    const logEntries = data.split('\n').filter(entry => entry.trim() !== '').map(entry => {
      const parsedEntry = JSON.parse(entry); 
      return parsedEntry;  
    });

    res.status(200).json({ log: logEntries });
  });
});

// Endpoint to save logs
app.post('/log', (req, res) => {
  const { timestamp, action, page } = req.body;

  // Check if the action contains SQL Injection
  if (detectSQLInjection(action)) {
    const logEntry = {
      timestamp: timestamp,
      action: 'Attempted SQL Injection',
      page: page,
    };

    fs.appendFile('userActions.txt', JSON.stringify(logEntry) + '\n', (err) => {
      if (err) {
        return res.status(500).json({ message: 'Error saving log' });
      }
    });

    return res.status(400).json({ message: 'SQL Injection detected and logged' });
  }

  // Check if the page contains "/admin"
  if (page.includes('/admin')) {
    console.log('Invalid action detected: User tried to access restricted page', page);

    const logEntry = {
      timestamp: timestamp,
      action: `User tried to access restricted page ${page}`,
      page: page,
    };

    fs.appendFile('userActions.txt', JSON.stringify(logEntry) + '\n', (err) => {
      if (err) {
        return res.status(500).json({ message: 'Error saving log' });
      }
    });

    return res.status(403).json({ message: 'Access Denied' }); // 403 Forbidden
  }

  // If it's not SQL Injection and not unauthorized access to the "/admin" page, save the log
  const logEntry = {
    timestamp: timestamp,
    action: action,
    page: page,
  };

  fs.appendFile('userActions.txt', JSON.stringify(logEntry) + '\n', (err) => {
    if (err) {
      return res.status(500).json({ message: 'Error saving log' });
    }
    res.status(200).json({ message: 'Log saved' });
  });
});

// Starting the server on port 5000
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
