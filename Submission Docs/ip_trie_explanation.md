### IP Trie Explanation

The IP addresses are stored in a trie. Each node of the trie has 2 fields :
* root = Stores the value of the current node (0 or 1)
* children = A dictionary object with 2 keys - "0" and "1"

Each octet of the ip address is first converted into their binary equivalent. 

192.168.1.2 becomes  11000000.10101000.00000001.00000010

and then stored in the trie. 

An example of how `5` would be stored in this trie (the preceding 0s are omitted in the figure for better understanding)

<p align="center">
<img src="https://github.com/UjjwalChallenge/FirewallChallenge/blob/master/Submission%20Docs/IP_Trie.png" width="200">
</p>
