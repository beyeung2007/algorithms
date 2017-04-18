<?php

// Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D are integers values in the array

// Note:

// 1) Return the indices `A1 B1 C1 D1`, so that 
//   A[A1] + A[B1] = A[C1] + A[D1]
//   A1 < B1, C1 < D1
//   A1 < C1, B1 != D1, B1 != C1 

// 2) If there are more than one solutions, 
//    then return the tuple of values which are lexicographical smallest. 

// Assume we have two solutions
// S1 : A1 B1 C1 D1 ( these are values of indices int the array )  
// S2 : A2 B2 C2 D2

// S1 is lexicographically smaller than S2 iff
//   A1 < A2 OR
//   A1 = A2 AND B1 < B2 OR
//   A1 = A2 AND B1 = B2 AND C1 < C2 OR 
//   A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
// Example:

// Input: [3, 4, 7, 1, 2, 9, 8]
// Output: [0, 2, 3, 5] (O index)
// If no solution is possible, return an empty list.

/**
 * Time: O(n^4)
 * Space: O(1)
 *
 */
function equal($arr) {
    if (empty($arr)) {
        return [];
    }
    $result = [];
    for ($i=0; $i < sizeof($arr); $i++) { 
        for ($j=$i+1; $j < sizeof($arr); $j++) { 
            $value = $arr[$i] + $arr[$j];
            $subResult = twoSum($arr, $value, $i, $j);
            if (!empty($subResult)) {
                $result[] = [$i, $j, $subResult[0], $subResult[1]];
            }
        }
    }
    return $result;
}

/**
 * Time: O(n^2)
 *
 */
function twoSum($arr, $val, $a, $b) {
    if (empty($arr)) {
        return [];
    }
    for ($i=0; $i < sizeof($arr); $i++) { 
        for ($j=$i+1; $j < sizeof($arr); $j++) { 
            if ($arr[$i] + $arr[$j] == $val &&
                $i != $a && $i != $b &&
                $j != $a && $j != $b) {
                return [$i, $j];
            }
        }
    }
    return [];
}

$arr1 = [3, 4, 7, 1, 2, 9, 8];

print_r(equal($arr1));
