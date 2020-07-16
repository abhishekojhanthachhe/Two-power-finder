from datetime import datetime
import multiprocessing

print("initializing variables...")

s = 29700000000 #make sure s%grouping_const==0 and s%threads==0
u = 39600000000 #make sure u%grouping_const==0 and u%threads==0
pres = 10**100 #precision, ie only calculates last 100 digits of 2^n
ps = [] #partial success power indices
ss = [] #success power indices

grouping_const = 100000
threads = 3

if s<10**9:
    init2 = 2**s
else:
    init2 = 1
    temppp1 = threads*grouping_const
    for temppp2 in range(int(s/temppp1)):
        init2 *= 2**temppp1
        init2 %= pres

fname = str(s) + " to " + str(u)

def general_thread_code (start, limit, step):
    f = open(fname+".txt","a")
    g = open(fname+".csv","a")

    f.write(str(s) + " to " +str(u) + " with grouping constant " + str(grouping_const) + " and " + str(threads) + " threads.\n")

    case = init2*(2**(start-s)) #particular case of power of2
    case = case%pres
    upper = start

    b = step*grouping_const

    for j in range(start, limit, b):

        lower = upper
        upper = lower + b

        for i in range(lower, upper, step):
            
            icase = case #initial case
            fail = False

            while (case>0):
                n,case = case%10,case//10
                if n==2 or n==4 or n==8:
                    fail = True
                    break
            
            if (not fail): #partial success
                print("Thread#"+str(start-s)+": PARTIAL SOL 2^"+str(i))
                f.write(str(datetime.now()) + ":\tPARTIAL! 2^"+str(i)+" PARTIAL " + str(icase) + "\n")
                ps.append(i)
            
            case = (icase*(2**step))%pres

        print("Thread#"+str(start-s)+", 2^"+str(i)+" done!")
        f.write(str(datetime.now()) + ":\tThread#"+str(start-s)+", 2^"+str(i)+" done!\n")
        g.write(str(i)+"\n")
    
    f.write("\nThread#" + str(start-s) + ", ALL DONE!\n" + "*"*70 + "\n"*2)

    f.close()
    g.close()

                #for successful find print:
                #print("2^"+str(i)+" = "+str(icase))
                #f.write("\n"*2 + "-"*70 + "\n" + str(datetime.now()) + ":\t2^"+str(i)+" = "+str(icase) + "\n" + "-"*70 + "\n"*2)

if __name__ == "__main__":
    print("------------- Multiprocessing ----------------")
    #thread_count = int(input("How many processes would you like to use?: "))
    thread_count = threads
    start_time = datetime.now()
    process_list = []

    for i in range(thread_count):
        process_list.append(multiprocessing.Process(target=general_thread_code, args=(s + i, u, thread_count)))
        process_list[i].start()

    for process in process_list:
        process.join()
    
    print("Partial solutions:" + str(", ".join(ps)))
    print("Solutions:" + str(", ".join(ss)))
    print("Time taken:", datetime.now() - start_time)

    f = open(fname+".txt","a")
    f.write("\n\nPartial solutions:" + str(", ".join(ps))+"\n"+"Solutions:" + str(", ".join(ss))+"\n\n"+"-*"*35+"\n\nTime taken:" + str(datetime.now() - start_time) + "\n\n\n")
    f.close()
