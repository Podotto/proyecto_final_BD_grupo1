# Total de eventos
def total_events():
    total = 0

    with open("data/logs.txt") as file_object:
        for record in file_object:
            total += 1

    print(f"Total de eventos: {total}")
    
# Successful Logins
def login_success():
    total = 0

    with open("data/logs.txt") as file_object:
        for record in file_object:
            line = record.strip().split(",")

            event = line[2].strip()
            success = line[3].strip()

            if event == "LOGIN" and success == "SUCCESS":
                total += 1

    print(f"Logins exitosos: {total}")
    
# Failed Logins
def login_fail():
    total = 0

    with open("data/logs.txt") as file_object:
        for record in file_object:
            line = record.strip().split(",")

            event = line[2].strip()
            success = line[3].strip()

            if event == "LOGIN" and success == "FAIL":
                total += 1

    print(f"Logins fallidos: {total}")

# Unique users
def unique_users():
    total = 0
    user_list = []

    with open("data/logs.txt") as file_object:
        for record in file_object:
            line = record.strip().split(",")
            user = line[1].strip()
            user_list.append(user)

    for i in set(user_list):
        total += 1

    print(f"Usuarios únicos: {total}")

# Usuarios sospechosos
def suspicious_users():
    fail_count = {}

    with open("data/logs.txt") as file_object:
        for record in file_object:
            line = record.strip().split(",")
            user = line[1].strip()
            event = line[2].strip()
            status = line[3].strip()

            if event == "LOGIN" and status == "FAIL":
                if user in fail_count:
                    fail_count[user] += 1
                else:
                    fail_count[user] = 1

    print("Usuarios sospechosos:")
    found = False

    for user in fail_count:
        if fail_count[user] > 3:
            print(user)
            found = True

    if found == False:
        print("No hay usuarios sospechosos.")


