import unittest
import requests
from unittest.mock import patch
import json

BASE_URL = "http://localhost:5000"

class TestServer(unittest.TestCase):
    
    def test_root_endpoint(self):
        response = requests.get(f"{BASE_URL}/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Backend server is running", response.text)

    def test_post_log_sql_injection(self):
        payload = {
            "timestamp": "2024-12-08T12:00:00Z",
            "action": "' OR '1'='1",
            "page": "/dashboard"
        }
        response = requests.post(f"{BASE_URL}/log", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json().get("message"), "SQL Injection detected and logged")

    def test_post_log_admin_access(self):
        payload = {
            "timestamp": "2024-12-08T12:00:00Z",
            "action": "View Admin Page",
            "page": "/admin"
        }
        response = requests.post(f"{BASE_URL}/log", json=payload)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json().get("message"), "Access Denied")

    def test_post_log_success(self):
        payload = {
            "timestamp": "2024-12-08T12:00:00Z",
            "action": "Clicked button",
            "page": "/dashboard"
        }
        response = requests.post(f"{BASE_URL}/log", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("message"), "Log saved")

if __name__ == "__main__":
    unittest.main()
