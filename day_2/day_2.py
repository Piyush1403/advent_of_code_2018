#part-1

words = []

with open('input.txt') as file:
    for line in file:
        words.append(line.strip())
        
twice = 0
thrice = 0    
for word in words:
    alpha = {}
    for letter in word:
        if letter not in alpha:
            alpha[letter] = 1
        else:
            alpha[letter] += 1
    for key in alpha:
        if alpha[key] == 2:
            twice += 1
            break
    for key in alpha:
        if alpha[key] == 3:
            thrice += 1
            break
        
print(twice*thrice)
            

#part-2

for i in range(len(words)):
    for j in range(i+1, len(words)):
        different_letters = 0
        for l in range(len(words[i])):
            if words[i][l] != words[j][l]:
                different_letters += 1
        if different_letters == 1:            
            first_word = words[i]
            second_word = words[j]
        
for x,y in zip(first_word, second_word):
    if x==y:
        print(x, end='')
        
        
        
        
        
        
        
        
        
        
        
        
        
        