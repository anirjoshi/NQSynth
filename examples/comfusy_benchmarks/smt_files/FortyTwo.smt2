(set-logic NRA)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 1) Declare variables as Real
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(declare-fun z () Real)
(declare-fun x () Real)
(declare-fun y () Real)
(declare-fun delta () Real)
(declare-fun delta2 () Real)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 2) Integer-likeness constraints for z, x, y
;;    Each must be within +/- delta of an integer in [-10..10].
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

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

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 3) The equality  z = 42*x + 5*y  => approximate with delta2
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; z - (42*x + 5*y) <= delta2
(assert (<= (- z (+ (* 42 x) (* 5 y))) delta2))

;; z - (42*x + 5*y) >= -delta2
(assert (>= (- z (+ (* 42 x) (* 5 y))) (- delta2)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4) Check satisfiability & get a model
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(check-sat)
(get-model)
