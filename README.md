# Interview_Prep_Questions
 this is a collection of technical questions gathering from the book "Cracking the Coding Interview" for me to practice for technical interviews.
 
 The questions and answers are as follows answered are as follows:
 1. 8.1 on page 134. Triple Step
    This problem was solved by realizing that the n'th stair can be reached from the n-1,n-2,n-3 stairs respectively. the recursive relationship is that the number of ways to reach the nth stair is the sum of the ways to reach the n-1,n-2,n-3 stairs. The recursive solution followed trivially and was further optimized by establishing a tabulated solution that would never reach a maxrecursiondepth error and was orders of magnitude more efficient.
