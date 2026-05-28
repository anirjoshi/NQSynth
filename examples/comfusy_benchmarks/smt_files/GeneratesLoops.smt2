(set-logic NRA)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 1) Declare variables as Real
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(declare-fun x () Real)
(declare-fun y () Real)
(declare-fun z () Real)
(declare-fun delta () Real)
(declare-fun delta2 () Real)  ; Declared but unused for equality constraints

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 2) Integer-likeness constraints for x, y, z
;;    Each must be within +/- delta of an integer in [-10..10].
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; --- x: 
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

;; --- y:
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

;; --- z:
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

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 3) Translate Scala inequalities (constants a=-32, b=-32, c=-18)
;;
;;    (i)   c - y <= a - x*6       =>  -18 - y <= -32 - 6x
;;    (ii)  a - x*6 <= b + x + 7y  =>  -32 - 6x <= -32 + x + 7y
;;    (iii) x > y + z
;;    (iv)  9z <= x + y
;;    (v)   5z > b + x + 8  =>  5z > -32 + x + 8  => 5z > x - 24
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; (i)  c - y <= a - x*6
(assert (<= (- (+ -18 (* -1 y)) (+ -32 (* -6 x))) 0))
;; Alternatively in simpler prefix:
;; (assert (<= (+ -18 (* -1 y)) (+ -32 (* -6 x))))

;; (ii)  a - x*6 <= b + x + 7y
(assert (<= (+ -32 (* -6 x)) (+ -32 x (* 7 y))))

;; (iii) x > y + z
(assert (> x (+ y z)))

;; (iv)  9z <= x + y
(assert (<= (* 9 z) (+ x y)))

;; (v)   5z > x - 24
;; b = -32, b+8 = -24 => 5z > x + (-24)
(assert (> (* 5 z) (+ x -24)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4) Check satisfiability & get model
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(check-sat)
(get-model)
