old_data = [32432,4532, 34343, 345, 565, 5345.89, 45435.54]
new_data = [12432,5532, 18343, 145, 5325, 32345.59, 15435.54]

difference = map(lambda x,y: x-y, new_data,old_data)

print difference