class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.history: List[str] = [homepage]
        self.history_index = 0

    def visit(self, url: str) -> None:
        # First we clear the forward history
        self.history = self.history[:self.history_index+1]
        self.history.append(url)
        self.history_index = len(self.history) - 1


    def back(self, steps: int) -> str:
        i = 0
        while self.history_index > 0 and i < steps:
            self.history_index -= 1
            i += 1
        return self.history[self.history_index]


    def forward(self, steps: int) -> str:
        i = 0
        while (self.history_index < len(self.history) - 1) and i < steps:
            self.history_index += 1
            i += 1

        try:
            url = self.history[self.history_index]
        except IndexError:
            url = None

        return url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
