# Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who like to 
# buy LP record albums. The store rents new videos for $3.00 a night, and oldies for $2.00 
# a night. Write a program that the clerks at Five Star Retro Video can use to calculate the 
# total charge for a customer’s video rentals. The program should prompt the user for the 
# number of each type of video and output the total

print("Mayank - 2203855")
oldVideos = int(input("Enter the number of Old videos rented:"))
newVideos = int(input("Enter the number of new videos rented:"))
totalRent = float(newVideos*3 + oldVideos*2)
print("Rent is : $", totalRent)
