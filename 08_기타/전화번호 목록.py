class Node:
    def __init__(self, key):
        self.key = key
        self.child = dict()
        self.count = 0


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head     # 루트를 현재 포인터로 설정

        for ch in word:
            cur.count += 1      # 한 단어 추가될 것이므로 카운트 + 1

            # 만약 ch가 없다면
            if ch not in cur.child:
                cur.child[ch] = Node(ch)    # ch를 key로 갖는 자식 Node 생성
            cur = cur.child[ch]     # 자식 노드로 현재 포인터 이동

        cur.count += 1      # 마지막 노드 카운트 + 1

    def search(self, word):
        cur = self.head     # 루트를 현재 포인터로 설정

        for ch in word:

            # 만약 ch가 없다면
            if ch not in cur.child:
                return 0
            cur = cur.child[ch]     # 자식 노드로 현재 포인터 이동

        # 현재 노드까지의 카운트 리턴
        return cur.count


def isValidList():
    telcnt = int(input())
    telnums = list()
    trie = Trie()

    for i in range(telcnt):
        telnum = input()
        telnums.append(telnum)
        trie.insert(telnum)

    for telnum in telnums:
        if trie.search(telnum) > 1:
            return "NO"

    return "YES"


tc = int(input())

for _ in range(tc):
    print(isValidList())
