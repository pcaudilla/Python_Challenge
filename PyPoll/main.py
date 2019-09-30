import os
import csv
import collections as ct

election_data = os.path.join("..", "Resources", "election_data.csv")

khan_votes = []
correy_votes = []
li_votes = []
otooley_votes = []   


print("Election Results")
print("-----------------------------")

with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for vote in csvreader:
        candidate = vote[-1]

        if candidate == "Khan":
            khan_votes.append(candidate)

        elif candidate == "Correy":
            correy_votes.append(candidate)  
        
        elif candidate == "Li":
            li_votes.append(candidate) 

        else:
            otooley_votes.append(candidate) 

    total_votes = len(khan_votes) + len(correy_votes) + len(li_votes) + len(otooley_votes)    

    khan_vote_ptg = (len(khan_votes) / total_votes) * 100
    correy_vote_ptg = (len(correy_votes) / total_votes) * 100
    li_vote_ptg = (len(li_votes) / total_votes) * 100
    otooley_vote_ptg = (len(otooley_votes) / total_votes) * 100


    print(f"Total Votes: {(total_votes)}")

    print("-----------------------------")

    print(f"Khan: {round(khan_vote_ptg, 3)}% ({len(khan_votes)})")

    print(f"Correy: {round(correy_vote_ptg, 3)}% ({len(correy_votes)})")

    print(f"Li: {round(li_vote_ptg, 3)}% ({len(li_votes)})")

    print(f"O'Tooley: {round(otooley_vote_ptg, 3)}% ({len(otooley_votes)})")

    print("-----------------------------")

    if (len(khan_votes) > len(correy_votes)) and (len(khan_votes) > len(li_votes)) and (len(khan_votes) > len(otooley_votes)):
        print("Winner: Khan")
    elif (len(correy_votes) > len(khan_votes)) and (len(correy_votes) > len(li_votes)) and (len(correy_votes) > len(otooley_votes)):
        print("Winner: Correy")
    elif (len(li_votes) > len(khan_votes)) and (len(li_votes) > len(correy_votes)) and (len(li_votes) > len(otooley_votes)):
        print("Winner: Li")
    else: 
        print("Winner: O'Tooley")
    
    print("-----------------------------")


