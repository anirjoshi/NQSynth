(set-logic NRA)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 1) Declare all variables as Real
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(declare-fun x () Real)
(declare-fun y () Real)
(declare-fun z () Real)
(declare-fun i () Real)
(declare-fun j () Real)
(declare-fun k () Real)
(declare-fun l () Real)
(declare-fun delta () Real)
(declare-fun delta2 () Real)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 2) For each of x, y, z, i, j, k, l, assert that it is within
;;    +/- delta of some integer from -10 to 10.
;;    That is:  (or (and -delta <= (v - -10) <= delta)
;;                 (and -delta <= (v - -9 ) <= delta)
;;                 ...
;;                 (and -delta <= (v - 10 ) <= delta) )
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; --- Constraints for x ---
(assert
 (or
  (and (>= (- x -10) (- delta)) (<= (- x -10) delta))
  (and (>= (- x -9)  (- delta)) (<= (- x -9)  delta))
  (and (>= (- x -8)  (- delta)) (<= (- x -8)  delta))
  (and (>= (- x -7)  (- delta)) (<= (- x -7)  delta))
  (and (>= (- x -6)  (- delta)) (<= (- x -6)  delta))
  (and (>= (- x -5)  (- delta)) (<= (- x -5)  delta))
  (and (>= (- x -4)  (- delta)) (<= (- x -4)  delta))
  (and (>= (- x -3)  (- delta)) (<= (- x -3)  delta))
  (and (>= (- x -2)  (- delta)) (<= (- x -2)  delta))
  (and (>= (- x -1)  (- delta)) (<= (- x -1)  delta))
  (and (>= (- x 0)   (- delta)) (<= (- x 0)   delta))
  (and (>= (- x 1)   (- delta)) (<= (- x 1)   delta))
  (and (>= (- x 2)   (- delta)) (<= (- x 2)   delta))
  (and (>= (- x 3)   (- delta)) (<= (- x 3)   delta))
  (and (>= (- x 4)   (- delta)) (<= (- x 4)   delta))
  (and (>= (- x 5)   (- delta)) (<= (- x 5)   delta))
  (and (>= (- x 6)   (- delta)) (<= (- x 6)   delta))
  (and (>= (- x 7)   (- delta)) (<= (- x 7)   delta))
  (and (>= (- x 8)   (- delta)) (<= (- x 8)   delta))
  (and (>= (- x 9)   (- delta)) (<= (- x 9)   delta))
  (and (>= (- x 10)  (- delta)) (<= (- x 10)  delta))
 )
)

;; --- Constraints for y ---
(assert
 (or
  (and (>= (- y -10) (- delta)) (<= (- y -10) delta))
  (and (>= (- y -9)  (- delta)) (<= (- y -9)  delta))
  (and (>= (- y -8)  (- delta)) (<= (- y -8)  delta))
  (and (>= (- y -7)  (- delta)) (<= (- y -7)  delta))
  (and (>= (- y -6)  (- delta)) (<= (- y -6)  delta))
  (and (>= (- y -5)  (- delta)) (<= (- y -5)  delta))
  (and (>= (- y -4)  (- delta)) (<= (- y -4)  delta))
  (and (>= (- y -3)  (- delta)) (<= (- y -3)  delta))
  (and (>= (- y -2)  (- delta)) (<= (- y -2)  delta))
  (and (>= (- y -1)  (- delta)) (<= (- y -1)  delta))
  (and (>= (- y 0)   (- delta)) (<= (- y 0)   delta))
  (and (>= (- y 1)   (- delta)) (<= (- y 1)   delta))
  (and (>= (- y 2)   (- delta)) (<= (- y 2)   delta))
  (and (>= (- y 3)   (- delta)) (<= (- y 3)   delta))
  (and (>= (- y 4)   (- delta)) (<= (- y 4)   delta))
  (and (>= (- y 5)   (- delta)) (<= (- y 5)   delta))
  (and (>= (- y 6)   (- delta)) (<= (- y 6)   delta))
  (and (>= (- y 7)   (- delta)) (<= (- y 7)   delta))
  (and (>= (- y 8)   (- delta)) (<= (- y 8)   delta))
  (and (>= (- y 9)   (- delta)) (<= (- y 9)   delta))
  (and (>= (- y 10)  (- delta)) (<= (- y 10)  delta))
 )
)

;; --- Constraints for z ---
(assert
 (or
  (and (>= (- z -10) (- delta)) (<= (- z -10) delta))
  (and (>= (- z -9)  (- delta)) (<= (- z -9)  delta))
  (and (>= (- z -8)  (- delta)) (<= (- z -8)  delta))
  (and (>= (- z -7)  (- delta)) (<= (- z -7)  delta))
  (and (>= (- z -6)  (- delta)) (<= (- z -6)  delta))
  (and (>= (- z -5)  (- delta)) (<= (- z -5)  delta))
  (and (>= (- z -4)  (- delta)) (<= (- z -4)  delta))
  (and (>= (- z -3)  (- delta)) (<= (- z -3)  delta))
  (and (>= (- z -2)  (- delta)) (<= (- z -2)  delta))
  (and (>= (- z -1)  (- delta)) (<= (- z -1)  delta))
  (and (>= (- z 0)   (- delta)) (<= (- z 0)   delta))
  (and (>= (- z 1)   (- delta)) (<= (- z 1)   delta))
  (and (>= (- z 2)   (- delta)) (<= (- z 2)   delta))
  (and (>= (- z 3)   (- delta)) (<= (- z 3)   delta))
  (and (>= (- z 4)   (- delta)) (<= (- z 4)   delta))
  (and (>= (- z 5)   (- delta)) (<= (- z 5)   delta))
  (and (>= (- z 6)   (- delta)) (<= (- z 6)   delta))
  (and (>= (- z 7)   (- delta)) (<= (- z 7)   delta))
  (and (>= (- z 8)   (- delta)) (<= (- z 8)   delta))
  (and (>= (- z 9)   (- delta)) (<= (- z 9)   delta))
  (and (>= (- z 10)  (- delta)) (<= (- z 10)  delta))
 )
)

;; --- Constraints for i ---
(assert
 (or
  (and (>= (- i -10) (- delta)) (<= (- i -10) delta))
  (and (>= (- i -9)  (- delta)) (<= (- i -9)  delta))
  (and (>= (- i -8)  (- delta)) (<= (- i -8)  delta))
  (and (>= (- i -7)  (- delta)) (<= (- i -7)  delta))
  (and (>= (- i -6)  (- delta)) (<= (- i -6)  delta))
  (and (>= (- i -5)  (- delta)) (<= (- i -5)  delta))
  (and (>= (- i -4)  (- delta)) (<= (- i -4)  delta))
  (and (>= (- i -3)  (- delta)) (<= (- i -3)  delta))
  (and (>= (- i -2)  (- delta)) (<= (- i -2)  delta))
  (and (>= (- i -1)  (- delta)) (<= (- i -1)  delta))
  (and (>= (- i 0)   (- delta)) (<= (- i 0)   delta))
  (and (>= (- i 1)   (- delta)) (<= (- i 1)   delta))
  (and (>= (- i 2)   (- delta)) (<= (- i 2)   delta))
  (and (>= (- i 3)   (- delta)) (<= (- i 3)   delta))
  (and (>= (- i 4)   (- delta)) (<= (- i 4)   delta))
  (and (>= (- i 5)   (- delta)) (<= (- i 5)   delta))
  (and (>= (- i 6)   (- delta)) (<= (- i 6)   delta))
  (and (>= (- i 7)   (- delta)) (<= (- i 7)   delta))
  (and (>= (- i 8)   (- delta)) (<= (- i 8)   delta))
  (and (>= (- i 9)   (- delta)) (<= (- i 9)   delta))
  (and (>= (- i 10)  (- delta)) (<= (- i 10)  delta))
 )
)

;; --- Constraints for j ---
(assert
 (or
  (and (>= (- j -10) (- delta)) (<= (- j -10) delta))
  (and (>= (- j -9)  (- delta)) (<= (- j -9)  delta))
  (and (>= (- j -8)  (- delta)) (<= (- j -8)  delta))
  (and (>= (- j -7)  (- delta)) (<= (- j -7)  delta))
  (and (>= (- j -6)  (- delta)) (<= (- j -6)  delta))
  (and (>= (- j -5)  (- delta)) (<= (- j -5)  delta))
  (and (>= (- j -4)  (- delta)) (<= (- j -4)  delta))
  (and (>= (- j -3)  (- delta)) (<= (- j -3)  delta))
  (and (>= (- j -2)  (- delta)) (<= (- j -2)  delta))
  (and (>= (- j -1)  (- delta)) (<= (- j -1)  delta))
  (and (>= (- j 0)   (- delta)) (<= (- j 0)   delta))
  (and (>= (- j 1)   (- delta)) (<= (- j 1)   delta))
  (and (>= (- j 2)   (- delta)) (<= (- j 2)   delta))
  (and (>= (- j 3)   (- delta)) (<= (- j 3)   delta))
  (and (>= (- j 4)   (- delta)) (<= (- j 4)   delta))
  (and (>= (- j 5)   (- delta)) (<= (- j 5)   delta))
  (and (>= (- j 6)   (- delta)) (<= (- j 6)   delta))
  (and (>= (- j 7)   (- delta)) (<= (- j 7)   delta))
  (and (>= (- j 8)   (- delta)) (<= (- j 8)   delta))
  (and (>= (- j 9)   (- delta)) (<= (- j 9)   delta))
  (and (>= (- j 10)  (- delta)) (<= (- j 10)  delta))
 )
)

;; --- Constraints for k ---
(assert
 (or
  (and (>= (- k -10) (- delta)) (<= (- k -10) delta))
  (and (>= (- k -9)  (- delta)) (<= (- k -9)  delta))
  (and (>= (- k -8)  (- delta)) (<= (- k -8)  delta))
  (and (>= (- k -7)  (- delta)) (<= (- k -7)  delta))
  (and (>= (- k -6)  (- delta)) (<= (- k -6)  delta))
  (and (>= (- k -5)  (- delta)) (<= (- k -5)  delta))
  (and (>= (- k -4)  (- delta)) (<= (- k -4)  delta))
  (and (>= (- k -3)  (- delta)) (<= (- k -3)  delta))
  (and (>= (- k -2)  (- delta)) (<= (- k -2)  delta))
  (and (>= (- k -1)  (- delta)) (<= (- k -1)  delta))
  (and (>= (- k 0)   (- delta)) (<= (- k 0)   delta))
  (and (>= (- k 1)   (- delta)) (<= (- k 1)   delta))
  (and (>= (- k 2)   (- delta)) (<= (- k 2)   delta))
  (and (>= (- k 3)   (- delta)) (<= (- k 3)   delta))
  (and (>= (- k 4)   (- delta)) (<= (- k 4)   delta))
  (and (>= (- k 5)   (- delta)) (<= (- k 5)   delta))
  (and (>= (- k 6)   (- delta)) (<= (- k 6)   delta))
  (and (>= (- k 7)   (- delta)) (<= (- k 7)   delta))
  (and (>= (- k 8)   (- delta)) (<= (- k 8)   delta))
  (and (>= (- k 9)   (- delta)) (<= (- k 9)   delta))
  (and (>= (- k 10)  (- delta)) (<= (- k 10)  delta))
 )
)

;; --- Constraints for l ---
(assert
 (or
  (and (>= (- l -10) (- delta)) (<= (- l -10) delta))
  (and (>= (- l -9)  (- delta)) (<= (- l -9)  delta))
  (and (>= (- l -8)  (- delta)) (<= (- l -8)  delta))
  (and (>= (- l -7)  (- delta)) (<= (- l -7)  delta))
  (and (>= (- l -6)  (- delta)) (<= (- l -6)  delta))
  (and (>= (- l -5)  (- delta)) (<= (- l -5)  delta))
  (and (>= (- l -4)  (- delta)) (<= (- l -4)  delta))
  (and (>= (- l -3)  (- delta)) (<= (- l -3)  delta))
  (and (>= (- l -2)  (- delta)) (<= (- l -2)  delta))
  (and (>= (- l -1)  (- delta)) (<= (- l -1)  delta))
  (and (>= (- l 0)   (- delta)) (<= (- l 0)   delta))
  (and (>= (- l 1)   (- delta)) (<= (- l 1)   delta))
  (and (>= (- l 2)   (- delta)) (<= (- l 2)   delta))
  (and (>= (- l 3)   (- delta)) (<= (- l 3)   delta))
  (and (>= (- l 4)   (- delta)) (<= (- l 4)   delta))
  (and (>= (- l 5)   (- delta)) (<= (- l 5)   delta))
  (and (>= (- l 6)   (- delta)) (<= (- l 6)   delta))
  (and (>= (- l 7)   (- delta)) (<= (- l 7)   delta))
  (and (>= (- l 8)   (- delta)) (<= (- l 8)   delta))
  (and (>= (- l 9)   (- delta)) (<= (- l 9)   delta))
  (and (>= (- l 10)  (- delta)) (<= (- l 10)  delta))
 )
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 3) Constraints from Scala code:
;;    (i)   i == l * (x*y) + k * x + j
;;          ==> -delta2 <= i - [l*(x*y) + k*x + j] <= delta2
;;    (ii)  0 <= j
;;    (iii) j < x
;;    (iv)  0 <= k
;;    (v)   k < y
;;    (vi)  0 <= l
;;    (vii) l < z
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; i == l*(x*y) + k*x + j, with approximation by delta2
(assert (<= (- i (+ (* l (* x y)) (* k x) j)) delta2))
(assert (>= (- i (+ (* l (* x y)) (* k x) j)) (- delta2)))

;; 0 <= j
(assert (>= j 0))

;; j < x
(assert (< j x))

;; 0 <= k
(assert (>= k 0))

;; k < y
(assert (< k y))

;; 0 <= l
(assert (>= l 0))

;; l < z
(assert (< l z))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4

(check-sat)
(get-model)