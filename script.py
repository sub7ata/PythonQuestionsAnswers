##### Q1
import csv
from datetime import datetime
dict = {}
reader = csv.DictReader(open("demo1.csv"))
for raw in reader:
    dict[raw['Shipment id']] = raw
print("Q1. Create a Dictionary of lists to store the information of shipments given in the table")
print(dict)


##### Q2
dict1 = {}
reader = csv.DictReader(open("demo2.csv"))
for raw in reader:
    dict1[raw['Client_id']] = raw
print("\nQ2. Create a Dictionary of to store the information of clients given in the table.")
print(dict1)


##### Q3
result = {}
for key, value in dict.items():
    new_value = {k: dict1[v]['Client Name'] if k in ('Sender', 'Receiver') else v for k,v in value.items()}
    result[key] = new_value
print("\nQ3. Write a code to replace client’s id with their respective name in shipment dictionary using a loop and dictionary comprehension")
print(result)


##### Q4
phillips = list(filter(lambda value: value['Sender'] == 'Phillip', result.values()))
print("\nQ4. Print all shipment details that are sent by Phillip")
print(phillips)


##### Q5
ramya = list(filter(lambda value: value['Receiver'] == 'Ramya', result.values()))
print("\nQ5. Print all shipment details that are received by Ramya")
print(ramya)


##### Q6
status = list(filter(lambda value: value['Deliver status'] == 'In-Transit', result.values()))
print("\nQ6. Print all shipments which are in 'In-Transit' status")
print(status)


##### Q7
print("\nQ7. Print all shipments which are delivered within 7 days of courier Start date")
for v in result.values():
    if v["Delivery date"] == "Null":
        continue
    start = datetime.strptime(v["Start date"], "%d-%m-%Y")
    delivery = datetime.strptime(v["Delivery date"], "%d-%m-%Y")

    if (delivery - start).days <= 7:
        print(v)

print("\nQ8. Print all shipments which are delivered after 15 days of courier start date or not yet been delivered.")
for v in result.values():
    if v["Delivery date"] == "Null":
        continue
    start = datetime.strptime(v["Start date"], "%d-%m-%Y")
    delivery = datetime.strptime(v["Delivery date"], "%d-%m-%Y")

    if (delivery - start).days >= 15:
        print(v)