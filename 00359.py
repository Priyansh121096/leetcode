# https://leetcode.com/problems/logger-rate-limiter/
# 359. Logger Rate Limiter

class Logger:
    def __init__(self):
        self.map = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.map or self.map[message] <= timestamp:
            self.map[message] = timestamp + 10
            return True
        
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)