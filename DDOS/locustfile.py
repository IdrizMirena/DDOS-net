from locust import HttpUser, task, between

class LoadTestUser(HttpUser):
    wait_time = between(1, 2)  # Koha mes kërkesave

    @task
    def load_test(self):
        self.client.get("/")  # Kërkon faqen kryesore

if __name__ == "__main__":
    import os
    os.system("locust -f locustfile.py --host=https://blog.sentry.security/ --users 70000 --spawn-rate 5")
