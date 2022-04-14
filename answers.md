# CMPS 2200 Reciation 6
## Answers

**Name:** Keith J Mitchell


Place all written answers from `recitation-06.md` here for easier grading.

- **1b.**

Random:

|      n |         qsort_fixed |         qsort_random |
|--------|---------------------|----------------------|
|     10 |               0.026 |                0.235 |
|    100 |               0.328 |                0.439 |
|    200 |               0.703 |                0.951 |
|    300 |               1.086 |                1.308 |
|    400 |               1.558 |                2.478 |
|    500 |               2.694 |                2.568 |
|    600 |               7.494 |                8.531 |
|    700 |               9.044 |                9.149 |
|    800 |              10.023 |               10.629 |
|    900 |              10.778 |               10.353 |

Sorted:

|      n |         qsort_fixed |         qsort_random |
|--------|---------------------|----------------------|
|     10 |               0.030 |                0.050 |
|    100 |               1.371 |                0.419 |
|    200 |               4.631 |                0.957 |
|    300 |               9.760 |                1.337 |
|    400 |              18.002 |                1.948 |
|    500 |              26.545 |                2.377 |
|    600 |              68.204 |                6.029 |
|    700 |             123.969 |               13.163 |
|    800 |             334.147 |               16.163 |
|    900 |             533.443 |               11.843 |

  - Using a randomized list and/or pivot tends to lead to better runtimes. Using a fixed pivot like the first element tends to be inefficient as it is essentially like iterating through the list one at a time. 


- **1c.**

Random:

|      n |         qsort_fixed |         qsort_random |
|--------|---------------------|----------------------|
|     10 |               0.032 |                0.245 |
|    100 |               0.348 |                0.432 |
|    200 |               0.653 |                0.811 |
|    300 |               1.186 |                1.102 |
|    400 |               1.758 |                2.348 |
|    500 |               2.991 |                2.982 |
|    600 |               6.494 |                5.238 |
|    700 |               9.444 |                8.429 |
|    800 |              11.126 |               11.619 |
|    900 |              10.876 |               12.123 |

Sorted:

|      n |         qsort_fixed |         qsort_random |
|--------|---------------------|----------------------|
|     10 |               0.031 |                0.050 |
|    100 |               1.378 |                0.419 |
|    200 |               3.671 |                0.957 |
|    300 |               7.761 |                1.337 |
|    400 |              18.002 |                1.948 |
|    500 |              26.545 |                2.377 |
|    600 |              68.204 |                6.029 |
|    700 |             123.969 |               13.163 |
|    800 |             334.147 |               16.163 |
|    900 |             533.443 |               11.843 |

  - The results are similar to the ones seen in 1b. The fixed pivot results in the worst runtimes whereas the randomized lists and pivots result in far better runtimes. 