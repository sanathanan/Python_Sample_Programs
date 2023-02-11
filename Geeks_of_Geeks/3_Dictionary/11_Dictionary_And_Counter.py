"""
Given an array of names of candidates in an election. A candidate name in the array represents a vote cast to the candidate.
Print the name of candidates received Max vote. If there is tie, print a lexicographically smaller name.

Input :  votes[] = {"john", "johnny", "jackie",
                    "johnny", "john", "jackie",
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny",
                    "john"};
Output : John
We have four Candidates with name as 'John',
'Johnny', 'jamie', 'jackie'. The candidates
John and Johny get maximum votes. Since John
is alphabetically smaller, we print it.
"""
# Method 1
print("---------Method 1 ----------")
votes= ["john", "johnny", "jackie",
           "johnny", "john", "jackie",
           "jamie", "jamie", "john",
           "johnny", "jamie", "johnny",
           "john"]

dict_1 = {}

for i in votes:
    if i not in dict_1:
        dict_1[i] = 1
    else:
        dict_1[i] += 1
print("Total Number of Votes for Each Candidate:", dict_1)

max_values = max(dict_1.values())
print("Max Value is: ", max_values)

lst = []
for i,j in dict_1.items():
    if j == max_values:
       lst.append(i)
print("The max vote person is :", lst)
print("Printing the smaller name: ",sorted(lst)[0])

# Method 2
from collections import Counter
print("--------Method 2 ---------")
votes2= ["john", "johnny", "jackie",
           "johnny", "john", "jackie",
           "jamie", "jamie", "john",
           "johnny", "jamie", "johnny",
           "john"]

votes_count = Counter(votes2)
print("Votes for each candidate: ", votes_count)

max_vote = max(votes_count.values())
print("Maximum vote is: ",max_vote)

lst_2 = [i for i in votes_count if votes_count[i] == max_vote]
# for i in votes_count:
#     if votes_count[i] == max_vote:
#         lst_2.append(i)
print("Maximum Vote got by: ", lst_2)
print("Printing the smaller name: ",sorted(lst_2)[0])

