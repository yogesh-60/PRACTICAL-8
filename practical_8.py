file=open("practical-8.txt",'w')
list=[3,2,1.5,5,7,6,4,3]
file.write("Before sorting:")
file.write(str(list))
list.sort()
file.write(f"\nAfter sorting in Ascending order: {str(list)}")
list.sort(reverse=True)
file.write(f"\nAfter sorting in Descending order: {str(list)}")