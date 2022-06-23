from generators import fake


class UserGenerator:

    def __init__(self):
        self.name = None
        self.job = None

    def set_name(self, name=fake.name()):
        self.name = name
        return self

    def set_job(self, job=fake.first_name()):
        self.job = job
        return self

    def _clear(self):
        self.set_job()
        self.set_name()

    def build(self):
        self._clear()
        return {"name": self.name, "job": self.job}
