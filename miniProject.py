from doctest import master
from tkinter import *
from PIL import ImageTk,Image
import json
root = Tk()
root.title("CDY CAB SERVEICE")
root.config(bg='#D9D8D7')
root.geometry("500x500")

def userLogin():
    while True:
        print("---- WELCOME TO USER LOGIN ----")
        print("Vehicle Categories\nCar\nVan\n3 Wheeler\nLorry\nTruck\n")
        vehicleCategory = input("What kind of vehicle do you need:- ")

        # User Input checking Part
        if (vehicleCategory == "Car"):
            while True:

                # Check the input passenger range
                passenger = int(input("Select number of passengers:- "))
                if (passenger == 3 or passenger == 4):
                    print("Select what category of a Car: \nChoose AC or NonAC: \n")
                    break
                else:
                    print("Select passengers between 3 and 4: \n")

        elif (vehicleCategory == "Van"):
            while True:
                passenger = int(input("Select number of passengers:- "))
                if (passenger == 3 or passenger == 4):
                    print("Select what category of a Van\nChoose AC or NonAC\n")
                    break
                else:
                    print("Select passengers between 3 and 4:\n")
        elif (vehicleCategory == "Wheeler"):
            print("Select a Wheeler")
        elif (vehicleCategory == "Lorry"):
            print("Max Load & Size: 2500kg and 3500kg\nYou Can Select a Lorry\n")
        elif (vehicleCategory == "Truck"):
            print("Size: 20ft and 10ft\nYou Can Select a Truck\n")

def adminLogin():
    while True:
        print("---- WELCOME TO ADMIN LOGIN ----")

        print("\n(1) ENTER 1 TO ADD A NEW VEHICLE\n(2) ENTER 2 TO REMOVE A VEHICLE\n(3) ENTER 3 TO ASSIGN A VEHICLE\n(4) ENTER 4 TO RELEASE A VEHICLE\n(5) ENTER 5 TO SEE AVAILABLE VEHICLES\n(6) ENTER 6 TO EXIT\n")
        MenuItems = input("Select a Number Here: ")

        if MenuItems == '6':
            break

        # MenuItems 01 Add Vehicle Part
        elif MenuItems == '1':
            addVehicle = input("ENTER A VEHICLE CATEGORY TO ADD(\nCar\nVan\nWheeler\nTruck\nLorry\n)\n:- ")
            if (addVehicle == "Car"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Cars = obj['Cars']
                AvailableCars = obj['AvailableCars']
                name = input("Enter Name of the Car: ")
                number = int(input("Enter Number of the Car: "))
                category = input("Enter Category of the Car: ")

                CarDic = {
                    'name': name,
                    'number': number,
                    'category': category,
                }
                Cars.append(CarDic)
                print("--- THE NEW CAR WAS ADDED SUCCESSFULLY ---")
                f.close()

                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (addVehicle == "Van"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Vans = obj['Vans']
                AvailableVans = obj['AvailableVans']
                name = input("Enter Name of the Van: ")
                number = int(input("Enter Number of the Van: "))
                category = input("Enter Category of the Van: ")

                vanDic = {
                    'name': name,
                    'number': number,
                    'category': category
                }
                Vans.append(vanDic)
                print("--- THE NEW VAN WAS ADDED SUCCESSFULLY ---")
                f.close()

                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (addVehicle == "Wheeler"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Wheelers = obj['Wheelers']
                AvailableWheelers = obj['AvailableWheelers']
                name = input("Enter Name of the Wheeler: ")
                number = int(input("Enter Number of the Wheeler: "))
                category = input("Enter Category of the Wheeler: ")

                WheelerDic = {
                    'name': name,
                    'number': number,
                }
                Wheelers.append(WheelerDic)
                print("--- THE NEW 3WHEELER WAS ADDED SUCCESSFULLY ---")
                f.close()

                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (addVehicle == "Lorry"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Lorries = obj['Lorries']
                AvailableLorries = obj['AvailableLorries']
                name = input("Enter Name of the Lorry: ")
                number = int(input("Enter Number of the Lorry: "))
                category = input("Enter Category of the Lorry: ")

                LorryDic = {
                    'name': name,
                    'number': number,
                }
                Lorries.append(LorryDic)
                print("--- THE NEW LORRY WAS ADDED SUCCESSFULLY ---")
                f.close()

                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()


            elif (addVehicle == "Truck"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Truks = obj['Truks']
                AvailableTruks = obj['AvailableTruks']
                name = input("Enter Name of the Truck: ")
                number = int(input("Enter Number of the Truck: "))
                category = input("Enter Category of the Truck: ")

                TruckDic = {
                    'name': name,
                    'number': number,
                }
                Truks.append(TruckDic)
                print("--- THE NEW TRUCK WAS ADDED SUCCESSFULLY ---")
                f.close()

                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()


        # MenuItems 02 Remove Vehicle Part
        elif MenuItems == '2':
            removeVehicle = input("ENTER A VEHICLE CATEGORY TO REMOVE(\nCar\nVan\nWheeler\nTruck\nLorry): ")

            if (removeVehicle == "Car"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Cars = obj['Cars']
                AvailableCars = obj['AvailableCars']
                for car in Cars:
                    print("ID", Cars.index(car), " Name:", car['name'], "   Number:", car['number'],
                          "  category:", car['category'])
                removeId1 = int(input("Select the Car ID: "))
                Cars.pop(removeId1)
                print("--- THE CAR WAS REMOVED SUCCESSFULLY ---")
                f.close()

                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (removeVehicle == "Van"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Vans = obj['Vans']
                AvailableVans = obj['AvailableVans']
                for van in Vans:
                    print("ID", Vans.index(van), "Name:", van['name'], "Number:", van['number'],
                          "category:", van['category'])
                removeId2 = int(input("Select the Van ID: "))
                Vans.pop(removeId2)
                print("--- THE VAN WAS REMOVED SUCCESSFULLY ---")
                f.close()

                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (removeVehicle == "Wheeler"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Wheelers = obj['Wheelers']
                AvailableWheelers = obj['AvailableWheelers']
                for wheeler in Wheelers:
                    print("ID", Wheelers.index(wheeler), " Name:", wheeler['name'], "Number:", wheeler['number'], )
                removeId3 = int(input("Select the 3-Wheeler ID: "))
                Wheelers.pop(removeId3)
                "--- THE 3-Wheeler WAS REMOVED SUCCESSFULLY ---"
                f.close()

                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (removeVehicle == "Lorry"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Lorries = obj['Lorries']
                AvailableLorries = obj['AvailableLorries']
                for lorry in Lorries:
                    print("ID", Lorries.index(lorry), " Name:", lorry['name'], "   Number:", lorry['number'], )
                removeId5 = int(input("Select the Lorry ID: "))
                Lorries.pop(removeId5)
                "--- THE LORRY WAS REMOVED SUCCESSFULLY ---"
                f.close()

                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (removeVehicle == "Truck"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Truks = obj['Truks']
                AvailableTruks = obj['AvailableTruks']
                for truck in Truks:
                    print("ID", Truks.index(truck), " Name:", truck['name'], "   Number:", truck['number'],
                          truck[''])
                removeId4 = int(input("Select the Truck ID: "))
                Truks.pop(removeId4)
                "--- THE TRUCK WAS REMOVED SUCCESSFULLY ---"
                f.close()

                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()


        #  MenuItems 03 Assign Vehicle Part
        elif MenuItems == '3':
            assignVehicle = input("ENTER A VEHICLE CATEGORY TO ASSIGN(\nCar\nVan\nWheeler\nTruck\nLorry): ")

            if (assignVehicle == "Car"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Cars = obj['Cars']
                AvailableCars = obj['AvailableCars']
                for car in Cars:
                    print("ID", Cars.index(car), " Name:", car['name'], "   Number:", car['number'],
                          "  category:", car['category'])
                print("Enter \"AC\" for select AC Car\nEnter \"NAC\" for select Non-AC Car\n")
                userInput = input("Select your preferred  type here: ")

                if userInput == 'AC':
                    print("--- You selected the AC Category ---")
                    for car in Cars:
                        if car['category'] == 'AC':
                            dic = car
                            id = Cars.index(car)
                            break
                            f.close()

                elif userInput == 'NAC':
                    print("--- You selected the Non-AC Category ---")
                    for car in Cars:
                        if car['category'] == 'NonAC':
                            dic = car
                            id = Cars.index(car)
                            break
                            f.close()
                AvailableCars.append(dic)
                Cars.pop(id)
                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (assignVehicle == "Van"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Vans = obj['Vans']
                AvailableVans = obj['AvailableVans']
                for van in Vans:
                    print("ID", Vans.index(van), " Name:", van['name'], "   Number:", van['number'],
                          "  category:", van['category'])
                print("Enter \"AC\" for select AC Van\nEnter \"NAC\" for select Non-AC Van\n")
                userInput = input("You selected the AC Category: ")
                if userInput == 'AC':
                    print("--- You selected the AC Category ---")
                    for van in Vans:
                        if van['category'] == 'AC':
                            dic = van
                            id = Vans.index(van)
                            break
                            f.close()

                elif userInput == 'NAC':
                    print("--- You selected the Non-AC Category ---")
                    for van in Vans:
                        if van['category'] == 'NonAC':
                            dic = van
                            id = Vans.index(van)
                            break
                            f.close()
                AvailableVans.append(dic)
                Vans.pop(id)
                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (assignVehicle == "Wheeler"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Wheelers = obj['Wheelers']
                AvailableWheelers = obj['AvailableWheelers']
                for wheeler in Wheelers:
                    print("ID", Wheelers.index(wheeler), " Name:", wheeler['name'], "   Number:", wheeler['number'], )
                    for wheeler in Wheelers:
                        dic = wheeler
                        id = Wheelers.index(wheeler)
                        break
                        f.close()
                AvailableWheelers.append(dic)
                Wheelers.pop(id)
                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (assignVehicle == "Lorry"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Lorries = obj['Lorries']
                AvailableLorries = obj['AvailableLorries']
                f.close()
                for lorry in Lorries:
                    print("ID", Lorries.index(lorry), " Name:", lorry['name'], "   Number:", lorry['number'],
                          lorry[''])
                    for lorry in Lorries:
                        dic = lorry
                        id = Lorries.index(lorry)
                        break
                        f.close()
                AvailableLorries.append(dic)
                Lorries.pop(id)
                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (assignVehicle == "Truck"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Truks = obj['Truks']
                AvailableTruks = obj['AvailableTruks']
                for truck in Truks:
                    print("ID", Truks.index(truck), " Name:", truck['name'], "   Number:", truck['number'], )
                    for truck in Truks:
                        dic = truck
                        id = Truks.index(truck)
                        break
                        f.close()
                AvailableTruks.append(dic)
                Truks.pop(id)
                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()

        # MenuItems 4 Release Vehicle Part
        elif MenuItems == '4':
            releaseVehicle = input("ENTER VEHICLE CATEGORY TO RELEASE(\nCar\nVan\nWheeler\nTruck\nLorry): ")

            if (releaseVehicle == "Car"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Cars = obj['Cars']
                AvailableCars = obj['AvailableCars']
                f.close()
                for car in AvailableCars:
                    print("ID", AvailableCars.index(car), "Name: ", car['name'], "  Number:", car['number'],
                          "  category: ", car['category'])
                userInput = int(input("Enter the Car id: "))
                obj = AvailableCars[userInput]
                AvailableCars.pop(userInput)
                print("--- You Released the Vehicle Successfully ---")
                f.close()

            elif (releaseVehicle == "Van"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Vans = obj['Vans']
                AvailableVans = obj['AvailableVans']

                for van in AvailableVans:
                    print("ID", AvailableVans.index(van), "Name: ", van['name'], "  Number:", van['number'],
                          "  category: ", van['category'])
                userInput = int(input("Enter the Van id: "))
                obj = AvailableVans[userInput]
                Vans.append(obj)
                AvailableVans.pop(userInput)
                print("--- You Released the Vehicle Successfully ---")
                f.close()

            elif (releaseVehicle == "Wheeler"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Wheelers = obj['Wheelers']
                AvailableWheelers = obj['AvailableWheelers']

                for wheeler in AvailableWheelers:
                    print("ID", AvailableWheelers.index(wheeler), "Name: ", wheeler['name'], "  Number:",
                          wheeler['number'], )
                userInput = int(input("Enter the 3-Wheeler id: "))
                obj = AvailableWheelers[userInput]
                Wheelers.append(obj)
                AvailableWheelers.pop(userInput)
                print("--- You Released the Vehicle Successfully ---")
                f.close()

            elif (releaseVehicle == "Lorry"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Lorries = obj['Lorries']
                AvailableLorries = obj['AvailableLorries']

                for lorry in AvailableLorries:
                    print("ID", AvailableLorries.index(lorry), "Name: ", lorry['name'], "  Number:",
                          lorry['number'], )
                userInput = int(input("Enter the Lorry id: "))
                obj = AvailableLorries[userInput]
                Lorries.append(obj)
                AvailableLorries.pop(userInput)
                print("--- You Released the Vehicle Successfully ---")
                f.close()

            elif (releaseVehicle == "Truck"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Truks = obj['Truks']
                AvailableTruks = obj['AvailableTruks']

                for truck in AvailableTruks:
                    print("ID", AvailableTruks.index(truck), "Name: ", truck['name'], "  Number:", truck['number'], )
                userInput = int(input("Enter the Truck id: "))
                obj = AvailableTruks[userInput]
                Truks.append(obj)
                AvailableTruks.pop(userInput)
                print("--- You Released the Vehicle Successfully ---")
                f.close()

        # MenuItems 05 Check Available Vehicle Part
        elif MenuItems == '5':
            print("--- CURRENTLY AVAILABLE VEHICLES ---")
            CheckAvailability = input(
                "ENTER A VEHICLE CATEGORY TO SEE THE AVAILABILITY(\nCar\nVan\nWheeler\nTruck\nLorry): ")

            if (CheckAvailability == "Car"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Cars = obj['Cars']
                AvailableCars = obj['AvailableCars']

                for car in Cars:
                    print("ID", Cars.index(car), "Name: ", car['name'], "  Number: ", car['number'],
                          "category: ", car['category'])
                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (CheckAvailability == "Van"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Vans = obj['Vans']
                AvailableVans = obj['AvailableVans']

                for van in Vans:
                    print("ID", Vans.index(van), " Name:", van['name'], "   Number:", van['number'],
                          " category:", van['category'])
                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (CheckAvailability == "Wheeler"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Wheelers = obj['Wheelers']
                AvailableWheelers = obj['AvailableWheelers']

                for wheeler in Wheelers:
                    print("ID", Wheelers.index(wheeler), " Name:", wheeler['name'], "   Number:", wheeler['number'], )
                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (CheckAvailability == "Lorry"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Lorries = obj['Lorries']
                AvailableLorries = obj['AvailableLorries']

                for lorry in Lorries:
                    print("ID", Lorries.index(lorry), " Name:", lorry['name'], "   Number:", lorry['number'], )
                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (CheckAvailability == "Truck"):
                f = open('vehicleDetails.json', 'r')
                obj = json.load(f)
                Trucks = obj['Trucks']
                AvailableTrucks = obj['AvailableTrucks']

                for truck in Truks:
                    print("ID", Truks.index(truck), " Name:", truck['name'], "   Number:", truck['number'], )
                f = open('vehicleDetails.json', 'w')
                json.dump(obj, f)
                f.close()

back=Image.open('E:\BSE OUSL\2nd Semester\EEI3372 - Programming in Python\pic1')
back_end=ImageTk.PhotoImage(back)
root.geometry("508x340")
lbl=Label(master,image=back_end)
lbl.place(x=0,y=0)

Label(root, text="WELCOME TO CDY CAB SERVEICE ", font="Arial 20 bold "). grid(row=0, column=2)

userLabel = Label(root, text='Customer Login:- ', font=('Arial', 11,"bold"), background="cyan")
userLabel.place(x=20, y=60)

Custbtn = Button(text="USER", command=userLogin, font=('Arial', 11,"bold"))
Custbtn.place(x=180, y=60)

adminLabel = Label(root, text='Admin login:- ', font=('Arial', 11,"bold"), background="cyan")
adminLabel.place(x=20, y=100)

Adminbtn = Button(text="ADMIN", command=adminLogin, font=('Arial', 11,"bold"))
Adminbtn.place(x=180, y=100)

root.mainloop()
