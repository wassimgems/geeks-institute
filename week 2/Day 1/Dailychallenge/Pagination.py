class Pagination :
    def __init__(self, items =None, page_size = 10):
        if items == None:
            items = []
        self.items = items
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = (len(items) + page_size - 1) // page_size
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]
    def go_to_page(self, page_num):
        if 1 <= page_num <= self.total_pages:
           self.current_idx = page_num - 1
        else:
            print("Invalid page number") 
    def first_page(self):
        self.current_idx = 0
        return self
    def last_page(self):
         if self.total_pages > 0:
           self.current_idx = self.total_pages - 1
         return self
    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx =+ 1
            return self
    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx =- 1
        return self
    def desplay_current_page(self):
        return "\n".join(self.get_visible_items()) 

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(7)
print(p.current_idx + 1)
# Output: 7

p.go_to_page(0)
# Expected behavior:
# Prints an invalid page message and keeps the current page unchanged.

    