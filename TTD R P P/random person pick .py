import random
people_data = [
    {"name": "Ravindra Kumar", "age": random.randint(18, 50), "city": "Bangalore", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Arun Sharma", "age": random.randint(18, 50), "city": "Mumbai", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Priya Reddy", "age": random.randint(18, 50), "city": "Hyderabad", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Karthik Nair", "age": random.randint(18, 50), "city": "Chennai", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Aishwarya Iyer", "age": random.randint(18, 50), "city": "Coimbatore", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Sandeep Patel", "age": random.randint(18, 50), "city": "Ahmedabad", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Vikram Singh", "age": random.randint(18, 50), "city": "Delhi", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Sneha Menon", "age": random.randint(18, 50), "city": "Kochi", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Ravi Desai", "age": random.randint(18, 50), "city": "Pune", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Anjali Gupta", "age": random.randint(18, 50), "city": "Lucknow", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Neelam Joshi", "age": random.randint(18, 50), "city": "Jaipur", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Suresh Babu", "age": random.randint(18, 50), "city": "Madurai", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Vani Srinivasan", "age": random.randint(18, 50), "city": "Chennai", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Manoj Yadav", "age": random.randint(18, 50), "city": "Noida", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Ritika Kapoor", "age": random.randint(18, 50), "city": "Mumbai", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Tejaswini Rao", "age": random.randint(18, 50), "city": "Hyderabad", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Rajesh Kumar", "age": random.randint(18, 50), "city": "Bhopal", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Nandini Sharma", "age": random.randint(18, 50), "city": "Kanpur", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Sanjay Kumar", "age": random.randint(18, 50), "city": "Chandigarh", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Deepika Agarwal", "age": random.randint(18, 50), "city": "Patna", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Rohit Verma", "age": random.randint(18, 50), "city": "Jaipur", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Madhavi Sethi", "age": random.randint(18, 50), "city": "Indore", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Vikas Choudhary", "age": random.randint(18, 50), "city": "Jodhpur", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Kavita Iyer", "age": random.randint(18, 50), "city": "Chennai", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Mohan Rao", "age": random.randint(18, 50), "city": "Bangalore", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Pooja Rathi", "age": random.randint(18, 50), "city": "Delhi", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Suraj Patel", "age": random.randint(18, 50), "city": "Surat", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Kiran Kaur", "age": random.randint(18, 50), "city": "Amritsar", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Neha Soni", "age": random.randint(18, 50), "city": "Vadodara", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Krishna Reddy", "age": random.randint(18, 50), "city": "Vijayawada", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Chitra Menon", "age": random.randint(18, 50), "city": "Bangalore", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Sanjay Deshmukh", "age": random.randint(18, 50), "city": "Nagpur", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Rupesh Yadav", "age": random.randint(18, 50), "city": "Delhi", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Tanya Gupta", "age": random.randint(18, 50), "city": "Agra", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Ramesh Jha", "age": random.randint(18, 50), "city": "Patna", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Lalitha Rao", "age": random.randint(18, 50), "city": "Kochi", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Anil Sharma", "age": random.randint(18, 50), "city": "Shimla", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Sonali Roy", "age": random.randint(18, 50), "city": "Kolkata", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Jaya Kumari", "age": random.randint(18, 50), "city": "Jaipur", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Ranjan Chatterjee", "age": random.randint(18, 50), "city": "Kolkata", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Vishal Sharma", "age": random.randint(18, 50), "city": "Ludhiana", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Monika Patil", "age": random.randint(18, 50), "city": "Bangalore", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Suman Soni", "age": random.randint(18, 50), "city": "Jaipur", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Shankar Yadav", "age": random.randint(18, 50), "city": "Gurgaon", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Vijay Kumar", "age": random.randint(18, 50), "city": "Delhi", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Amit Thakur", "age": random.randint(18, 50), "city": "Bhopal", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Krishna Mohan", "age": random.randint(18, 50), "city": "Varanasi", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Nikita Verma", "age": random.randint(18, 50), "city": "Lucknow", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Arvind Joshi", "age": random.randint(18, 50), "city": "Guwahati", "id": f"ID{random.randint(1000, 9999)}"},
    {"name": "Simran Gill", "age": random.randint(18, 50), "city": "Amritsar", "id": f"ID{random.randint(1000, 9999)}"}
]

# Step 2: Randomly select 10 people
selected_people = random.sample(people_data, 10)

# Step 3: Display the selected people
print("\nThe randomly selected 10 people are:")
for person in selected_people:
    print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}, ID: {person['id']}")
