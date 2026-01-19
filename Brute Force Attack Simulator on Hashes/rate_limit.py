import time

class RateLimiter:
    def __init__(self, max_per_sec=80):
        self.max = max_per_sec
        self.count = 0
        self.start = time.time()

    def allow(self):
        if time.time() - self.start >= 1:
            self.count = 0
            self.start = time.time()
        self.count += 1
        return self.count <= self.max
