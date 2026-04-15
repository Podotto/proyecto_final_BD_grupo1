def process_logs():
  with open("data/logs.txt") as file_object:
        
    for record in file_object:
      line = record.split(",")
      
      date = line[0]
      user = line[1]
      event = line[2]
      status = line[3]
      
      print(f"Date: {date}\nUser: {user}\nEvent: {event}\nStatus: {status}")
      
if __name__ == "__main__":
    process_logs()