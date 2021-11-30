from locust import HttpUser, task


class TestCarga(HttpUser):

    @task(1)
    def solicitudes(self):
        self.client.get("/solicitudes/")

    @task(2)
    def profesionales(self):
        self.client.get("/profesionales/")
        
    
    @task(3)
    def profesionales_perfil(self):
        self.client.get("/veterinarios/profile/1")
