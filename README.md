# Algorithms

This is a simple repository where I code the algorithms I learned in my university courses. The purpose is to complement with the lecture analysis.


# Table of Contents

Topics                         |  Remark
--------------------------- |  ---------------------------
**Asymptotic Notation** | Big O,Theta, Omega, little o
**Proof by Induction**  | Assume n=k is true, prove n=k+1 also true
**Binary Tree/ Binary Search**  | O(logn)
**Comparison-based sorting** | -
Insertion sort  | O(n<sup>2</sup>), stable
Selection sort  | O(n<sup>2</sup>), not stable
Quick sort  | worst case O(nlogn), average O(nlogn), not stable
Merge sort  |  O(nlogn), stable
Binary heaps  | -
Heap sort   | O(nlogn), not stable
**Address-calculation sorting**  | -
Counting sort | O(n+k)
Bucket sort | O(n) + O(sum of s<sup>2</sup>)+ O(b)
Radix sort | O(nk)
**External sorting** | -
Polyphase Merge / Replacement Selection| -
**Greedy Algorithm**  | Find local maximum instead of global maximum
Fractional knapsack| Take all of the object with the highest values
Task scheduling to minimize the number of processors required| Order tasks by end time
Task scheduling on a uniprocessor to maximize the number of tasks that can be performed | Take the first one available and omit others
Huffman coding / Huffman trees | Assign coding to symbol, assign less bits to symbol with more frequency
**Divide and conquer**  | - 
Recurrence equation | T(n) = aT(n/b) + f(n)
Simplified method | compare a and n<sup>k</sup>
Master method | when f(n) is not of the form n<sup>k</sup>
Point-quadtree | Break into 4 problem, work on 1 of them
Integer multiplication | Improve to O(n<sup>log2 3</sup>)
Strassen's method | Improve to O(n<sup>log2 7</sup>)
**Selection and related problems**  | -
Finding the second largest  | Tournament Approach
Finding Maximum and Minimum | Break into pairs
Quick Select | Find the k<sup>th</sup> smallest
Deterministic Selection| Neither L nor G has more than (7n/10)+3 element
**Graphs** | -
Depth First Search | -
Breadth First Search | -
Connected Component Labeling | -
Auxiliary Graph | Find biconnected components
Strong Connectivity | Every point can go to any point in a direct graph
Topological Sorting | Check if directed graph has cycles (DAG)
**Weighted Graphs**| -
Dijkstra's shortest path Algorithm | O(mlogn), undirected graph and nonnegative weight
Bellman-Ford shortest path Algorithm | O(m*n), does not allow negative cycles
Prim-Jarnik MST Algorithm |  O(mlogn), Similar to Dijkstra
Kruskal's MST algorithm | O((M+n)logn)Process edges from smallest to largest
Baruvka's MST Algorithm | O(mlogn), merge clusters
Union-Find Algorithm | 
**Dynamic Programming** | -|-

