amt = float(input("enter an amount of nz dollars "))
note100=amt //100
amt=amt%100
note50=amt //50
amt=amt%50
note20=amt //20
amt=amt%20
note10=amt //10
amt=amt%10
note5=amt //5
coin2=amt //2
amt=amt%2
coin1=amt //1
amt=amt%1
coin50c=amt //0.50
amt=amt%0.50
coin20c=amt //0.20
amt=amt%0.20
coin10c=amt //0.10
amt=amt%0.10
print("notes of 100:",note100)
print("notes of 50:",note50)
print("notes of 20:",note20)
print("notes of 10:",note10)
print("notes of 5:",note5)
print("coins of 2:",coin2)
print("coins of 1:",coin1)
print("coins of 50c:",coin50c)
print("coins of 20c:",coin20c)
print("coins of 10c:",coin10c)