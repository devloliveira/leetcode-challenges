class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.history: List[str] = [homepage]
        self.history_index = 0

    def visit(self, url: str) -> None:
        # First we clear the forward history
        self.history = self.history[:self.history_index+1]
        self.history.append(url)
        self.history_index += 1


    def back(self, steps: int) -> str:
        if self.history_index - steps >= 0:
            self.history_index -= steps
        else:
            self.history_index = 0
        return self.history[self.history_index]


    def forward(self, steps: int) -> str:
        size_history = len(self.history)
        if self.history_index + steps < size_history - 1:
            self.history_index += steps
        else:
            self.history_index = size_history - 1
        return self.history[self.history_index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
