class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort()
        indexed_queries = sorted((query, i) for i, query in enumerate(queries))
        answer = [-1] * len(queries)
        heap = []
        interval_index = 0

        def push(item):
            heap.append(item)
            child = len(heap) - 1
            while child > 0:
                parent = (child - 1) // 2
                if heap[parent] <= heap[child]:
                    break
                heap[parent], heap[child] = heap[child], heap[parent]
                child = parent

        def pop():
            top = heap[0]
            last = heap.pop()
            if heap:
                heap[0] = last
                parent = 0
                while True:
                    left = parent * 2 + 1
                    right = left + 1
                    smallest = parent

                    if left < len(heap) and heap[left] < heap[smallest]:
                        smallest = left
                    if right < len(heap) and heap[right] < heap[smallest]:
                        smallest = right
                    if smallest == parent:
                        break

                    heap[parent], heap[smallest] = heap[smallest], heap[parent]
                    parent = smallest
            return top

        for query, original_index in indexed_queries:
            while interval_index < len(intervals) and intervals[interval_index][0] <= query:
                start, end = intervals[interval_index]
                push((end - start + 1, end))
                interval_index += 1

            while heap and heap[0][1] < query:
                pop()

            if heap:
                answer[original_index] = heap[0][0]

        return answer
