import random
            # data for 50 people ages under 60
people_data = [
    {"name": "Ravindra Kumar", "age": 30, "city": "Bangalore", "AadharCard": "3052 7875 6145"},
    {"name": "Arun Sharma", "age": 28, "city": "Mumbai", "AadharCard": "4782 1925 3145"},
    {"name": "Priya Reddy", "age": 35, "city": "Hyderabad", "AadharCard": "5621 8374 1992"},
    {"name": "Karthik Nair", "age": 40, "city": "Chennai", "AadharCard": "2831 6574 9203"},
    {"name": "Aishwarya Iyer", "age": 25, "city": "Coimbatore", "AadharCard": "1673 4592 3745"},
    {"name": "Sandeep Patel", "age": 50, "city": "Ahmedabad", "AadharCard": "8492 5623 4711"},
    {"name": "Vikram Singh", "age": 45, "city": "Delhi", "AadharCard": "2945 7635 9812"},
    {"name": "Sneha Menon", "age": 38, "city": "Kochi", "AadharCard": "5734 6845 1928"},
    {"name": "Ravi Desai", "age": 32, "city": "Pune", "AadharCard": "6472 1039 2764"},
    {"name": "Anjali Gupta", "age": 29, "city": "Lucknow", "AadharCard": "8153 9382 5761"},
    {"name": "Neelam Joshi", "age": 34, "city": "Jaipur", "AadharCard": "4652 7435 8923"},
    {"name": "Suresh Babu", "age": 50, "city": "Madurai", "AadharCard": "1309 5894 2831"},
    {"name": "Vani Srinivasan", "age": 42, "city": "Chennai", "AadharCard": "6783 9274 3106"},
    {"name": "Manoj Yadav", "age": 39, "city": "Noida", "AadharCard": "2865 1942 8517"},
    {"name": "Ritika Kapoor", "age": 27, "city": "Mumbai", "AadharCard": "5164 8237 6249"},
    {"name": "Tejaswini Rao", "age": 33, "city": "Hyderabad", "AadharCard": "8234 7614 9258"},
    {"name": "Rajesh Kumar", "age": 36, "city": "Bhopal", "AadharCard": "4056 7623 9810"},
    {"name": "Nandini Sharma", "age": 50, "city": "Kanpur", "AadharCard": "3248 5976 2825"},
    {"name": "Sanjay Kumar", "age": 43, "city": "Chandigarh", "AadharCard": "2076 4831 8956"},
    {"name": "Deepika Agarwal", "age": 41, "city": "Patna", "AadharCard": "5473 6821 5392"},
    {"name": "Rohit Verma", "age": 30, "city": "Jaipur", "AadharCard": "3928 7465 2840"},
    {"name": "Madhavi Sethi", "age": 46, "city": "Indore", "AadharCard": "8357 2831 4793"},
    {"name": "Vikas Choudhary", "age": 48, "city": "Jodhpur", "AadharCard": "9237 6574 6198"},
    {"name": "Kavita Iyer", "age": 39, "city": "Chennai", "AadharCard": "5193 7462 8430"},
    {"name": "Mohan Rao", "age": 33, "city": "Bangalore", "AadharCard": "8623 4917 5629"},
    {"name": "Pooja Rathi", "age": 27, "city": "Delhi", "AadharCard": "4392 6581 2896"},
    {"name": "Suraj Patel", "age": 50, "city": "Surat", "AadharCard": "2841 9510 1834"},
    {"name": "Kiran Kaur", "age": 44, "city": "Amritsar", "AadharCard": "9528 7634 1509"},
    {"name": "Neha Soni", "age": 31, "city": "Vadodara", "AadharCard": "7461 3829 7642"},
    {"name": "Krishna Reddy", "age": 29, "city": "Vijayawada", "AadharCard": "9371 6394 7452"},
    {"name": "Chitra Menon", "age": 38, "city": "Bangalore", "AadharCard": "6457 8932 7480"},
    {"name": "Sanjay Deshmukh", "age": 45, "city": "Nagpur", "AadharCard": "5289 1762 7491"},
    {"name": "Rupesh Yadav", "age": 42, "city": "Delhi", "AadharCard": "1027 5934 8723"},
    {"name": "Tanya Gupta", "age": 30, "city": "Agra", "AadharCard": "3549 8276 1129"},
    {"name": "Ramesh Jha", "age": 41, "city": "Patna", "AadharCard": "1857 2398 4356"},
    {"name": "Lalitha Rao", "age": 48, "city": "Kochi", "AadharCard": "7365 9821 4187"},
    {"name": "Anil Sharma", "age": 52, "city": "Shimla", "AadharCard": "9712 6259 4281"},
    {"name": "Sonali Roy", "age": 33, "city": "Kolkata", "AadharCard": "1835 9567 4392"},
    {"name": "Jaya Kumari", "age": 36, "city": "Jaipur", "AadharCard": "3917 5284 3670"},
    {"name": "Ranjan Chatterjee", "age": 40, "city": "Kolkata", "AadharCard": "4973 8509 6312"},
    {"name": "Vishal Sharma", "age": 50, "city": "Ludhiana", "AadharCard": "7584 3912 6417"},
    {"name": "Monika Patil", "age": 31, "city": "Bangalore", "AadharCard": "6284 2759 8245"},
    {"name": "Suman Soni", "age": 46, "city": "Jaipur", "AadharCard": "3847 5398 7451"},
    {"name": "Shankar Yadav", "age": 49, "city": "Gurgaon", "AadharCard": "5027 8437 1934"},
    {"name": "Vijay Kumar", "age": 45, "city": "Delhi", "AadharCard": "2938 7420 1537"},
    {"name": "Amit Thakur", "age": 38, "city": "Bhopal", "AadharCard": "4176 5392 8061"},
    {"name": "Krishna Mohan", "age": 37, "city": "Varanasi", "AadharCard": "8921 3745 6812"},
    {"name": "Nikita Verma", "age": 32, "city": "Lucknow", "AadharCard": "1925 3784 4963"},
    {"name": "Arvind Joshi", "age": 42, "city": "Guwahati", "AadharCard": "6347 2984 1650"},
    {"name": "Simran Gill", "age": 40, "city": "Amritsar", "AadharCard": "2746 5890 7413"}
]
            #  here we are randomly selctong 10 people out of 50.
selected_people = random.sample(people_data, 10)

            # final display the R selected 10 people
print("\nThe randomly selected 10 piligrims are:")
for person in selected_people:
    print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}, AadharCard: {person['AadharCard']}")
