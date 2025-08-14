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


# import re
# from locust import HttpUser, task, between

# class WebsiteUser(HttpUser):
#     wait_time = between(1, 3)

#     @task
#     def login(self):
#         # Step 1: GET login page
#         res = self.client.get("/", name="Get Login Page")

#         # Step 2: Extract CSRF token
#         token = re.search(r'name="_token"\s*value="(.+?)"', res.text)
#         if not token:
#             return

#         # Step 3: POST login
#         self.client.post("/admin_login", data={
#             "email": "admin@gmail.com",
#             "password": "111",
#             "_token": token.group(1)
#         }, name="Login")




        #  python -m locust


# import re
# from locust import HttpUser, task, between

# class WebsiteUser(HttpUser):
#     wait_time = between(1, 3)

#     @task
#     def login(self):
#         r = self.client.get("/supervisor/login")
#         token = re.search(r'name="_token"\s*value="(.+?)"', r.text)
#         if not token:
#             return
#         login_res = self.client.post("/supervisor/login", data={
#             "_token": token.group(1),
#             "email": "sp1@gmail.com",
#             "password": "123456789"
#         })
#         r = self.client.get("/supervisor/otp-verify")
#         otp_token = re.search(r'name="_token"\s*value="(.+?)"', r.text)
#         if not otp_token:
#             return
#         self.client.post("/supervisor/otp-verify", data={
#             "_token": otp_token.group(1),
#             "otp": "123456"
#         })


# import re
# from locust import HttpUser, task, between

# class WebsiteUser(HttpUser):
#     wait_time = between(1, 3)

#     @task
#     def login(self):
#         r = self.client.get("/deliveryman/login")
#         token = re.search(r'name="_token"\s*value="(.+?)"', r.text)
#         if not token:
#             return
#         login_res = self.client.post("/deliveryman/authenticate", data={
#             "_token": token.group(1),
#             "email": "dm1@gmail.com",
#             "password": "123456789"
#         })
#         r = self.client.get("/deliveryman/otp-verify")
#         otp_token = re.search(r'name="_token"\s*value="(.+?)"', r.text)
#         if not otp_token:
#             return
#         self.client.post("/deliveryman/otp-verify", data={
#             "_token": otp_token.group(1),
#             "otp": "123456"
#         })


# from locust import HttpUser, task, between

# class WebsiteUser(HttpUser):
#     wait_time = between(1, 3)

#     @task
#     def login(self):
#         # Step 1: Load login page to get cookies if any
#         response = self.client.get("tlentry/")

#         # Step 2: Prepare login form data
#         login_data = {
#             "log": "adminag",
#             "pwd": "WP@bd2025!",
#             "rememberme": "forever",
#             "wp-submit": "Log In",
#             "redirect_to": "https://tldelivery.rksoftwarebd.com/wp-admin/",
#             "testcookie": "1"
#         }

#         # Step 3: Post login form with redirects enabled to follow any redirects
#         login_response = self.client.post("tlentry/", data=login_data, allow_redirects=True)

#         # Step 4: After login, request the dashboard page explicitly
#         dashboard_response = self.client.get("wp-admin/")

#         # Step 5: Check if dashboard loaded successfully
#         if "Dashboard" in dashboard_response.text or "wp-admin-bar-logout" in dashboard_response.text:
#             print("Login success and dashboard loaded")
#         else:
#             print("Login failed or dashboard not accessible")




from locust import HttpUser, task, constant

class WebsiteUser(HttpUser):
    # Fixed wait time between tasks for more consistent results
    wait_time = constant(1)

    def on_start(self):
        """
        Runs once when each simulated user starts.
        Logs in and keeps the session.
        """
        # Step 1: Load login page to set cookies
        self.client.get("tlentry/")

        # Step 2: Login form data
        login_data = {
            "log": "adminag",
            "pwd": "WP@bd2025!",
            "rememberme": "forever",
            "wp-submit": "Log In",
            "redirect_to": "https://tldelivery.rksoftwarebd.com/wp-admin/",
            "testcookie": "1"
        }

        # Step 3: Submit login
        login_response = self.client.post("tlentry/", data=login_data, allow_redirects=True)

        # Optional check for successful login
        if login_response.status_code != 200:
            print(f"Login failed with status: {login_response.status_code}")

    @task
    def view_dashboard(self):
        """
        Simulates a logged-in user visiting the dashboard.
        """
        dashboard_response = self.client.get("wp-admin/")
        if dashboard_response.status_code != 200:
            print(f"Dashboard load failed: {dashboard_response.status_code}")
