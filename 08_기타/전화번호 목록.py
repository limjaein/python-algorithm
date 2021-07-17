

class Trie:
    def __init__(self):
        # 한 글자씩 탐색위해 map 형태로 설정
        self.child = dict()
        # 단어 개수 카운트
        self.count = 0

    def insert(self, word):
        # 루트를 현재 포인터로 설정
        cur = self

        for ch in word:
            # 한 단어 추가될 것이므로 노드 카운트 + 1
            cur.count += 1

            # 만약 ch가 없다면
            if ch not in cur.child:
                # 해당 ch를 자식 Trie 노드로 생성
                cur.child[ch] = Trie()

            # 자식 노드로 현재 포인터 이동
            cur = cur.child[ch]

        # 마지막 노드 카운트 + 1
        cur.count += 1

    def search(self, word):
        # 루트를 현재 포인터로 설정
        cur = self

        for ch in word:

            # 만약 ch가 없다면
            if ch not in cur.child:
                return 0

            # 자식 노드로 현재 포인터 이동
            cur = cur.child[ch]

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
