email = input("Enter any email id: ")

thisList = email.split("@")

username = thisList[0]
print("\nUsername: ",username)

thisList = thisList[1]
domain = thisList.split(".")

print("Domain name: ",domain[0])
print("Domain: ." + str(domain[1]))
