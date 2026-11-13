c=str(input("Copy is complete or Incomplete:"))
if c=="complete":
   m=int(input("Enter the marks:"))
   if m>=50:
       print("eligible for mids")
   else:
       print("not eligible for mids")
else:
    print("Copy is incomplete not eligible for mids")