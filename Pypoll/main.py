import os
import csv

filepath=os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("pypoll_analysis.txt")   

total_votes=0
candidates_list=[]
candidate_dictionary={}
total_votes_candidate=0
winner_votes=0

with open(filepath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    header=next(csvreader)

    for row in csvreader:
        total_votes+=1
        candidate_name=row[2]
        if candidate_name not in candidate_dictionary.keys():
            # candidates_list.append(candidate_name)
            candidate_dictionary[candidate_name]={'votes':1, 'percentage':1}
        elif candidate_name in candidate_dictionary.keys():
            candidate_dictionary[candidate_name]['votes']=candidate_dictionary[candidate_name]['votes']+1
        
        # candidate_dictionary[candidate_name]["votes"]=candidate_dictionary[candidate_name]["votes"]+1
        
output_1=(f"Election Results\n"
            f"-----------------------------\n"
            f"Total Votes: {total_votes}\n")
print(f"Election Results\n"
            f"-----------------------------\n"
            f"Total Votes: {total_votes}\n")

for k, v in candidate_dictionary.items():
    percent=round(v['votes']/total_votes*100)  
    v['percentage'] =percent 
    if percent>50:
        winner=k
    output_2=(f"{k} : {v['percentage']}% ({ v['votes']}) ")
    print(f"{k} : {v['percentage']}% ({ v['votes']}) ")  

output_3= (f"-----------------------------\n"
        f"Winner:{winner}\n")
print(f"-----------------------------\n"
        f"Winner:{winner}\n")
