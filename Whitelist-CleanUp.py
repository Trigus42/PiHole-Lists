##Save only entries of whitelist, which are actually in gravitiy list
ad = open("gravity.list", "r", encoding="ISO-8859-1")
wh_old = list(open("whitelist.txt", "r", encoding="ISO-8859-1"))

try:
	open("whitelist_new.txt", "x")
except FileExistsError:
	if("J" == input("Are you sure, you want to overwrite whitelist_new.txt? (J/N) >").upper()):
		open("whitelist_new.txt", "w")
	elif("J" == input("Do you want to append new entries to the existing file? Caution: You may get dublicates! (J/N) >").upper()):
		pass
	else:
		exit()

wh_new = open("whitelist_new.txt", "a")

for y in ad:
	for x in wh_old:
		if(x == y):
			wh_new.write(x)

wh_new.close()
print("Done")

##Merge two lists without dublicates in linux. "sort -um list1.txt list2.txt > list.merge"
