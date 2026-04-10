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

    with open("logs.txt") as file_object:
        for record in file_object:
            line = record.strip().split(",")

            event = line[2].strip()
            success = line[3].strip()

            if event == "LOGIN" and success == "SUCCESS":
                total += 1

    print(f"Logins exitosos: {total}")

