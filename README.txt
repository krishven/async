README:

INSTRUCTIONS:
--------------
	DISTALGO INSTALLATION
	-----------------------
	1. Install python 3.5
	2. Download DistAlgo-1.0.0b17 based on your OS and install it
	3. Set distalgo bin PATH 
	4. To confirm if its working run a sample example as "python -m da <example_pgm.da>"

	HOW TO RUN PROGRAM:
	---------------------
	Run script.sh under src directory. In script.sh, the user can pass config file as argument. Different test cases can be tested using different config files. The logs will be stored as Logs/<config_name>.log


MAIN FILES:
-----------

1. Master Process - <rootdir/src/main.da>   
	This is the main process which starts all other process based on the parameters read from config file.

2. Client Process - <rootdir>/src/Client.da
	Constructs policy evaluation request based on parameters from config file and then sends and wait for the response.

3. SubjectCoordinator Process - <rootdir>/src/SubjectCoordinator.da
	This file contains code for Subject Coordinator Process which communicates with Client, Worker and Resource Coordinator to evaluate a policy request and also handles the subject attribute conflicts

4. ResourceCoordinator Process - <rootdir>/src/ResourceCoordinator.da
	This file contains code for Resource Coordinator Process which communicates with the Worker assigned for it and Subject Coordinator to evaluate a policy request and also handles the resource attribute conflicts

5. Worker Process - <rootdir>/src/Worker.da
	The Worker process handles requests from Resource Coordinator Process and communicates with DB inorder to evaluate a policy request based on the rules specified. The policy evaluation is done here and it sends the results back to respective Subject Coordinator 	
	
6. Database Emulator Process - <rootdir>/src/DbEmulator.da
	The database emulator maintains an in memory data structure to store the information received from Subject Coordinator and also send this data to Worker if any requested.

7. common functions and data structure - <rootdir>/src/common.da
	This file contains common function and common data structure which will be used by all processes	


BUGS AND LIMITATIONS:
----------------------
1. We assumed that there won't be subject and resource update together for a rule.
2. The updates are not commited in the order in which it is updated in tentative cache

ASSUMPTIONS:
------------	
1. The number of coordinators read from config file is equally divided for Subject Coordinator and Resource Coordinator. Incase of odd number of coordinators, the resource coordinator will be one greater than subject coordinator

2. If there are multiple clients, the requests will be equally distributed in round robin fashin. For example, it there are five requests and 3 clients, then 1st client will handle 1st and 4th request, while second client will handle 2nd and 5th request and third client will handle 3rd request.

3. For numnber of Workers per corrdinator parameter, we randomly assigned equal number of unique workers to each resource coordinator. 
