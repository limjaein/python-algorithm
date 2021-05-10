# Trie 란?
# 문자열을 저장하고 효율적으로 탐색하기 위한 트리 형태의 자료구조
# radix tree 혹은 prefix tree라고도 함
# 검색어 자동완성, 사전에서 찾기, 문자열 검사 등으로 활용
# 시간 복잡도가 문자열의 길이가 된다

def solution(words, queries):
    answer = []
    trie_words = {}
    trie_words_r = {}

    for word in words:
        if len(word) not in trie_words:
            trie_words[len(word)] = Trie()
            trie_words_r[len(word)] = Trie()
        trie_words[len(word)].insert(word)
        trie_words_r[len(word)].insert(word[::-1])

    for query in queries:
        if len(query) not in trie_words:
            answer.append(0)
            continue

        if query[0] == '?':
            answer.append(trie_words_r[len(query)].search(query[::-1].replace('?', '')))
        else:
            answer.append(trie_words[len(query)].search(query.replace('?', '')))
    return answer


class Trie:
    def __init__(self):
        self.child = dict()
        self.count = 0

    def insert(self, word):
        cur = self

        for ch in word:
            cur.count += 1
            if ch not in cur.child:
                cur.child[ch] = Trie()
            cur = cur.child[ch]
        cur.count += 1

    def search(self, word):
        cur = self

        for ch in word:
            if ch not in cur.child:
                return 0
            cur = cur.child[ch]
        return cur.count


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"]
               , ["fro??", "????o", "fr???", "fro???", "pro?"]))