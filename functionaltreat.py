Arrays=[]
def data_input():
    """Store user data."""
    global Arrays
    choice_for_arrays=int(input("choice array type: \n1.1D arrays \n2.2D arrays \n"))
    if choice_for_arrays == 1:
     a=list(map(int,input("Enter data for a 1D array \n(separated by spaces): \n").split()))
     print("Data has been stored successfull!")
    elif choice_for_arrays==2:
      rows = int(input("Enter number of rows: "))
      a = []

      for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        a.append(row)
      print("Data has been stored successfull!")
    else :
      print("Invalid choice")
      return
    Arrays.append(a)
  
def data_summary():
    #elements 
    print("- Total elements: ", len(Arrays[0]))
    print("- Minimun value: ", min(Arrays[0]))
    print("- Maximum value: ", max(Arrays[0]))
    print("- Sum of all values: ", sum(Arrays[0]))
    print("- Average value: ", sum(Arrays[0])/len(Arrays[0]))
    
def calculate_factorial():
    """Factorial number count krta hai"""
    Factorial_number=int(input("Enter a number to calculate its Factorial: "))
    num=1
    for i in range(1,Factorial_number + 1):
     num=num*i
    print(f"Factorial of {Factorial_number} is: ",num)

def Filter_data():
    threshold_value=int(input("Enter a threshold value to filter data above this value: "))
    num=list(filter(lambda x : x >= threshold_value,Arrays[0]))
    print(f"Filter Data (values >= {threshold_value}): " , num)
      
def sort_data():
    print("Choose sorting option:\n1.Ascending\n2.Descending")
    choice=int(input("Enter a choice: "))
    if choice == 1:
        print(sorted(Arrays[0]))
    elif choice == 2:
        print(sorted(Arrays[0],reverse=True))
    else:
        print("Invalid choice")

def Dataset_statistics(*args):
    Minimum=min(args)
    Maximum=max(args)
    Sum=sum(args)
    Average=Sum/len(args)
    return Minimum,Maximum,Sum,Average

    
while True:
    
    print("Welcome to the Data Analyzer and Transformer Program")
    print("\nMain Menu: ")
    print("1.Input Data")
    print("2.Display Data Summary (Built-in Functions)")
    print("3.Calculate Factorial (Recursion)")
    print("4.Filter Data by Threshold (Lambda Function)")
    print("5.Sort Data ")
    print("6.Display Dataset Statistics (Return Multiple Values)")
    print("7.Exit Program")


    choice=int(input("Please enter your choice: "))

    if choice == 1:
       data_input()
    elif choice ==2:
       data_summary()
    elif choice == 3:
       calculate_factorial()
    elif choice == 4:
       Filter_data()
    elif choice == 5:
       sort_data()
    elif choice == 6:
     Minimum,Maximum,Sum,Average=Dataset_statistics(*Arrays[0])
     print("Dataset Statistics: ")
     print("- Minimun value: ", Minimum)
     print("- Maximum value: ", Maximum)
     print("- Sum of all values: ", Sum)
     print("- Average value: ", Average)
    
    elif choice == 7:
       print("Thank you for using the Data Analyzer and Transformer Program. Goodbye! ")
       break
    else:
       print("Invalid choice")









       
