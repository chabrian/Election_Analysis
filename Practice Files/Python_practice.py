counties = ["Arapahoe","Denver","Jefferson"]

# if counties[1] == "Denver":
# #     print(counties[1])

# if "El Paso" in counties:
# #     print("El Paso is in the list of counties.")
# else:
# #     print("El Paso is not in the list of counties.")

# if "Arapahoe" in counties and "El Paso" in counties:
# #     print("Arapahoe and El Paso are in the list of counties.")
# else:
# #     print("Arapahoe or El Paso is not in the list of counties.")

# if "Arapahoe" in counties or "El Paso" in counties:
# #     print("Arapahoe or El Paso is in the list of counties.")
# else:
# #     print("Arapahoe and El Paso are not in the list of counties.")

# for county in counties:
# #     print(county)

# for num in range(5):
# #     print(num)

# for i in range(len(counties)):
# #     print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# #get keys in dictionary using keys()
# for county in counties_dict.keys():
#     #print(county)

# #print(counties_dict.keys())

# #get values in dictionary using values()
# for voters in counties_dict.values():
#     #print(voters)

# #also get values this way using index
# for county in counties_dict:
#     #print(counties_dict[county])

#also get values using get()
# for county in counties_dict:
#     print(counties_dict.get(county))

#get key-value pairs using items()
# for county, voters in counties_dict.items():
#     print(county, voters)

#print the sentence with key-value pairs
# for county, voters in counties_dict.items():
#      print(f"{county} county has {voters:,} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#to get each dictionary
# for county_dict in voting_data:
#     print(county_dict)

#to print counties in voting_data
# for i in range(len(voting_data)):
#     print(voting_data[i]["county"])

#could also do it this way
# for county_dict in voting_data:
#     print(county_dict['county'])

#to get all values in a dictionary
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

#multiline f-strings
# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
# print(message_to_candidate)

#to format number use f'{value:{width},.{precision}}' where width is number of characters and precision is number of decimal places. 
# comma after width is for thousands separator
#.2f the f stands for floating-point decimal format

for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")

