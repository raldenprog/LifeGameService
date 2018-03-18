from multiprocessing import Process


class admin(Process):
    def __init__(self):
        super().__init__()
        self.daemon = True

    def run(self):
        import admin.server
