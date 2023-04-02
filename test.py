import numpy as np

Black = [(9,9), (8,3)]
    


global_array = [
        [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
        [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
        [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
        [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
        [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
]
        
print('Row:{}'.format(len(global_array)))
print('Col:{}'.format(len(global_array[0])))

# (6,6)
global_array[0][0].append((1, 8))
global_array[0][0].append((2, 11))
global_array[0][0].append((1, 16))

print(global_array[0][0][:])
