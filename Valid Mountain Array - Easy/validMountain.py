def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        if A[0] > A[1]:
            return False
        updown = 0 # it checks if mountain is rising only or not
        direction = 1 # if direction = 1 it is up if direction = 0 it is going down
        for i in range(1,len(A)):
            if A[i] == A[i-1]:
                return False
            if direction:
                if A[i] < A[i-1]:
                    direction = 0
                    updown += 1
            else:
                if A[i] > A[i-1]:
                    return False
        if updown:
            return True
        return False 