# Challenge
[![Build Status](https://travis-ci.com/UjjwalChallenge/Challenge.svg?branch=master)](https://travis-ci.com/UjjwalChallenge/Challenge)


This repository contains the code for challenge given by Illumio. 

The source code for the required Firewall class can be found [here](https://github.com/UjjwalChallenge/Challenge/blob/master/firewall/firewall.py)

## Table of Contents

* Basic Usage

```python
from firewall.firewall import Firewall

fw = Firewall('data.csv')
print(fw.accept_packet("inbound", "tcp", "80", "192.168.1.2"))
print(fw.accept_packet("outbound", "tcp", "20000", "192.168.10.11"))
```
Output
```
(True, 'Valid')
(True, 'Valid')
```



* [Code Explanation](https://github.com/UjjwalChallenge/Challenge/blob/master/Submission%20Docs/code_explanation.md)
* [Things I would have liked to do if I had more time](https://github.com/UjjwalChallenge/Challenge/blob/master/Submission%20Docs/improvements.md)
* [Teams I would like to work with](https://github.com/UjjwalChallenge/Challenge/blob/master/Submission%20Docs/teams_interested.md)
* [References used](https://github.com/UjjwalChallenge/Challenge/blob/master/Submission%20Docs/references.md)


##### I would like to give very special thanks to Illumio for perceiving a potential for a strong fit between my skills and their team's hiring needs and giving me an opportunity to work on this challenge. It was amazing. I admit that I spent more than 2 hours on this problem because it had more elements (design, tests, structure, readability) than just coming up with an efficient solution to the problem, which made this challenge even more enjoyable. I had a great time working on this and I feel that I learned a lot during the process. 


Submitted By : [Ujjwal Ayyangar](https://github.com/UjjwalAyyangar)
 
