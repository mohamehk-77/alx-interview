# 0x03-log_parsing

This project is about parsing Apache logs using Python.
The script `logs.py` parses Apache logs and outputs the following information:

- The total number of requests
- The number of requests by method (GET, POST, etc.)
- The number of requests by status code (200, 404, etc.)
- The top 10 most frequent IP addresses
- The top 10 most frequent URLs
- The top 10 most frequent user agents
- The average bytes sent per request
- The total bytes sent
- The average time taken to serve a request
- The total time taken to serve all requests
- The 10 most frequent referrers
