class ListNode:
    def __init__(self, value: str = '', prev_node: Optional['ListNode'] = None, next_node: Optional['ListNode'] = None):

        self.prev: Optional[ListNode] = prev_node
        self.val: str = value
        self.next: Optional[ListNode] = next_node

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history: ListNode = ListNode(homepage)
        self.current: ListNode = self.history

    def visit(self, url: str) -> None:
        new: ListNode = ListNode(url, prev_node=self.current)
        self.current.next = new
        self.current = new
        

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.current.prev:
                break

            self.current = self.current.prev

        return self.current.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.current.next:
                break

            self.current = self.current.next

        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)