from locust import HttpUser, task, between

class PerformanceTestUser(HttpUser):
    wait_time = between(1, 3)  # Random wait time between 1 and 3 seconds

    @task
    def get_logs(self):
        # Task to make a GET request to the "/log" endpoint
        self.client.get("/log")

    @task
    def post_log(self):
        # Task to make a POST request to the "/log" endpoint with a sample payload
        payload = {
            "timestamp": "2024-12-08T12:00:00Z",
            "action": "User clicked on BUTTON",
            "page": "/dashboard"
        }
        self.client.post("/log", json=payload)

# Command to run the performance test:
# locust -f performance_test.py --host=http://localhost:5000

class StressTestUser(HttpUser):
    wait_time = between(0.1, 0.5)  # Fast requests for stress testing

    @task
    def stress_test_log(self):
        # Task to make a POST request to the "/log" endpoint with a sample payload
        payload = {"timestamp": "2024-12-08T12:00:00Z", "action": "Stress", "page": "/about"}
        self.client.post("/log", json=payload)

# Command to run the stress test:
# locust -f performance_test.py --users=1000 --spawn-rate=50 --host=http://localhost:5000
