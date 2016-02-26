fh = open("A-large-practice.in")

# worsolution, need to take add num_at_shyness_list in every for loop

# def min_people(max_shyness, num_at_shyness_list):
#     num_up = num_at_shyness_list[0]
#     need_to_invite = 0
#     for cur_shyness in xrange(max_shyness+1):
#         if num_up>=max_shyness:
#             return need_to_invite
#         elif num_up < cur_shyness:
#             need_to_invite += 1
#             num_up += 1
#         else:
#             num_up += num_at_shyness_list[cur_shyness]



def min_people(max_shyness, num_at_shyness_list):
    num_up = num_at_shyness_list[0]
    need_to_invite = 0
    for cur_shyness in xrange(1,max_shyness+1):
        if num_up>=max_shyness:
            return need_to_invite
        elif num_up < cur_shyness:
            need_to_invite += 1
            num_up += 1
        num_up += num_at_shyness_list[cur_shyness]
    return need_to_invite
        

file = open('output.txt', 'w')

for line in fh:
    case_number = int(line)
    break
cn = 1
for line in fh:
    line = line.split()
    max_shy = int(line[0])
    shyness_list = [int(i) for i in list(line[1])]
    file.write(
        'Case #'+str(cn)+': '+str(min_people(max_shy, shyness_list))+'\n')
    cn += 1
file.close()
