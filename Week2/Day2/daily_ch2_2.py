''' Daily Challenge'''

class Pagination:
    def __init__(self, items = [], pageSize=10):
        self.items = items
        self.pageSize = pageSize

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)