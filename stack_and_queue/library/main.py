from collections import deque

if __name__ == "__main__":
    # stack
    q = deque()
    for i in range(1, 5):
        q.append(i)
    for _ in range(4):
        print(q)
        print(q.pop())
    print(q)
    # queue
    q = deque()
    for i in range(1, 5):
        q.append(i)
    for _ in range(4):
        print(q)
        print(q.popleft())
    print(q)
