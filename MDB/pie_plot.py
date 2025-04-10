 # pip install pandas
import pandas as pd
df = pd.read_csv("customer_data.csv")
total_customers = len(df)
invalid_emails = len(df[df["email"] == "invalid_email"])
valid_emails = total_customers - invalid_emails

print(df.head())

print(f"total customers: {total_customers}")
print(f"invalid emails: {valid_emails}")
print(f"invalid customers: {invalid_emails}")

data = [invalid_emails, valid_emails]

pie_df = pd.DataFrame({"email":data}, index=["invalid, valid"])
pie_plot = pie_df.pd.Plot(y="email", figsize=(5,5))

pie_plot.figure.savefig("pie_plot.png")