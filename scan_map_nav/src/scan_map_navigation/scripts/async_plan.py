"""One read-only planning request at a time. Worker never commits a route."""
import threading
import time


class AsyncPlan:
    def __init__(self, function, task_id):
        self.task_id=task_id
        self.started=time.monotonic()
        self.done=threading.Event()
        self.result=None
        self.error=None
        def work():
            try:
                self.result=function()
            except Exception as exc:
                self.error=exc
            finally:
                self.done.set()
        threading.Thread(target=work,daemon=True).start()
