# In this program you use a List of animal names.
# Write the code to move the elements of the List one place to the left.

list = ['cat','dog','mouse','rat','squirrel','owl','rabbit']
sprong = int(input('Geef sprong: '))
i=0
while i < sprong:
    dummy=list[0]
    list.remove(list[0])
    list.append(dummy)
    i+=1
print(list)








