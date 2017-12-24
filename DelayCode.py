#Import  Expansion lib
import re

#Start nodes
AllNodes = { '10.1.1.1' : 0,
            '10.1.1.2' : 1,
            '10.1.1.3' : 2,
            '10.1.1.4' : 3,
            '10.1.1.5' : 4,
            '10.1.1.6' : 5,
            '10.1.1.7' : 6,
            '10.1.1.8' : 7,
            '10.1.1.9' : 8,
            '10.1.1.10' : 9,
            '10.1.1.11' : 10,
            '10.1.1.12' : 11, 
            '10.1.1.13' : 12, 
            '10.1.1.14' : 13, 
            '10.1.1.15' : 14, 
            '10.1.1.16' : 15, 
            '10.1.1.17' : 16, 
            '10.1.1.18' : 17, 
            '10.1.1.19' : 18, 
            '10.1.1.20' : 19, 
            '10.1.1.21' : 20, 
            '10.1.1.22' : 21, 
            '10.1.1.23' : 22, 
            '10.1.1.24' : 23, 
            '10.1.1.25' : 24,
            '10.1.1.26' : 25,
            '10.1.1.27' : 26,
            '10.1.1.28' : 27,
            '10.1.1.29' : 28,
            '10.1.1.30' : 29,
            '10.1.1.31' : 30,
            '10.1.1.32' : 31,
            '10.1.1.33' : 32,
            '10.1.1.34' : 33,
            '10.1.1.35' : 34,
            '10.1.1.36' : 35,
            '10.1.1.37' : 36,
            '10.1.1.38' : 37,
            '10.1.1.39' : 38,
            '10.1.1.40' : 39,
            '10.1.1.41' : 40,
            '10.1.1.42' : 41,
            '10.1.1.43' : 42,
            '10.1.1.44' : 43,
            '10.1.1.45' : 44,
            '10.1.1.46' : 45,
            '10.1.1.47' : 46,
            '10.1.1.48' : 47,
            '10.1.1.49' : 48,
            '10.1.1.50' : 49, }

#open trace file
with open("IP_Trace.tr","r") as sa:

#Create list 't' and 'r' from trace file 
    t = list()
    r = list()

    for line in sa:
        if line.start("t "):
            t.append(line[0:])
        if line.start("r "):
            r.append(line[0:])

#Creat lists of the transmitted and received packets
TransmtPacks = list()
Pckts_received = list()
Delay_Max = 0
Delay_Total = 0

PcktsTransmt_Total = 0


for a in t:
    if "Payload" in a:
        TransmittedPckts.append(a)

for b in r:
    if "Payload" in b:
        Pckts_received.append(b)
#Compare IP add, Seq num and ID
for trans in TransmtPacks:
    Match_IP = re.search(r'10.1.1.\d{1,2} > 10.1.1.\d{1,2}', trans)
    Match_Seqnum = re.search(r'SeqNum=\d{1,2}',trans)
    Match_id = re.search(r'id \d{1,}',trans)
    if Match_IP and Match_Seqnum and Match_id:
        Trans_Time = re.findall(r't(.*?)/',trans)
        IP = Match_IP.group(0).split('>')
        sourceIP = IP[0].strip()
        string = "/Nodlst/" + str(AllNodes[sourceIP])
        if string in trans: 
            destIP = IP[1].strip()
            seqNumber = Match_Seqnum.group(0).split('=')
            seqNumber = seqNumber[1]
            src_id = Match_id.group(0).split(' ')
            src_id = src_id[1]
            for recv in Pckts_received:
                string = "/Nodlst/" + str(AllNodes[destIP])
                if string in recv:
                    Match_IP = re.search(r'10.1.1.\d{1,2} > 10.1.1.\d{1,2}', recv)
                    Match_Seqnum = re.search(r'SeqNum=\d{1,2}',recv)
                    Match_id = re.search(r'id \d{1,}',recv)
                    if Match_IP and Match_Seqnum and Match_id:
                        Rec_Time = re.findall(r'r(.*?)/',recv)
                        IP = Match_IP.group(0).split('>')
                        rcv_sourceIP = IP[0].strip()
                        rcv_destIP = IP[1].strip()
                        rcv_seqnum = rcv_seqnum[1]
                        des_id = Match_id.group(0).split(' ')
                        des_id = des_id[1]
                        if sourceIP == rcv_sourceIP and destIP == rcv_destIP and seqNum == rcv_seqnum and src_id == des_id:
                            if float(Trans_Time[0]) < float(Rec_Time[0]):
                                delay = float(Rec_Time[0]) - float(Trans_Time[0])
                                Delay_Total = Delay_Total + delay
                                PcktsTrans_Total +=1
                                if Delay_Max < delay:
                                    Delay_Max = delay
                                Pckts_received.remove(recv)
                                break
            else: break    

#calclate average delay 
Delay_Avg = Delay_Total / PcktsTrans_Total


#print avg and max delay
print('Average delay {}'.format(Delay_Avg))
print('Maximum delay {}'.format(Delay_Max))

