#You are given an array A representing heights of students. All the students are asked to stand in rows.
# The students arrive by one, sequentially (as their heights appear in A).
# For the i-th student, if there is a row in which all the students are taller than A[i],
# the student will stand in one of such rows. If there is no such row, the student will create a new row.
# Your task is to find the minimum number of rows created.

# Write a function that, given a non-empty array A containing N integers, denoting the heights of the students, returns the minimum number of rows created.
#
# For example, given A = [5, 4, 3, 6, 1], the function should return 2.

def smallIndex(array,num):
    newlist = []
    for i in array:
        if num<i:
            newlist.append(i)
    try:
        return array.index(max(newlist))
    except:
        return -1

def solution(A):
    rows = []
    for stud in A:
        if len(rows)==0:
            rows = [A[0]]
            continue
        replace = smallIndex(rows,stud)
        if replace == -1:
            rows.append(stud)
        else:
            rows[replace]=stud
    return len(rows)


S = [5,4,3,6,1]
print(solution(S))

