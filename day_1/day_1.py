#part-1
freqs = []

with open('input.txt') as file:
    for freq in file:
        freqs.append((int(freq.strip())))
    
print(sum(freqs))


#part-2   
import itertools
seen = {0}
totes = 0

for f in itertools.cycle(freqs):

    totes += f
    if totes in seen:
        print((totes))
        break
        
    else:
        seen.add(totes)
        
