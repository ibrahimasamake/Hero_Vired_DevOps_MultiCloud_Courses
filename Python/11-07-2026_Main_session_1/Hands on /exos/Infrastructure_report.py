print("==========================================================================================")
print("CLOUD INFRASTRUCTURE REPORT")
print("==========================================================================================")

is_env_correct = False

cpu_usage = 0
memory_usage = 0
disk_usage  = 0 
while not is_env_correct:


    environment = input("Enter the environment (e.g., production, staging, development, testing): ")

    if(environment.lower() != "production" and environment.lower() != "staging" and environment.lower() != "development" and environment.lower() != "testing" ):

        print("Invalid environment. Please enter a valid environment (production, staging, development, testing).")

    else:

        print("Generating report for the", environment, "environment...")

    


    monitoring_cycles = int(input("Enter the number of monitoring cycles: "))

    while monitoring_cycles <= 0:
        print("Invalid input. Please enter a positive integer for the number of monitoring cycles.")
        monitoring_cycles = int(input("Enter the number of monitoring cycles: "))
        if(monitoring_cycles > 0):
            break


    print("Monitoring cycles set to:", monitoring_cycles)


    munimum_instances = int(input("Enter the munimum number of instances allowed: "))
    while munimum_instances <= 0:
        print("Invalid input. Please enter a positive integer for the munimum number of instances.")
        munimum_instances = int(input("Enter the munimum number of instances allowed: "))
        if(munimum_instances > 0):
            break

    print("Munimum instances set to:", munimum_instances)



    maximum_instances = int(input("Enter the maximum number of instances allowed: "))
    while maximum_instances < munimum_instances:
        print("Invalid input. Please enter a positive integer for the maximum number of instances.")
        maximum_instances = int(input("Enter the maximum number of instances allowed: "))
        if(maximum_instances > munimum_instances):
            break

    print("Maximum instances set to:", maximum_instances)

            
    

    current_instances = int(input("Enter the current number of instances: "))
    while current_instances < munimum_instances or current_instances > maximum_instances:
        print("Invalid input. Please enter a positive integer for the current number of instances.")
        current_instances = int(input("Enter the current number of instances: "))
        if(current_instances >= munimum_instances and current_instances <= maximum_instances):
            break

    print("Current instances set to:", current_instances)
    



    hourly_cost_per_instance = float(input("Enter the hourly cost per instance: "))
    while hourly_cost_per_instance < 0:
        print("Invalid input. Please enter a positive number for the hourly cost per instance.")
        hourly_cost_per_instance = float(input("Enter the hourly cost per instance: "))
        if(hourly_cost_per_instance >= 0):
            break

    print("Hourly cost per instance set to:", hourly_cost_per_instance)


    for i  in range(munimum_instances, maximum_instances ) :

        print("Monitoring cycle : " , i )
        cpu_usage = int(input("Entre CPU Usage "))
        memory_usage = int(input("Entre CPU Usage "))
        disk_usage =int( input("Entre Disk  Usage "))
        http_status= int(input("Entre Https status response  : ") )
        response_time_milliseconds = int(input("Entre response time in  milliseconds  : ") )

        if(cpu_usage < 0 and cpu_usage > 100 or memory_usage < 0 or memory_usage>100 or disk_usage   <0 or disk_usage >100 ):
    
            print("Invalid resource usage. Monitoring cycle skipped.")
            continue
                
        else:
            cost =  current_instances * hourly_cost_per_instance
            if(cpu_usage >80 or disk_usage > 80 or  memory_usage > 80 ) :
                print("Resource status: Critical")
    
            elif(cpu_usage >=60 or disk_usage >= 60 or  memory_usage >= 70   ) :
                print("Resource status: Warning")
            else:
                 print("Healthy All remaining valid readings Resource status: Healthy")

        

            print("Current CPU Usage:", cpu_usage, "%")
            print("Current Memory Usage:", memory_usage, "%")
            print("Current Disk Usage:", disk_usage, "%")
            print("Current HTTP Status Response:", http_status)
            print("Current Response Time:", response_time_milliseconds, "milliseconds")
            print("Current Cost per Hour:", cost, "USD")    
             
            if(http_status ==200 or http_status >= 299 and  response_time_milliseconds  <= 500) :
                print("Application status: Healthy.")
            elif(http_status ==200 or http_status >= 299  and response_time_milliseconds > 500 ) :
                print("Application status: Slow.")
            else:
                print("Application status: Failed.")



            print("Simulated Auto-Scaling Decision")
            if (environment.lower() == "production" and cpu_usage > 70 or memory_usage > 70  ) :
                if(current_instances <  maximum_instances) :
                    print("Increase by 1")
                elif(current_instances ==  munimum_instances) :
                    print("Do not change count")    
                elif(current_instances >  munimum_instances) :
                    print("Decrease by 1")
                    
            elif (environment.lower() == "staging" or environment.lower()== "developement" and cpu_usage > 75 or memory_usage > 75  ) :
                print("Increase by 1")
          




            




             








    

    
    
           






    is_env_correct = True
    break;

