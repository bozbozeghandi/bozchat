test = [3,-1,2]
max_ha_chapo_rast =[]	
max_haye_akhar = []

def bigest_finder(test):
	global max_ha_chapo_rast
	# global max_haye_akhar
	left_list = []
	right_list = []
	sum_right = []
	sum_left =[]
	

	if len(test) <= 1:
		max_ha_chapo_rast.append(max(test))
		# max_haye_akhar.append(max(test))
		# if len(max_haye_akhar) == 2:
		# 	max_haye_akhar.append(max_haye_akhar[0] + max_haye_akhar[1])

	else:
		for i in range(int(len(test)/2)):
			left_list.append(test.pop(0))
		right_list = test


		sum_right.append(0)
		c=0
		for i in right_list:
			sum_right.append(i+sum_right[c])
			c+=1
			print(sum_right)


		sum_left.append(0)
		c=0
		for i in reversed(left_list):
			sum_left.append(i+sum_left[c])
			c+=1
			print(sum_left)
		
		max_ha_chapo_rast.append(max(sum_left)+max(sum_right))

		bigest_finder(left_list)
		bigest_finder(right_list)



bigest_finder(test)
print(max_ha_chapo_rast)

