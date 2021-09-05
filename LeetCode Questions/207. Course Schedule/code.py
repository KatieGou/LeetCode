class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses=dict()
        for numCourse in range(numCourses):
            courses[numCourse]=0
        for prerequisite in prerequisites:
            courses[prerequisite[0]]+=1
        while courses:
            v=list(courses.values())
            if all(v):
                return False
            can_takes=[k for k,v in courses.items() if v == 0]
            for can_take in can_takes:
                for prerequisite in prerequisites:
                    if prerequisite[1]==can_take:
                        courses[prerequisite[0]]-=1
                courses.pop(can_take)
        return True
