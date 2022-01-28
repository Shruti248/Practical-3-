# ID : 20ce153 
#Name : Shruti Unadkat

K = int(input())

Room_no = map(int, input().split())
Room_no = sorted(Room_no)

for i in range(len(Room_no)):
    if(i != len(Room_no)-1):
        if(Room_no[i]!=Room_no[i-1] and Room_no[i]!=Room_no[i+1]):
            print(Room_no[i])
            break;
    else:
        print(Room_no[i])
