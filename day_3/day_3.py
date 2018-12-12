#part-1

words = []
with open('input.txt') as file:
    for line in file:
        words.append(line.strip())
        
M = [[0 for x in range(1000)] for y in range(1000)] 

for line in words:
    claim_id = line[:line.index('@')-1]
    pos_x = int(line[line.index('@')+1:line.index(',')])
    pos_y = int(line[line.index(',')+1:line.index(':')])
    width = int(line[line.index(':')+2:line.index('x')])
    height = int(line[line.index('x')+1:])
    for i in range(pos_y, pos_y+height):
        for j in range(pos_x, pos_x+width):
            M[i][j] += 1

count = 0

for i in range(0, 1000):
    for j in range(0, 1000):
        if M[i][j] >= 2:
            count += 1
print(count)
    

#part-2

for line in words:
    claim_id = line[:line.index('@')-1]
    pos_x = int(line[line.index('@')+1:line.index(',')])
    pos_y = int(line[line.index(',')+1:line.index(':')])
    width = int(line[line.index(':')+2:line.index('x')])
    height = int(line[line.index('x')+1:])    
    area = width*height
    count = 0
    for i in range(pos_y, pos_y+height):
        for j in range(pos_x, pos_x+width):
            if M[i][j] == 1:
                count += 1 

    if count == area:
        print(claim_id)
        break
                
                
                
                
                
                
                
                