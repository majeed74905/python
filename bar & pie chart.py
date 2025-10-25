import matplotlib.pyplot as plt

products = ['A', 'B', 'C', 'D']
sales = [300, 450, 150, 200]

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.bar(products, sales, color='skyblue')
plt.title("Product Sales - Bar Chart")

plt.subplot(1,2,2)
plt.pie(sales, labels=products, autopct='%1.1f%%')
plt.title("Product Sales - Pie Chart")

plt.tight_layout()
plt.show()
