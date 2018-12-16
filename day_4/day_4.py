#NSFW code, copy at your own risk

#part-1

import operator

list1=[]

with open('input.txt') as file:
    for line in file:
        list1.append(line.strip())
        
sorted_list = sorted(list1)

total_sleep = {}
falling_asleep_time = {}
waking_up_time = {}

temp_guard_num = 0

for line in sorted_list:
    
    if 'Guard' in line:
        
        guard_num = line[line.index('#')+1:line.index('b')-1]
        temp_guard_num = guard_num
                            
    elif 'falls' in line:
        time_of_falling_asleep = line[15:17]
        try:
            falling_asleep_time[temp_guard_num].append(time_of_falling_asleep)
        except KeyError:
            falling_asleep_time[temp_guard_num] = [time_of_falling_asleep]
        
    elif 'wakes' in line:
        time_of_waking_up = line[15:17]
        try:
            waking_up_time[temp_guard_num].append(time_of_waking_up)
        except KeyError:
            waking_up_time[temp_guard_num] = [time_of_waking_up]
        
#        
#print("\n Time different guards fall asleep at: ", falling_asleep_time)
#print("\n Time different guards wake up at: ", waking_up_time)

for guard in list(falling_asleep_time.keys()):
    
    try:
        fl = falling_asleep_time[guard]
        wl = waking_up_time[guard]
#        print(fl)
#        print(wl)
        total_sleep[guard] = sum([int(x2) - int(x1) for (x1, x2) in zip(falling_asleep_time[guard], waking_up_time[guard])])
    except KeyError:
#        print(fl)
        total_sleep[guard] = sum([int(x1) for (x1) in falling_asleep_time[guard]])
    
        
#print("\nTotal sleep per guard:", total_sleep)     
print("\nGuard who slept the most:" , max(total_sleep.items(), key=operator.itemgetter(1))[0])

sleepy_guard = max(total_sleep.items(), key=operator.itemgetter(1))[0]

minutes_slept = []

falling_asleep_time[sleepy_guard] = list(map(int, falling_asleep_time[sleepy_guard]))
waking_up_time[sleepy_guard] = list(map(int, waking_up_time[sleepy_guard]))

for i, j in zip(falling_asleep_time[sleepy_guard], waking_up_time[sleepy_guard]):
    while (i<j):
        minutes_slept.append(i)
        i = i + 1
        
#print(minutes_slept)
print("\nMinute he slept the most: ",max(minutes_slept, key=minutes_slept.count))


#part-2
fuck_this_shit = {}

for guard_i in list(falling_asleep_time.keys()):
    minutes_slept_part2 = []
    falling_asleep_time[guard_i] = list(map(int, falling_asleep_time[guard_i]))
    waking_up_time[guard_i] = list(map(int, waking_up_time[guard_i]))
    for i, j in zip(falling_asleep_time[guard_i], waking_up_time[guard_i]):
        while (i<j):
            minutes_slept_part2.append(i)
            i = i + 1
#    print('\n' + str(guard_i) + ' minutes slept: ', minutes_slept_part2)
    most_slept_minute_freq = minutes_slept_part2.count(max(minutes_slept, key=minutes_slept_part2.count))
#    print(most_slept_minute_freq)
    
    fuck_this_shit[guard_i] = most_slept_minute_freq
    
#print(fuck_this_shit)
print("\nGuard with most slept_freq: " , max(fuck_this_shit, key=fuck_this_shit.get))

fuck_this_dude = max(fuck_this_shit, key=fuck_this_shit.get)

falling_asleep_time[fuck_this_dude] = list(map(int, falling_asleep_time[fuck_this_dude]))
waking_up_time[fuck_this_dude] = list(map(int, waking_up_time[fuck_this_dude]))

minutes_slept_part3 = []
for i, j in zip(falling_asleep_time[fuck_this_dude], waking_up_time[fuck_this_dude]):
    while (i<j):
        minutes_slept_part3.append(i)
        i = i + 1
        
#print(minutes_slept_part3)
print("\nMinute he slept the most-2: ",max(minutes_slept_part3, key=minutes_slept_part3.count))
