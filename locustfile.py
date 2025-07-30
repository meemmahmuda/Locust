# from locust import HttpUser, task
# from locust import HttpLocust, HttpUser, TaskSet, task

# class HelloWorldUSer(HttpUser):
#      @task
#      def helloworld(self):
#          self.client.get("https://list.sanjoydeyreju.com/supervisor/dashboard")


# from locust import HttpUser, task, between

# class HelloWorldUser(HttpUser):
#     wait_time = between(1, 3)  
#     @task
#     def helloworld(self):
#         self.client.get("/")

import re
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def login(self):
        # Step 1: GET login page
        res = self.client.get("/", name="Get Login Page")

        # Step 2: Extract CSRF token
        token = re.search(r'name="_token"\s*value="(.+?)"', res.text)
        if not token:
            return

        # Step 3: POST login
        self.client.post("/admin_login", data={
            "email": "admin@gmail.com",
            "password": "111",
            "_token": token.group(1)
        }, name="Login")




        #  python -m locust