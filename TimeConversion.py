def HrsMntConvert (hrs, mnt):
    if mnt > 59:
        mnt = mnt - 60
        hrs += 1
    if hrs > 23:
        print("Next Day")
        hrs = hrs - 24
    if hrs < 0:
        print("Previous Date")
        hrs = 24 + hrs
    print(hrs, ":", mnt)


print("Enter the Time in 24hrs format\nHours: ", end="")
hrs = int(input())
print("Minutes: ", end="")
mnt = int(input())
print("\nSelect your choice: ")
print("1. UTC\n2. UTC -4\n3. UTC +8\n4. GMT\n5. GMT +8")
ch = int(input(""))
print("\nIST time")
if ch == 1:
    hrs = hrs+5
    mnt = mnt+30
    HrsMntConvert(hrs, mnt)

elif ch == 2:
    hrs = hrs+9
    mnt = mnt+30
    HrsMntConvert(hrs, mnt)

elif ch == 3:
    hrs = hrs-3
    mnt = mnt+30
    HrsMntConvert(hrs, mnt)

elif ch == 4:
    hrs = hrs+5
    mnt = mnt+30
    HrsMntConvert(hrs, mnt)

elif ch == 5:
    hrs = hrs-3
    mnt = mnt+30
    HrsMntConvert(hrs, mnt)

