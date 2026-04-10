def create_report(): 
    total_event = 0 
    login_success = 0 
    login_fail = 0 
    user_list = []
    fail_count = {}
    user_count = {}
    
    with open("data/logs.txt") as file_object: 
        for record in file_object: 
            line = record.strip().split(",") 
            
            user = line[1].strip()
            event = line[2].strip()
            status = line[3].strip()
            
            total_event += 1 
            user_list.append(user)
            
            if user in user_count: 
                user_count[user] += 1
            else: 
                user_count[user] = 1 
        