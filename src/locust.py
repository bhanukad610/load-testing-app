from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def news_page(self):
        self.client.get(url="news")

    @task
    def reel_page(self):
        self.client.get(url="reel")

    @task
    def sport_page(self):
        self.client.get(url="sport")