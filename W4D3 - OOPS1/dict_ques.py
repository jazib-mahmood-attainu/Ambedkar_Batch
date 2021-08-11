"""
Given a list of city results, which party won?
"""

parties = ["BJP","BJP","BJP","Congress","Congress","AAP","AAP","AAP","AAP"]

freq = dict()

for party in parties:
    if party not in freq:
        freq[party] = 1
    else:
        freq[party] += 1

print(freq)
winning_party = ""
max_votes = 0
#freq = {'BJP': 3, 'Congress': 2, 'AAP': 4}
for key in freq.keys():
    if max_votes<freq[key]:
        max_votes = freq[key]
        winning_party = key

print("winning party is",winning_party)