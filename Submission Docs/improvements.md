# Improvements

##### Approaches that came to my mind during the challenge. 
* Brute-Force approach : Maintain a list of all the rules (generate new rules when the rule input contains a range). On receiving a packet, to check whether it is accepted or not, iterate over all the rules and check one by one. 
* Better Brute-Force approach : Just like before, maintain a list of all the rules(generating new ones when the rule input contains a range) and store them in a dictionary/hash-table in the format -> RulesStore[rule] = True (if it exists), False otherwise. While such a solution would give us the answer in just 1 lookup, I decided against implementing it because of its high space complexity. I would have had to create a new key for two rules even if they had only minor differences(eg: only one octet of an ipaddress is different between two rules). 
* A Tree with IP Address hash : A RulesDataStore tree with a structure similar to the [one I have implemented](https://github.com/UjjwalChallenge/Challenge/blob/master/Submission%20Docs/code_explanation.md). The only difference being, at level 4, I make use of hash-table, converting ipaddresses into hashes and storing them as a key.

However taking time and space complexity into account, I figured out that the best way to store IP addresses would be 
using a binary trie data structure. I have explained this structure  [here](https://github.com/UjjwalChallenge/Challenge/blob/master/Submission%20Docs/ip_trie_explanation.md)

##### Things I would have liked to explore/try
* Right now, the rules data-store tries to add a new rule again even if it is already present in the data store if there
is a range element (an ip range or a port range) present. To fix this, I was thinking of merging the rules as I read 
them line by line through the .csv file. This problem can be reduced to the [merge intervals problem](https://www.geeksforgeeks.org/merging-intervals/)
* Move code and fix imports in different python files to prevent the problem of circular imports.
* Generate more test cases 
* I discovered the python's standard ipaddress library towards the very end of my implementation. I would have liked to explore it more 
and find out if it offers any efficient ip address matching capabilities or not

##### Note to reviewer : 

During the challenge, apart from focusing on the performance/efficiency of the code, I also tried to focus on the 
structure of the system. How it would be represented through classes and interface(if any) and which creational design
patterns could be applied here. I wanted the structure to be easily extensible and flexible with constant changes in
requirements, modular, usable and readable so that it can resist software erosion for as long as possible and reduce 
upkeep cost of development. As a result, I ended up spending more than 2 hours on this challenge. 


