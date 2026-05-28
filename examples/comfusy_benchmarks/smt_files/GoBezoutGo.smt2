(set-logic NRA)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 1) Declare all variables as Real
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(declare-fun i () Real)
(declare-fun a () Real)
(declare-fun b () Real)
(declare-fun c () Real)
(declare-fun x () Real)
(declare-fun y () Real)
(declare-fun z () Real)
(declare-fun delta () Real)
(declare-fun delta2 () Real)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 2) Integer-likeness constraints for i, a, b, c, x, y, z.
;;    Each must be within +/- delta of an integer in [-10..10].
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; --- i ---
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

;; --- a ---
(assert
 (or
  (and (>= (- a -10) (- delta)) (<= (- a -10) delta))
  (and (>= (- a -9)  (- delta)) (<= (- a -9)  delta))
  (and (>= (- a -8)  (- delta)) (<= (- a -8)  delta))
  (and (>= (- a -7)  (- delta)) (<= (- a -7)  delta))
  (and (>= (- a -6)  (- delta)) (<= (- a -6)  delta))
  (and (>= (- a -5)  (- delta)) (<= (- a -5)  delta))
  (and (>= (- a -4)  (- delta)) (<= (- a -4)  delta))
  (and (>= (- a -3)  (- delta)) (<= (- a -3)  delta))
  (and (>= (- a -2)  (- delta)) (<= (- a -2)  delta))
  (and (>= (- a -1)  (- delta)) (<= (- a -1)  delta))
  (and (>= (- a 0)   (- delta)) (<= (- a 0)   delta))
  (and (>= (- a 1)   (- delta)) (<= (- a 1)   delta))
  (and (>= (- a 2)   (- delta)) (<= (- a 2)   delta))
  (and (>= (- a 3)   (- delta)) (<= (- a 3)   delta))
  (and (>= (- a 4)   (- delta)) (<= (- a 4)   delta))
  (and (>= (- a 5)   (- delta)) (<= (- a 5)   delta))
  (and (>= (- a 6)   (- delta)) (<= (- a 6)   delta))
  (and (>= (- a 7)   (- delta)) (<= (- a 7)   delta))
  (and (>= (- a 8)   (- delta)) (<= (- a 8)   delta))
  (and (>= (- a 9)   (- delta)) (<= (- a 9)   delta))
  (and (>= (- a 10)  (- delta)) (<= (- a 10)  delta))
 )
)

;; --- b ---
(assert
 (or
  (and (>= (- b -10) (- delta)) (<= (- b -10) delta))
  (and (>= (- b -9)  (- delta)) (<= (- b -9)  delta))
  (and (>= (- b -8)  (- delta)) (<= (- b -8)  delta))
  (and (>= (- b -7)  (- delta)) (<= (- b -7)  delta))
  (and (>= (- b -6)  (- delta)) (<= (- b -6)  delta))
  (and (>= (- b -5)  (- delta)) (<= (- b -5)  delta))
  (and (>= (- b -4)  (- delta)) (<= (- b -4)  delta))
  (and (>= (- b -3)  (- delta)) (<= (- b -3)  delta))
  (and (>= (- b -2)  (- delta)) (<= (- b -2)  delta))
  (and (>= (- b -1)  (- delta)) (<= (- b -1)  delta))
  (and (>= (- b 0)   (- delta)) (<= (- b 0)   delta))
  (and (>= (- b 1)   (- delta)) (<= (- b 1)   delta))
  (and (>= (- b 2)   (- delta)) (<= (- b 2)   delta))
  (and (>= (- b 3)   (- delta)) (<= (- b 3)   delta))
  (and (>= (- b 4)   (- delta)) (<= (- b 4)   delta))
  (and (>= (- b 5)   (- delta)) (<= (- b 5)   delta))
  (and (>= (- b 6)   (- delta)) (<= (- b 6)   delta))
  (and (>= (- b 7)   (- delta)) (<= (- b 7)   delta))
  (and (>= (- b 8)   (- delta)) (<= (- b 8)   delta))
  (and (>= (- b 9)   (- delta)) (<= (- b 9)   delta))
  (and (>= (- b 10)  (- delta)) (<= (- b 10)  delta))
 )
)

;; --- c ---
(assert
 (or
  (and (>= (- c -10) (- delta)) (<= (- c -10) delta))
  (and (>= (- c -9)  (- delta)) (<= (- c -9)  delta))
  (and (>= (- c -8)  (- delta)) (<= (- c -8)  delta))
  (and (>= (- c -7)  (- delta)) (<= (- c -7)  delta))
  (and (>= (- c -6)  (- delta)) (<= (- c -6)  delta))
  (and (>= (- c -5)  (- delta)) (<= (- c -5)  delta))
  (and (>= (- c -4)  (- delta)) (<= (- c -4)  delta))
  (and (>= (- c -3)  (- delta)) (<= (- c -3)  delta))
  (and (>= (- c -2)  (- delta)) (<= (- c -2)  delta))
  (and (>= (- c -1)  (- delta)) (<= (- c -1)  delta))
  (and (>= (- c 0)   (- delta)) (<= (- c 0)   delta))
  (and (>= (- c 1)   (- delta)) (<= (- c 1)   delta))
  (and (>= (- c 2)   (- delta)) (<= (- c 2)   delta))
  (and (>= (- c 3)   (- delta)) (<= (- c 3)   delta))
  (and (>= (- c 4)   (- delta)) (<= (- c 4)   delta))
  (and (>= (- c 5)   (- delta)) (<= (- c 5)   delta))
  (and (>= (- c 6)   (- delta)) (<= (- c 6)   delta))
  (and (>= (- c 7)   (- delta)) (<= (- c 7)   delta))
  (and (>= (- c 8)   (- delta)) (<= (- c 8)   delta))
  (and (>= (- c 9)   (- delta)) (<= (- c 9)   delta))
  (and (>= (- c 10)  (- delta)) (<= (- c 10)  delta))
 )
)

;; --- x ---
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

;; --- y ---
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

;; --- z ---
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
;; 3) Equality constraint:
;;    i + a*x + b*y + c*z == 0
;;    => -delta2 <= (i + a*x + b*y + c*z) <= delta2
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(assert (<= (+ i (* a x) (* b y) (* c z)) delta2))
(assert (>= (+ i (* a x) (* b y) (* c z)) (- delta2)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4) Finally, check satisfiability and get a model
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(check-sat)
(get-model)
