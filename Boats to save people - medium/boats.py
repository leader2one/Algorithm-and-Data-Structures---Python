class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        output = 0
        people.sort()
        left = 0
        right = len(people)-1
        while (left <= right):
            if people[right] + people[left] <= limit:
                left += 1
            right -=1
            output += 1
        return output