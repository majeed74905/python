import matplotlib.pyplot as plt

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
sales = [500, 700, 800, 650, 900, 1200, 1100, 1000, 950, 1150, 1300, 1400]

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales - Line Chart")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.subplot(1,2,2)
plt.bar(months, sales, color='orange')
plt.title("Monthly Sales - Bar Chart")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()
