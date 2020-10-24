# cook your dish here
N = 10
tables = list()
dist_from_left = list()
dist_from_right = list()

# function is used to debug tables, dist_from_left & dist_from_right array
def print_all():
    print('--------------------------------------')
    for i in range(0, N):
        print(str("{0:0=2d}".format(tables[i])) + " ", end = '')
    print()
    
    for i in range(0, N):
        print(str("{0:0=2d}".format(dist_from_left[i])) + " " ,end = '')
    print()
        
    for i in range(0, N):
        print(str("{0:0=2d}".format(dist_from_right[i])) + " " ,end = '')
    print()
    print('--------------------------------------')
    
# Initialize the value of array
def init():
    z = 0
    while (z < N):
        tables.append(-1)
        dist_from_right.append(N)
        dist_from_left.append(N)
        z=z+1

# after allocating and vacating a table dist_from_left & dist_from_right is updated
def update_table_distance(table_index):
    # update dist_from_left
    for i in range(table_index, N):
        # update only if there is no nearer occupied table
        if dist_from_left[i] > (i - table_index):
            dist_from_left[i] = i - table_index
        
    # Update dist_from_right
    for i in range(table_index, -1, -1):
        if dist_from_right[i] > (table_index-i):
            dist_from_right[i] = table_index-i
    
    # this table is occupied    
    tables[table_index] = 1

# assign table 
def assign_table():
    #print_all()
    table_no = 1
    
    final_max_dist = -1
    current_max_dist = N
    
    
    for i in range(0, N):
        current_max_dist = min(dist_from_left[i], dist_from_right[i])
        if current_max_dist > final_max_dist: # > takes care of nearer to the entry
            final_max_dist = current_max_dist
            table_no = i + 1

    # Update dist_from_left & dist_from_right after finding the table
    update_table_distance(table_no - 1)

    return table_no;


# we're assuming the table_index user is sending is validated
def vacate_table(table_index):
    # vacate the table in tables array
    tables[table_index] = -1
    
    # udpate dist_from_left
    i = table_index
    old_value = 0
    curr_value = 0
    if table_index != 0:
        old_value = dist_from_left[table_index-1]
    
    while i < N:
        # Update the array with previous value(value before the table was assigned)
        if dist_from_left[i] == curr_value:
            dist_from_left[i] = old_value+1
            old_value = old_value + 1
            curr_value = curr_value + 1
        else:
            break;
        
        i=i+1
        
            
    # Update dist_from_right
    i = table_index
    old_value = 0
    curr_value = 0
    if table_index != N:
        old_value = dist_from_right[table_index + 1]
    
    while i >= 0:
        # Update the array with previous value(value before the table was assigned)
        if dist_from_right[i] == curr_value:
            dist_from_right[i] = old_value+1
            old_value = old_value + 1
            curr_value = curr_value + 1
        else:
            break;
        
        i=i-1



def main():
    print(assign_table())
    print(assign_table())
    print(assign_table())
    print_all()
    vacate_table(4)
    print_all()
    print(assign_table())
  
    
init() 
main()
    