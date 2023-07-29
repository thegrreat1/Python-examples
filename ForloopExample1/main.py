employees = ["Fay H. Wolf", "William C. Beltran", "Christie T. Johnson"]
employees_phone = ["786-433-5126", "978-302-2335", "435-693-2801"]
employees_address = ["4444 Burnside Avenue", "4408 Jarvis Street", "4747 Red Maple Drive"]

for name in employees:
    print("Name: {}\n"
          "Phone: {}\n"
          "Address: {}\n"
    .format(
        name,
        employees_phone[employees.index(name)],
        employees_address[employees.index(name)]))
