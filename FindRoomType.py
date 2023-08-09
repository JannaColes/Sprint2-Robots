# Written by:  Jennifer Oliver
# Date Written: August 7, 2023
# Program Description: Portion of code for determining room type (Branch 1)

# Function to determine the type of room, Fire, Poison or Person
# not sure if its supposed to be inputs or not...
def FindRoomType():
    # 1 = Fire; 2 = Poison; 3 = Person
    RoomList = [1, 2, 3]

    while True:
        RoomType = int(input("Enter the room type's corresponding number (1-3): "))

        if RoomType == 1:
            # Call function for FireRoom()
            print(" ")
        elif RoomType == 2:
            # Call function for PoisonRoom()
            print(" ")
        elif RoomType == 3:
            PersonRoomType()
            print("Person search and rescue completed successfully! ")
        elif RoomType not in RoomList:
            print("Error- not a valid room type")
        else:
            return RoomType
