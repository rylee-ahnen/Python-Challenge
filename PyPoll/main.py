import os
import csv

# Declare variables
voter_id = []
county = []
candidate = []
candidate_dict = {}
total_votes = 0
winning_votes = 0
winner = ""

# read in the file
csvpath = os.path.join('.', 'Resources', 'election_data.csv')
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)
    # print(csvheader)

# Read list into variables and append data
    for row in csvreader:
        voter = row[0]
        voter_id.append(voter)
        location = row[1]
        county.append(location)
        selection = row[2]
        candidate.append(selection)

#calculate total votes
total_votes = (len(voter_id)-1)
# print(total_votes)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Create the candidate list
candidate_list = list(set(candidate))

# Count votes per candidate
cand_one_tally = candidate.count(candidate_list[0])
cand_one_share = ((cand_one_tally/total_votes)*100)
cand_two_tally = candidate.count(candidate_list[1])
cand_two_share = ((cand_two_tally/total_votes)*100)
cand_three_tally = candidate.count(candidate_list[2])
cand_three_share = ((cand_three_tally/total_votes)*100)
cand_four_tally = candidate.count(candidate_list[3])
cand_four_share = ((cand_four_tally/total_votes)*100)

# Finding Winner
vote_share = []
vote_share.append(cand_one_tally)
vote_share.append(cand_two_tally)
vote_share.append(cand_three_tally)
vote_share.append(cand_four_tally)
highest = vote_share.index(int(max(vote_share)))
winner = candidate_list[highest]

# More Printing
# print("-------------------------")
# print(f"  : {cand_two_share}% ({cand_two_tally})")
# print(f"Correy: {cand_one_share}% ({cand_one_tally})")
# print(f"   : {cand_three_share}% ({cand_three_tally})")
# print(f"   : {cand_four_share}% ({cand_four_tally})")

# Truncate vote shares
cand_one_share_round = round(cand_one_share, 3)
cand_two_share_round = round(cand_two_share, 3)
cand_three_share_round = round(cand_three_share, 3)
cand_four_share_round = round(cand_four_share, 3)

# More Variables
one_1 = candidate_list[0] 
two_1 = cand_one_share_round
three_1 = cand_one_tally

one_2 = candidate_list[1]
two_2 = cand_two_share_round
three_2 = cand_two_tally

one_3 = candidate_list[2]
two_3 = cand_three_share_round
three_3 = cand_three_tally

one_4 = candidate_list[3]
two_4 = cand_four_share_round
three_4 = cand_four_tally

# Actually More Printing
print(f"{one_1}: {two_1}% ({three_1})")
print(f"{one_2}: {two_2}% ({three_2})")
print(f"{one_3}: {two_3}% ({three_3})")
print(f"{one_4}: {two_4}% ({three_4})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Create the text file
text_file = open("pypoll.txt", "w")
text_file.write("Election Results")
text_file.write("\n")
text_file.write("-------------------------")
text_file.write("\n")
text_file.write(f"Total Votes: {total_votes}")
text_file.write("\n")
text_file.write("-------------------------")
text_file.write("\n")
text_file.write(f"{one_1}: {two_1}% ({three_1})")
text_file.write("\n")
text_file.write(f"{one_2}: {two_2}% ({three_2})")
text_file.write("\n")
text_file.write(f"{one_3}: {two_3}% ({three_3})")
text_file.write("\n")
text_file.write(f"{one_4}: {two_4}% ({three_4})")
text_file.write("\n")
text_file.write("-------------------------")
text_file.write("\n")
text_file.write(f"Winner: {winner}")
text_file.write("\n")
text_file.write("-------------------------")