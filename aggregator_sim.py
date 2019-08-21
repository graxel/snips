import random


def get_group_info():
    
    num_results = []
    
    num_groups = random.randint(1,6)
    
    #print("Number of groups:", num_groups, "\n") 
    
    for n in range(num_groups):
        
        num_results.append(random.randint(0,1000)) 
        
        #print("G", n, ": ", num_results[n], sep="")
    
    return num_results


def download_and_store_stories(stories_found, group=""):
    
    #request
    #storage loop
    #sql code
    
    print("storing")
    	
        #check response
    error_code = 200
    	
    if error_code == 200:
        stories_stored = stories_found
    else:
        stories_stored = 0
    
    return stories_stored



###############################################
###############################################

print("================================================\n", sep="")


results_by_group = get_group_info()

num_groups = len(results_by_group) 

while sum(results_by_group) > 0:

    for group, stories_to_dl in enumerate(results_by_group):
    
        if stories_to_dl == 0:
            continue
    
        if stories_to_dl >= 100:
            stories_to_dl = 100
        
        stories_dled = download_and_store_stories(
    	                stories_to_dl)
        
        print(stories_dled,
        	"stories downloaded for group", group)
        
        results_by_group[group] -= stories_dled
        







