# Code Explanation

My main idea behind solving this problem was to make use of a combination of a Tree and binary Trie data structure for storing different rules. I call this the RulesDataStore.

### Components of RulesDataStore Tree

The RulesDataStore Tree is formed through 5 different types of nodes. The name of the nodes and their explanations are given as under :

* HeadNode - The starting node of the RulesDataStore Tree. Contains a `directions` dictionary that maps different `DirectionNode` nodes to it. There is only one HeadNode in the whole RulesDataStore Tree

* DirectionNode - A node which stores a direction and reference of the protocol nodes connected to it. Contains a `protocols` dictionary that maps different `ProtocolNode` nodes to it. 

* ProtocolNode - A node which stores a protocol and reference of the port nodes connected to it. Contains a `ports` dictionary that maps different `PortNode` nodes to it. 

*  PortNode - A node which stores a direction and a reference to the root of an IP address Trie (`IPTrieNode`), which is used to store different ip-addresses in a port.

* IPTrieNode - A node which forms the basic building block of the binary trie that is used to store different ip addresses.

The structure of IP Trie has been explained [here](https://github.com/UjjwalChallenge/FirewallChallenge/blob/master/Submission%20Docs/ip_trie_explanation.md) 

### Structure of RulesDataStore 
* It is a tree that contains 4 main levels (Discluding the IP Trie levels). 
  * Level 1 : Formed by the `HeadNode`. It matches the direction of a packet with the appropriate `DirectionNode`.
  * Level 2 : Formed by the `DirectionNode`. It matches the protocol of a packet with the appropriate `ProtocolNode`.
  * Level 3 : Formed by the `ProtocolNode`. It matches the port of a packet with the appropriate `PortNode`.
  * Level 4 : Formed by the `PortNode`. It contains a reference to an `IPTrieNode` which it uses to match the ip address of the packet. 

### Example

The following image shows the state of the data store when the rule `inbound,tcp,80,192.168.1.2-192.168.1.5` is read by the firewall and it's output when it receives the following packets :
- packet 1 : `inbound tcp, 80, 192.168.1.2` [GETS ACCEPTED]
- packet 2 : `inbound tcp, 80, 192.168.1.1` [GETS BLOCKED]

![here](https://github.com/UjjwalChallenge/FirewallChallenge/blob/master/Submission%20Docs/example_datastore.png)

