
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("employees.csv")

# 1. BAR CHART - Average salary per department
avg_salary = df.groupby("department")["salary"].mean()

plt.bar(avg_salary.index,avg_salary.values)

plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.bar_label(plt.gca().containers[0],fmt="%.0f")
plt.savefig("bar_chart.png")
plt.show()

#2.Histogram

plt.hist(df["salary"],bins=5, edgecolor="black")

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.savefig("histogram.png")
plt.show()

# 3.Scatter plot

colors = {
    "IT": "blue",
    "HR": "red",
    "Sales": "green",
    "Finance": "orange"
}

for dept, color in colors.items():
    data = df[df["department"] == dept]

    plt.scatter(data["id"], data["salary"],
                color=color, label=dept)

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.savefig("scatter_plot.png")
plt.show()

# 4. Line chart 

months=["Jan","Feb","Mar","Apr","May","Jun"]
sales=[12,15,14,18,22,25]

plt.plot(months,sales,marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.savefig("line_chart.png")
plt.show()

