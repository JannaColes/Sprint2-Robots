# Written by:  Jennifer Oliver
# Date Written: August 7, 2023
# Program Description: Portion of code for determining room type

# Function to determine the type of room, Fire, Poison or Person (clapping instead?)
def FindRoomType():
    # 1 = Fire; 2 = Poison; 3 = Person
    RoomList = [1, 2, 3]

    while True:
        Room = int(input("Enter the room number: "))

        if Room == 1:
            # Call function for FireRoom()
            print(" ")
        elif Room == 2:
            # Call function for PoisonRoom()
            print(" ")
        elif Room == 3:
            PersonRoomType()
            print("Person search and rescue completed successfully! ")
        elif Room not in RoomList:
            print("Error- not a valid room type")
        else:
            return Room
