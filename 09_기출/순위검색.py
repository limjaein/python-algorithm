import heapq
from bisect import bisect_left


def solution(info, query):
    answer = []
    trie = Trie()

    for i in info:
        trie.insert(i)

    for q in query:
        answer.append(findCnt(trie, q.replace(" and ", " ").split(" ")))

    return answer


class Trie:
    def __init__(self):
        self.child = dict()
        self.score = []

    def insert(self, info_str):
        cur = self

        # 조건 전체 조회
        for info in info_str.split(" "):
            # 숫자라면 배열 처리
            if info.isdigit():
                cur.score.append(int(info))
                cur.score.sort()
            else:
                # 해당 조건이 없다면 추가
                if info not in cur.child:
                    cur.child[info] = Trie()
                cur = cur.child[info]


def findCnt(trie, infos):
    cur = trie
    cnt = 0

    for idx, info in enumerate(infos):
        # 숫자라면 점수 조회
        if info.isdigit():
            score_idx = bisect_left(cur.score, int(info))
            return len(cur.score) - score_idx

        # '-' 조건이면 전체 카운트 sum
        if info == '-':
            for ch in cur.child:
                cnt += findCnt(cur.child[ch], infos[idx+1:])
            return cnt
        else:
            # 조건에 해당하는 지원자가 있을 경우
            if info in cur.child:
                cur = cur.child[info]
            else:
                return 0