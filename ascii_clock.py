# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Xander Tivis
# Section:      535
# Assignment:   Lab #, Assignment #
# Date:         

digits = {
    '0': ["###", "# #", "# #", "# #", "###"],
    '1': [" # ", "## ", " # ", " # ", "###"],
    '2': ["###", "  #", "###", "#  ", "###"],
    '3': ["###", "  #", "###", "  #", "###"],
    '4': ["# #", "# #", "###", "  #", "  #"],
    '5': ["###", "#  ", "###", "  #", "###"],
    '6': ["###", "#  ", "###", "# #", "###"],
    '7': ["###", "  #", "  #", "  #", "  #"],
    '8': ["###", "# #", "###", "# #", "###"],
    '9': ["###", "# #", "###", "  #", "###"],
    ':': ["   ", " : ", "   ", " : ", "   "],
    'A': [" A ", "A A", "AAA", "A A", "A A"],
    'P': ["PPP", "P P", "PPP", "P  ", "P  "],
    'M': ["M   M", "MM MM", "M M M", "M   M", "M   M"]
}

time_input = input("Enter the time: ")
clock_type = input("Choose the clock type (12 or 24): ")
valid_chars = "abcdeghkmnopqrsuvwxyz@$&*="
char = input("Enter your preferred character: ")
if char == "":
    char = None
else:
    while True:
        if char not in valid_chars:
            char = input("Character not permitted! Try again: ")
        else:
            break

if len(time_input) == 5:
    hour = (int(time_input[:2]))
    minute = (int(time_input[3:]))
elif len(time_input) == 4:
    hour = (int(time_input[:1]))
    minute = (int(time_input[2:]))
else:
    print('no pls')

period = ""

if clock_type == "12":
    if hour == 0:
        hour = 12
        period = "AM"
    elif hour == 12:
        period = "PM"
    elif hour > 12:
        hour -= 12
        period = "PM"
    else:
        period = "AM"
        
display = f"{hour}:{minute:02d}"

if period:
    display += period
lines = ["", "", "", "", ""]

for i in display:
    art = digits[i]
    for j in range(5):
        symbol = i if char is None else char
        lines[j] += art[j].replace("#", symbol) + " "
        
for line in lines:
    print(line)
