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



# from locust import HttpUser, task, between

# class WebsiteUser(HttpUser):
#     wait_time = between(1, 3)

#     def on_start(self):
#         self.logged_in = False  

      
#         with self.client.post(
#             "/deliveryman/login",
#             data={"username": "dm1@gmail.com", "password": "123456789"},
#             name="Login",
#             catch_response=True
#         ) as response:
#             if "Invalid" in response.text or "incorrect" in response.text.lower():
#                 response.failure("Invalid username or password.")
#             else:
#                 response.success()
#                 self.logged_in = True

#         if self.logged_in:
#             self.client.get("/dashboard", name="Visit Upload Page")

 
#     @task
#     def stop_task(self):
#         self.stop(True)  



# from locust import HttpUser, task, between
# import re

# class WebsiteUser(HttpUser):
#     wait_time = between(1, 3)

#     def on_start(self):
#         self.logged_in = False

#         r = self.client.get("/deliveryman/login")
#         token = re.search(r'name="_token" value="(.+?)"', r.text)
#         if not token:
#             return

#         res = self.client.post(
#             "/deliveryman/authenticate",
#             data={
#                 "email": "dm1@gmail.com",
#                 "password": "123456789",
#                 "_token": token.group(1)
#             }
#         )

#         if res.status_code in [200, 302]:
#             self.logged_in = True

#     @task
#     def dashboard(self):
#         if self.logged_in:
#             self.client.get("/deliveryman/dashboard")



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
#         self.client.get("/tlentry/")

#         login_data = {
#             "log": "adminag",
#             "pwd": "WP@bd2025!",
#             "rememberme": "forever",
#             "wp-submit": "Log In",
#             "redirect_to": "/wp-admin/",
#             "testcookie": "1"
#         }

#         with self.client.post("/tlentry/", data=login_data, allow_redirects=True, catch_response=True) as post_response:
#             if any(name.startswith("wordpress_logged_in") for name in self.client.cookies.keys()):
#                 post_response.success()
#                 print("Login success")
#             else:
#                 post_response.failure("Login failed (no cookie)")
#                 print("Login failed (no cookie)")
#                 return  

#         with self.client.get("/wp-admin/", allow_redirects=True, catch_response=True) as admin_response:
#             if "Dashboard" in admin_response.text in admin_response.text:
#                 admin_response.success()
#                 print("Accessed admin page successfully")
#             else:
#                 admin_response.failure("Failed to access admin page content")
#                 print("Failed to access admin page content")




# from locust import HttpUser, task, between

# class WebsiteUser(HttpUser):
#     wait_time = between(1, 3)

#     @task
#     def login(self):
#         self.client.get("/wp-login.php")

#         login_data = {
#             "log": "adminag",
#             "pwd": "WP@bd2025!",
#             "rememberme": "forever",
#             "wp-submit": "Log In",
#             "redirect_to": "/wp-admin/",
#             "testcookie": "1"
#         }

#         with self.client.post("/wp-login.php", data=login_data, allow_redirects=True, catch_response=True) as post_response:
#             if any(name.startswith("wordpress_logged_in") for name in self.client.cookies.keys()):
#                 post_response.success()
#                 print("Login success")
#             else:
#                 post_response.failure("Login failed (no cookie)")
#                 print("Login failed (no cookie)")
#                 return  

#         with self.client.get("/wp-admin/", allow_redirects=True, catch_response=True) as admin_response:
#             if "Dashboard" in admin_response.text in admin_response.text:
#                 admin_response.success()
#                 print("Accessed admin page successfully")
#             else:
#                 admin_response.failure("Failed to access admin page content")
#                 print("Failed to access admin page content")





# from locust import HttpUser, task, between

# class WebsiteUser(HttpUser):
#     wait_time = between(1, 3)

#     def on_start(self):
#         self.client.get("/tlentry/")
#         data = {
#             "log": "adminag",
#             "pwd": "WP@bd2025!",
#             "rememberme": "forever",
#             "wp-submit": "Log In",
#             "redirect_to": "/wp-admin/",
#             "testcookie": "1"
#         }
#         with self.client.post("/tlentry/", data=data, allow_redirects=False, catch_response=True) as r:
#             cookies = self.client.cookies.get_dict()
#             if any(k.startswith("wordpress_logged_in") for k in cookies):
#                 r.success()
#                 print("Login success")
#             else:
#                 r.failure("Login failed")
#         self.client.get(r.headers.get("Location", "/wp-admin/"))

#     @task
#     def access_admin(self):
#         r = self.client.get("/wp-admin/")
#         cookies = self.client.cookies.get_dict()
#         if r.status_code == 200 and any(k.startswith("wordpress_logged_in") for k in cookies):
#             print("Accessed admin page")
#         else:
#             print("Failed admin page")




# from locust import HttpUser, task, between
# from bs4 import BeautifulSoup


# class DNCCLoginUser(HttpUser):

#     wait_time = between(1, 2)

#     host = "http://103.135.235.182"

#     USERNAME = "Mahmuda"
#     PASSWORD = "meem123"

#     @task
#     def login_until_otp(self):

#         # ==========================================
#         # 1. Open Login Page
#         # ==========================================
#         with self.client.get(
#             "/Default.aspx",
#             name="01 - Open Login Page",
#             catch_response=True
#         ) as response:

#             if response.status_code != 200:
#                 response.failure(
#                     f"Login page failed: {response.status_code}"
#                 )
#                 return

#             soup = BeautifulSoup(response.text, "html.parser")

#             def get_hidden(name):
#                 element = soup.find("input", {"name": name})
#                 return element.get("value", "") if element else ""

#             viewstate = get_hidden("__VIEWSTATE")
#             eventvalidation = get_hidden("__EVENTVALIDATION")
#             viewstategenerator = get_hidden("__VIEWSTATEGENERATOR")

#         # ==========================================
#         # 2. Select Wing
#         #    Holding Tax = b
#         # ==========================================
#         with self.client.post(
#             "/Default.aspx",
#             data={
#                 "__EVENTTARGET": "ddType",
#                 "__EVENTARGUMENT": "",
#                 "__LASTFOCUS": "",

#                 "__VIEWSTATE": viewstate,
#                 "__VIEWSTATEGENERATOR": viewstategenerator,
#                 "__EVENTVALIDATION": eventvalidation,

#                 "ddType": "b"
#             },
#             name="02 - Select Wing: Holding Tax",
#             catch_response=True
#         ) as response:

#             if response.status_code != 200:
#                 response.failure(
#                     f"Wing selection failed: {response.status_code}"
#                 )
#                 return

#             # Get NEW ASP.NET hidden values
#             soup = BeautifulSoup(response.text, "html.parser")

#             def get_hidden_after_post(name):
#                 element = soup.find("input", {"name": name})
#                 return element.get("value", "") if element else ""

#             viewstate = get_hidden_after_post("__VIEWSTATE")
#             eventvalidation = get_hidden_after_post("__EVENTVALIDATION")
#             viewstategenerator = get_hidden_after_post(
#                 "__VIEWSTATEGENERATOR"
#             )

#         # ==========================================
#         # 3. Select Tax Type
#         #    Holding Tax = 1
#         # ==========================================
#         # NOTE:
#         # ddlGender does NOT have onchange/postback.
#         # So we don't need a separate HTTP request for it.
#         # We send ddlGender=1 during login.

#         # ==========================================
#         # 4. Login
#         # ==========================================
#         with self.client.post(
#             "/Default.aspx",
#             data={
#                 "__EVENTTARGET": "",
#                 "__EVENTARGUMENT": "",
#                 "__LASTFOCUS": "",

#                 "__VIEWSTATE": viewstate,
#                 "__VIEWSTATEGENERATOR": viewstategenerator,
#                 "__EVENTVALIDATION": eventvalidation,

#                 "ddType": "b",
#                 "ddlGender": "1",

#                 "txtLogin": self.USERNAME,
#                 "txtPwd": self.PASSWORD,

#                 "btnSubmit": "LOGIN"
#             },
#             name="03 - Login",
#             allow_redirects=True,
#             catch_response=True
#         ) as response:

#             # ==========================================
#             # 5. Check whether OTP page was reached
#             # ==========================================

#             if "otpverification" in response.url.lower():

#                 print("✅ LOGIN SUCCESS → OTP PAGE")
#                 print("OTP URL:", response.url)

#                 response.success()

#             elif response.status_code == 200:

#                 print("❌ Login did not reach OTP page")
#                 print("Final URL:", response.url)

#                 response.failure(
#                     "Login did not reach OTP verification page"
#                 )

#             else:

#                 response.failure(
#                     f"Login failed: HTTP {response.status_code}"
#                 )





from bs4 import BeautifulSoup
from locust import HttpUser, task

USERNAME = "Mahmuda"
PASSWORD = "meem123"

DNCC_UNLOCK_AUTHORIZED = "YES"
DNCC_CUSERID = "Mahmuda"


class DNCCUser(HttpUser):

    @task
    def login(self):

        # Open login page
        self.client.get("/newv/Default")

        # Unlock user if authorized
        if DNCC_UNLOCK_AUTHORIZED == "YES":
            self.client.get(
                "/web/userulocknew.aspx",
                params={"cuserid": DNCC_CUSERID}
            )

        # Get login form
        r = self.client.get("/newv/Default")
        soup = BeautifulSoup(r.text, "html.parser")

        data = {
            x["name"]: x.get("value", "")
            for x in soup.select("input[type=hidden][name]")
        }

        # Select wing and gender
        data.update({
            "__EVENTTARGET": "ddType",
            "ddType": "b",
            "ddlGender": "0"
        })

        r = self.client.post("/newv/Default", data=data)

        # Get updated form data
        soup = BeautifulSoup(r.text, "html.parser")

        data = {
            x["name"]: x.get("value", "")
            for x in soup.select("input[type=hidden][name]")
        }

        # Submit login details
        data.update({
            "ddType": "b",
            "ddlGender": "1",
            "txtLogin": USERNAME,
            "txtPwd": PASSWORD,
            "btnSubmit": "LOGIN"
        })

        r = self.client.post(
            "/newv/Default",
            data=data,
            allow_redirects=False
        )

        # Check OTP redirect
        location = r.headers.get("Location", "")

        if "otpverification" not in location.lower():
            print("Login failed:", r.status_code)
            self.stop()
            return

        print("OTP page reached successfully")

        # Open OTP page
        otp_page = self.client.get(location)
        soup = BeautifulSoup(otp_page.text, "html.parser")

        otp_data = {
            x["name"]: x.get("value", "")
            for x in soup.select("input[type=hidden][name]")
        }

        # Enter OTP
        otp = input("Enter OTP: ")

        otp_data.update({
            "txtOTP": otp,
            "btnSubmit": "VERIFY"
        })

        result = self.client.post(
            otp_page.url,
            data=otp_data,
            allow_redirects=True
        )

        print("OTP response:", result.status_code)

        # Check dashboard
        dashboard = self.client.get("/newv/web/homenew_ver2")

        if (
            dashboard.status_code == 200
            and "otpverification" not in dashboard.url.lower()
        ):
            print("SUCCESS: Dashboard reached")
        else:
            print("Dashboard access failed")
            print("Final URL:", dashboard.url)

        # Stop after one attempt
        self.environment.runner.quit()
