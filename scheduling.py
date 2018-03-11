# This program is a simulation of Operating System Process Scheduling. The user enteres n processes,
# the time of arrival of each process, the amount of time needed for each process to complete its task, 
# and the relative priority of the process and this program will output the order and duration at which the
# processes excecute. The output is in the form of a Gantt Chart. 
#
# The order and duration in which the processes run depend on the scheduling algorithm used, and this program
# implements four different computer scheduling algorithms: shortest job first, first come first serve, non-preemptive priority 
# and round robin. 


from copy import *

class Process:
	def __init__ (self, name, arrival, burst, priority):
		self.name = name
		self.arrival = arrival
		self.burst = burst
		self.priority = priority

	def display(self):
		print (self.name)
		print (self.arrival)
		print (self.burst)
		print (self.priority)

def getProcesses():
	num = input("How many processes are there? ")

	i = 0
	processes = []
	
	while i < num:
		name = "p" + str(i+1)
		arrival = eval('input("arrival time: ")')
		burst = eval('input("burst time: ")')
		priority = eval('input("priority: ")')
		processes.append(Process(name, arrival, burst, priority))
		i += 1

	processes = sorted(processes, key=lambda Process: Process.arrival)

	#for i in range(len(processes)):
	#	processes[i].display()

	return processes

def getMinArrival(arr):
	min = arr[0].arrival
	for i in range(len(arr)):
		if min > arr[i].arrival:
			min = arr[i].arrival
	return min

def getMinBurst(arr):
	min = arr[0].burst
	for i in range(len(arr)):
		if min > arr[i].burst:
			min = arr[i].burst
	return min

def getHighestPriority(arr):
	#Highest priority based on lowest relative priority

	min = arr[0].priority
	for i in range(len(arr)):
		if min > arr[i].priority:
			min = arr[i].priority
	return min

def fcfs(array):
	# first come first served
	arr = deepcopy(array)
	gantt = []
	deleted = False

	while len(arr) > 0:
		min = getMinArrival(arr)
		i = 0
		while i < len(arr):
			while len(gantt) < arr[i].arrival:
				gantt.append("00")
			if min == arr[i].arrival:
				#add to gant chart (burst) amount of times 
				while arr[i].burst > 0:
					gantt.append(arr[i].name)
					arr[i].burst -= 1
				del(arr[i])
				deleted = True
			if not deleted:
				i += 1
			deleted = False
	return (gantt)


def sjf(array):
	#shortest job first
	arr = deepcopy(array)
	gantt = []
	deleted = False

	while len(arr) > 0:
		min = getMinBurst(arr)
		i = 0
		while i < len(arr):
			while len(gantt) < arr[i].arrival:
				gantt.append("00")
			if min == arr[i].burst:
				#add to gant chart (burst) amount of times 
				while arr[i].burst > 0:
					gantt.append(arr[i].name)
					arr[i].burst -= 1
				del(arr[i])
				deleted = True
			if not deleted:
				i += 1
			deleted = False
	#print("SJF:")
	#display(gantt)
	return gantt

def npp(array):
	#non-preemptive priority
	
	arr = deepcopy(array)
	gantt = []
	deleted = False

	while len(arr) > 0:
		min = getHighestPriority(arr)
		i = 0
		while i < len(arr):
			while len(gantt) < arr[i].arrival:
				gantt.append("00")
			if min == arr[i].priority:
				#add to gantt chart (burst) amount of times 
				while arr[i].burst > 0:
					gantt.append(arr[i].name)
					arr[i].burst -= 1
				del(arr[i])
				deleted = True
			if not deleted:
				i += 1
			deleted = False
	#print("NPP:")
	#display(gantt)
	return gantt

def rr(array, q):
	# round robin
	arr = deepcopy(array)
	gantt = []
	deleted = False
	quantum = q

	while len(arr) > 0:
		i = 0
		while i < len(arr):
			deleted = False
			while len(gantt) < arr[i].arrival:
				gantt.append("00")

			#if arr[i].burst > 0 and quantum > 0:
			gantt.append(arr[i].name)
			arr[i].burst -= 1
			quantum -= 1
				
			if arr[i].burst == 0:
				del(arr[i])
				deleted = True
				
			if quantum == 0:
				quantum = q
				if not deleted:
					i += 1 

	#print("Round Robin:")
	#display(gantt)
	return gantt

def display(gantt):

	arr = []
	for i in range(len(gantt)):
		if len(arr) < 10:
			arr.append('0' + str(len(arr)))
		else :
			arr.append(str(len(arr)))

	print(arr)
	print(gantt)

def compress(gantt):

	arr = []
	start = 0
	i = 0

	while i < len(gantt):
		start = i # for last append i will be out of range
		j = i+1

		while j < len(gantt) and gantt[i] == gantt[j]:
			j += 1
		if j < len(gantt) and gantt[i] != gantt[j]:
			arr.append( gantt[i] + ":"+ str(i) + "-" + str(j))
		i = j

	#LAST PROCESS is never appended (since process is appended
	#to the gantt chart whenever a difference is found between 
	#gantt[i] and gantt[j]

	arr.append(gantt[start] + ":"+ str(start) + "-" + str(j))
	return arr

def main():
	
	processes = getProcesses()

	print("\nFCFS: ")
	#print(fcfs(processes))
	#print("\n")
	print(compress(fcfs(processes)))
	print("\nSJF: ")
	#print(sjf(processes))
	#print("\n")
	print(compress(sjf(processes)))
	print("\nNPP: ")
	#print(npp(processes))
	#print("\n")
	print(compress(npp(processes)))

	q = input("\nRound Robin: What is the quantum? ")
	
	#print(rr(processes, q))
	print(compress(rr(processes, q)))

main()