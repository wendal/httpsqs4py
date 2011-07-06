import httpsqs
#Verion 1.0
#Author wendal(wendal1985@gmail.com)
#If you find a bug, pls mail me


#PLEASE start you httpsqs first!!!

print("init httpsqs client")
hq = httpsqs.Httpsqs('sunfarms.net')
#if you didn't use default 1218
#hq = httpsqs.Httpsqs('localhost',8020)

#PUT
print("Test PUT -------------------------------------")
data = 'This is a httpsqs client' #data can be a file
resp = hq.put('QueueABC',data)
if httpsqs.isOK(resp) :
    print("PUT OK")
else :
    print("PUT FAIL --> "+ resp)

#GET
print("Test GET -------------------------------------")
resp = hq.get('QueueABC')
if httpsqs.isOK(resp) :
    print("GET OK --> " + resp)
else :
    print("GET FAIL --> "+ resp)

#Status
print("Test Status ----------------------------------")
resp = hq.status('QueueABC')
print(resp) #Alway OK

#Status json
print("Test Status json -----------------------------")
resp = hq.status_json('QueueABC')
print(resp) #Alway OK

#Reset
print("Test Reset -----------------------------------")
resp = hq.reset('QueueABC')
if httpsqs.isOK(resp) :
    print("Reset OK")
else :
    print("Reset FAIL --> "+ resp)

#Set max len of a queue
print("Test maxlen ----------------------------------")
resp = hq.maxlen('QueueABC',100000)
if httpsqs.isOK(resp) :
    print("Set max len OK")
else :
    print("Set max len FAIL --> "+ resp)

#Set sync time
print("Test sync time --------------------------------")
resp = hq.synctime('QueueABC',5)
if httpsqs.isOK(resp) :
    print("Set sync time OK")
else :
    print("Set sync time FAIL --> "+ resp)


print("Test END -------------------------------------")
