
# TASKS 1 ================================ 
# Find the total score
# ========================================
# total score = ?

# Read the input text file:
with open('input.txt') as f:
    input = f.readlines()

# print(input[:20])

# Clean input:
cleaned_input = []
for item in input:
    item = item.strip()
    item = item.replace(" ", "")
    cleaned_input.append(item)

# print(cleaned_input[:20])

# Make a dict of all the possible combinations:
# A: Paper, B: Scissors, C: Rock
# X: Paper, Y: Scissors, Z: Rock
score_map = {
    'AX': 1 + 3,
    'BX': 1 + 0,
    'CX': 1 + 6,
    
    'AY': 2 + 6,
    'BY': 2 + 3,
    'CY': 2 + 0,

    'AZ': 3 + 0,
    'BZ': 3 + 6,
    'CZ': 3 + 3,
}

# Calculate total score:
total_score = 0
for item in cleaned_input:
    total_score += score_map[item]

print("Total Score: ", total_score)



# TASKS 2 ================================ 
# Find total score but description changed. 
# ========================================

# First column, RPC and second column If you need to loose draw or win
# Desc:    A: Rock  B: Paper C: Scissors
#          X: loose Y: draw  Z: win
#You play: B: paper B: paper A: Rock

# Figure out what you need to show:
your_hand = {
    'AX': 'AC',
    'BX': 'BA',
    'CX': 'CB',
    
    'AY': 'AA',
    'BY': 'BB',
    'CY': 'CC',

    'AZ': 'AB',
    'BZ': 'BC',
    'CZ': 'CA',
    
}


updated_score_map = {
    'AA': 1 + 3,
    'BA': 1 + 0,
    'CA': 1 + 6,
    
    'AB': 2 + 6,
    'BB': 2 + 3,
    'CB': 2 + 0,

    'AC': 3 + 0,
    'BC': 3 + 6,
    'CC': 3 + 3,
}

# Calculate total score with new description:
new_total_score = 0

for item in cleaned_input:
    myHand = your_hand[item]
    new_total_score += updated_score_map[myHand]

print("New Total Score: ", new_total_score)