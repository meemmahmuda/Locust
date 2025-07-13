
# from locust import HttpUser, task
# from locust import HttpLocust, HttpUser, TaskSet, task

# class HelloWorldUSer(HttpUser):
#      @task
#      def helloworld(self):
#          self.client.get("https://list.sanjoydeyreju.com/supervisor/dashboard")


from locust import HttpUser, task, between

class HelloWorldUser(HttpUser):
    wait_time = between(1, 3)  
    @task
    def helloworld(self):
        self.client.get("/supervisor/dashboard")


        #  python -m locust