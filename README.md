# Algorithms

This is a simple repository where I code the algorithms I learned in my university courses. The purpose is to complement with the lecture analysis.


# Table of Contents

Topics                         |  Remark
--------------------------- |  ---------------------------
**Asymptotic Notation** | Big O,Theta, Omega, little o
**Proof by Induction**  | Assume n=k is true, prove n=k+1 also true
**Binary Tree/ Binary Search**  | O(logn)
**Comparison-based sorting** | -
[Insertion sort](https://github.com/yatw/Algorithms/blob/master/SelectionSort.py)  | O(n<sup>2</sup>), stable
[Selection sort](https://github.com/yatw/Algorithms/blob/master/SelectionSort.py)  | O(n<sup>2</sup>), not stable
[Quick sort](https://github.com/yatw/Algorithms/blob/master/QuickSort.py)  | worst case O(nlogn), average O(nlogn), not stable
[Merge sort](https://github.com/yatw/Algorithms/blob/master/MergeSort.py)  |  O(nlogn), stable
[Binary heaps](https://github.com/yatw/Algorithms/blob/master/BinaryHeap.py)  | -
[Heap sort](https://github.com/yatw/Algorithms/blob/master/HeapSort.py)   | O(nlogn), not stable
**Address-calculation sorting**  | -
Counting sort | O(n+k)
Bucket sort | O(n) + O(sum of s<sup>2</sup>)+ O(b)
Radix sort | O(nk)
**External sorting** | Used when data is too large for memory
Polyphase Merge / Replacement Selection| -
**Greedy Algorithm**  | Find local maximum instead of global maximum
Fractional knapsack| Take all of the object with the highest values
Task scheduling to minimize the number of processors required| Order tasks by star time
Task scheduling on a uniprocessor to maximize the number of tasks that can be performed | Order tasks by end time
Huffman coding / Huffman trees | Assign coding to symbol, assign less bits to symbol with more frequency
**Divide and conquer**  | - 
Recurrence equation | T(n) = aT(n/b) + f(n)
Simplified method | compare a and n<sup>k</sup>
Master method | when f(n) is not of the form n<sup>k</sup>
Point-quadtree | Break into 4 problem, work on 1 of them
Integer multiplication | Improve to O(n<sup>log2 3</sup>)
Strassen's method | Improve to O(n<sup>log2 7</sup>)
**Selection and related problems**  | -
[Finding the second largest (Tournament Approach)](https://github.com/yatw/Algorithms/blob/master/Tournament.py)  | O(n-1 + logn-1)
[Finding Maximum and Minimum (Break into pairs)](https://github.com/yatw/Algorithms/blob/master/MaxAndMin.py) | O( 3((n/2)-1) + 2)
[Quick Select](https://github.com/yatw/Algorithms/blob/master/QuickSelect.py) | Find the k<sup>th</sup> smallest
[Deterministic Selection](https://github.com/yatw/Algorithms/blob/master/DeterministicSelection.py)| Advance version of quick select
**[Graphs](https://github.com/yatw/Algorithms/blob/master/Graph.py)** | -
[Depth First Search](https://github.com/yatw/Algorithms/blob/master/DepthFirstSearch.py) | Keep going alone a path and back out
[Breadth First Search](https://github.com/yatw/Algorithms/blob/master/BreadthFirstSearch.py) | Each level branch out from visited notes
[Connected Component Labeling](https://github.com/yatw/Algorithms/blob/master/ConnectedComponentLabeling.py) | Group them if they are connected
[Auxiliary Graph](https://github.com/yatw/Algorithms/blob/master/BiconnectedComponentAlgorithm.py) | Find biconnected components
[Strong Connectivity](https://github.com/yatw/Algorithms/blob/master/StrongConnectivity.py) | Every point can go to any point in a direct graph
[Topological Sorting](https://github.com/yatw/Algorithms/blob/master/TopologicalSort.py) | Find a way to visit all nodes according to prequisite
**Weighted Graphs**| -
[Dijkstra's shortest path Algorithm](https://github.com/yatw/Algorithms/blob/master/DijkstraAlgorithm.py) | O(mlogn), no nonnegative weight
[Bellman-Ford shortest path Algorithm](https://github.com/yatw/Algorithms/blob/master/BellmanFordAlgorithm.py) | O(m*n), no negative cycles
[Prim-Jarnik MST Algorithm](https://github.com/yatw/Algorithms/blob/master/Prim-JarnikMST.py)  |  O(mlogn), Similar to Dijkstra, pick the shortest outgoing edge to connect
Kruskal's MST algorithm | O((M+n)logn)Process edges from smallest to largest, take the edge if it is not in the same tree
Baruvka's MST Algorithm | O(mlogn), merge clusters
Union-Find Algorithm | 
**Dynamic Programming** | -|-

