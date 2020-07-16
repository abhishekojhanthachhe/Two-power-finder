# Two-power-finder
This program is built to find the power of 2 after 65536 which does not have the digits 2, 4, or 8.

## About
This uses the multiprocessing module of python to carry out the said task. The number of threads involved for parrallel processing can be modified with the threads variable and the upper and lower limit of the search index can be modified with the s and u variables, respectively.

The reason for using python's standard library, and not something like PyOpenCL, is its ease in handling infinite precision integers.

Research has shown us that upto 2^40000000000 (40 billion) has already been checked with no positive results. We plan to check upto 2^100000000000 (1 trillion).

The first version of the code was written by Kiwi and further improvements were made by Kiwi and A___P___O___.

The following people are thanked for providing their valuable computational resources for running this code:

A___P___O___
Kiwi
Bipa
Jaya Ojha
If anyone wants to contribute by providing your computational resource, please contact us at:

Email: a.pd.ojha@gmail.com
Twitter: @AbhishekPrasadO [Kiwi, insert your credentials here]
