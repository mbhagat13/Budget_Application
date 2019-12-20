import sys
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np


if (len(sys.argv) != 4):
    print("Enter input in correct format: python Budget.py filename.csv Year(2020) Month(09)")
    exit()
    
try:
    creditCardData = pd.read_csv (sys.argv[1], names=["Date","Transaction_Description","Debit","Credit","Balance"]) #open csv statement file if it exists
except:
    print("File not Found")
    exit()

purchaseNum=1 # used as output variable to check amount of purchases in a statement not including credit card payments0
entryExists = 0 #flag variable, if 1, allow user to categorize eithe type of purchase
categoryNames = ["Transportation", "Food", "Clothes_Accessories", "Entertainment", "Other"] #Categories for purchases
totalSpent =  [0 for i in range(len(categoryNames))] # to store total value of all categories
purchaseDescriptors=[set() for i in range(len(categoryNames))] #set to store specifc purchase descriptions (Uber, Pizza Pizza etc.)

for x in range(len(categoryNames)): # open exist data files and store purchaseDescriptors data
    f = open(str(categoryNames[x] + ".txt"),"r")
    for y in f:
        purchaseDescriptors[x].add(y[0:(len(y)-1)])
    f.close()

categorizedData = [pd.DataFrame(columns=["Date","Transaction_Description","Debit","Credit","Balance"]) for i in range(len(categoryNames))] ## create dataframes to store all descriptions seperately
print(creditCardData)

for x in range(len(creditCardData)):
    if(math.isnan(creditCardData.Credit[x])): #check if it is a Credit or Debit on the card
        print("\n\n\nPurchase " +str(purchaseNum) + ":")
        purchaseNum += 1
        print(creditCardData.iloc[x,:])
      
        for i in range(len(categoryNames)): #check if purchase descriptor is known
            for j in purchaseDescriptors[i]:
                if (j in creditCardData.Transaction_Description[x]):
                    categorizedData[i].loc[len(categorizedData[i]),:] = creditCardData.loc[x,:]##if known, sort data into appropriate category
                    entryExists = 1; #flag not to let user sort type of entry
                    i=(len(categoryNames));
                    break;

        if(entryExists==0):
            for y in range(len(categoryNames)):
                print(str(y) + " - " + categoryNames[y])            
            userChoice = input("Enter the type of purchase:\n");# Enter Purchase category
            userChoice = int(userChoice);
            categorizedData[userChoice].loc[len(categorizedData[userChoice]),:] = creditCardData.loc[x,:]
            userDescriptor = input("Enter the unique identifier for Records:\n") #Data to be stored in additional text file
            f = open(str(categoryNames[userChoice] + ".txt"),"a") #write data appropriate file
            f.write(str(userDescriptor +"\n"))
            purchaseDescriptors[userChoice].add(userDescriptor) ## add to existing set of purchase descriptors
            f.close()
        else:
            entryExists=0;           
    else: # If the balance is paid off, let user know when payment was made
        print("\n\n\nCredit Card Payment on "+ str(creditCardData.Date[x]))
        print(creditCardData.iloc[x,:]) 
        
for x in range(len(categorizedData)):#output all the data
    totalSpent[x] = totalSpent[x]+sum(categorizedData[x].Debit)  
    print("\n\n{:s}: ${:.2f}".format(categoryNames[x],totalSpent[x]))
    print(categorizedData[x])
print("\n\nTotal: ${:.2f}".format(sum(totalSpent)))

#Plotting Pie chart below

def func(pct, allvals):
   abc=pct
   price = (pct/100.*sum(allvals))
   return "{:.1f}%  ${:.2f} ".format(abc, price)
    
    
fig, ax = plt.subplots(figsize=(10, 5), subplot_kw=dict(aspect="equal"))
theme = plt.get_cmap('bwr')
ax.set_prop_cycle("color", [theme(1. * i / len(totalSpent))for i in range(len(totalSpent))])

wedges, texts, autotexts = ax.pie(totalSpent, wedgeprops=dict(width=0.7), autopct = '%1.1f%%', textprops=dict(color="w"))

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")
for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate("${:.2f}".format(totalSpent[i]), xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)

ax.legend(wedges, categoryNames,title="Categories",bbox_to_anchor=(0, 0.70,-0.3,0))
plt.setp(autotexts, size=7, color = "black",weight="bold")
ax.set_title(str("Expense for " + sys.argv[2] + "/" + sys.argv[3]),y=1.05)
plt.show()

    
  