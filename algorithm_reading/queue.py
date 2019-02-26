from collections import deque       # deque表示队列

# 队列先进先出，栈后进先出
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["clair"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search_queue = deque()
search_queue += graph["you"]     # 将数据输入队列

def search_seller(serch_queue):
    while search_queue:
        person = search_queue.popleft()   # 从队列中取出一个数据
        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True
        else:
            search_queue += graph[person]
        return False

def person_is_seller(name):
    return name[-1] == 'm'

search_seller(search_queue)