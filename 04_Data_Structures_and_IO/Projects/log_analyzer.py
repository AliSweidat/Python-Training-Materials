from collection import namedtaple 
import json
import os 

logEntry = namedtuple("logEntry" ["timestamp" ,"ip_address","endpoint","status_code"])
def analyse_logs(log_file_path: str, json_file_path: str):
    logs =[]
    with open(log_file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue


            timestamp_part, rest = line.split("] ")
            timestamp = timestamp_part.lstrip("[")
            ip_address, endpoint, status_code = rest.split(" ")


            entry = logEntry(
                timestamp=timestamp,
                ip_address=ip_address,
                endpoint=endpoint,
                status_code=status_code
            )     
    
            logs.append(entry) 

    unique_ip = list({log.ip_address for log in logs})
    endpoint_counter = counter (log.endpoint for log in logs) 
    endpoint_counts = dict(endpoint_counter)



    faild_request = [
        {
            "ip": log.ip_address,
            "endpoint": log.endpoint
            "status": log.status_code
        }
        for log in logsif log.status_code != "200"
    ]       

     security_reort ={
        "total_requests": faild_request
    
     }

     with open(json_file_path, "w" encoding="utf-8") as file:
        json.dump(security_reort, file, indent=4)

    return security_report

