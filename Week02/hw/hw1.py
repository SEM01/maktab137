import csv
import json
try:
    def logreader(filename):
        error = 0
        info = 0
        warning = 0
        with open(filename, 'r') as file:
            line_number = 0
            
            for i in file:
                line_number +=1
                if (i[0] == '[') and (i[25] == ']') and (i[20] == ' '):        #Create correct pattern line log File
                    with open('all_logs.txt', 'a') as log_file:
                        log_file.write(f'{line_number} {i}')
                else:                                                          #Create incorrect pattern line log file
                    with open('errors.log', 'a') as error_file:
                        error_file.write(f'{line_number}: {i}')
                
                
                if i.find("error")>0:                                          #create error level log file
                    rows = [line_number,'Timestamp: ' + i[1:25],'Message: '+ i[35:]]
                    
                    with open('critical_errors.csv', 'a') as critical_errors:
                        writer = csv.writer(critical_errors, delimiter=' ')
                        writer.writerows([rows])
                
                if i.find('error')>0:
                    error = error +1
                if i.find('info')>0:
                    info +=1
                if i.find('warning')>0:
                    warning+=1
                data = {
                    "INFO" : info,
                    "WARNING" : warning,
                    "ERROR" : error
                }
                json_str = json.dumps(data, indent=0)
                with open('summary.json' , 'w') as summary_file:
                    summary_file.write(json_str)
        
except FileNotFoundError:
    print('Server.log not found')


            

                
    

