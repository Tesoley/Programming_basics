# investment_cost = float(input("How much did you invest? : "))
# total_revenue = float(input("What is your revenue? : "))
# roi = 100*(total_revenue-investment_cost)/investment_cost
# print(f"{roi}%")

receipt = float(input("Enter the cost of the order: "))
tip_percentage = float(input("How much do you want to tip (enter the value in percentage)?: "))/100

while tip_percentage<1:
    tip_percentage = float(input("How much do you want to tip (enter the value in percentage)?: ")) / 100
    break
final_price = receipt*(1+tip_percentage)
people = int(input("How many people in the company?: "))
individually = final_price/people

print(f"Your tip percentage: {tip_percentage*100}% \nYour receipt: {final_price} UAH\n Each person need to drop: {individually} UAH")



