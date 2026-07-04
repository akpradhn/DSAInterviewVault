class Solution:
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []

        for day, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                previous_day = stack.pop()
                answer[previous_day] = day - previous_day
            stack.append(day)

        return answer
