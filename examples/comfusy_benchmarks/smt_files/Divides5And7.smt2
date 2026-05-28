(set-logic NRA)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 1) Declare all variables as Real
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(declare-fun y () Real)
(declare-fun b () Real)
(declare-fun c () Real)
(declare-fun a1 () Real)
(declare-fun a2 () Real)
(declare-fun delta () Real)
(declare-fun delta2 () Real)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 2) "Integer-likeness" constraints for y, b, c 
;;    Each must be within +/- delta of an integer in [-10..10].
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

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

;; --- Constraints for b ---
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

;; --- Constraints for c ---
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

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 3) "Integer-likeness" for a1, a2, but excluding 0
;;    => each is within +/- delta of an integer in [-10..-1, 1..10].
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; --- Constraints for a1 (a1 != 0) ---
(assert
 (or
  (and (>= (- a1 -10) (- delta)) (<= (- a1 -10) delta))
  (and (>= (- a1 -9)  (- delta)) (<= (- a1 -9)  delta))
  (and (>= (- a1 -8)  (- delta)) (<= (- a1 -8)  delta))
  (and (>= (- a1 -7)  (- delta)) (<= (- a1 -7)  delta))
  (and (>= (- a1 -6)  (- delta)) (<= (- a1 -6)  delta))
  (and (>= (- a1 -5)  (- delta)) (<= (- a1 -5)  delta))
  (and (>= (- a1 -4)  (- delta)) (<= (- a1 -4)  delta))
  (and (>= (- a1 -3)  (- delta)) (<= (- a1 -3)  delta))
  (and (>= (- a1 -2)  (- delta)) (<= (- a1 -2)  delta))
  (and (>= (- a1 -1)  (- delta)) (<= (- a1 -1)  delta))
  (and (>= (- a1 1)   (- delta)) (<= (- a1 1)   delta))
  (and (>= (- a1 2)   (- delta)) (<= (- a1 2)   delta))
  (and (>= (- a1 3)   (- delta)) (<= (- a1 3)   delta))
  (and (>= (- a1 4)   (- delta)) (<= (- a1 4)   delta))
  (and (>= (- a1 5)   (- delta)) (<= (- a1 5)   delta))
  (and (>= (- a1 6)   (- delta)) (<= (- a1 6)   delta))
  (and (>= (- a1 7)   (- delta)) (<= (- a1 7)   delta))
  (and (>= (- a1 8)   (- delta)) (<= (- a1 8)   delta))
  (and (>= (- a1 9)   (- delta)) (<= (- a1 9)   delta))
  (and (>= (- a1 10)  (- delta)) (<= (- a1 10)  delta))
 )
)

;; --- Constraints for a2 (a2 != 0) ---
(assert
 (or
  (and (>= (- a2 -10) (- delta)) (<= (- a2 -10) delta))
  (and (>= (- a2 -9)  (- delta)) (<= (- a2 -9)  delta))
  (and (>= (- a2 -8)  (- delta)) (<= (- a2 -8)  delta))
  (and (>= (- a2 -7)  (- delta)) (<= (- a2 -7)  delta))
  (and (>= (- a2 -6)  (- delta)) (<= (- a2 -6)  delta))
  (and (>= (- a2 -5)  (- delta)) (<= (- a2 -5)  delta))
  (and (>= (- a2 -4)  (- delta)) (<= (- a2 -4)  delta))
  (and (>= (- a2 -3)  (- delta)) (<= (- a2 -3)  delta))
  (and (>= (- a2 -2)  (- delta)) (<= (- a2 -2)  delta))
  (and (>= (- a2 -1)  (- delta)) (<= (- a2 -1)  delta))
  (and (>= (- a2 1)   (- delta)) (<= (- a2 1)   delta))
  (and (>= (- a2 2)   (- delta)) (<= (- a2 2)   delta))
  (and (>= (- a2 3)   (- delta)) (<= (- a2 3)   delta))
  (and (>= (- a2 4)   (- delta)) (<= (- a2 4)   delta))
  (and (>= (- a2 5)   (- delta)) (<= (- a2 5)   delta))
  (and (>= (- a2 6)   (- delta)) (<= (- a2 6)   delta))
  (and (>= (- a2 7)   (- delta)) (<= (- a2 7)   delta))
  (and (>= (- a2 8)   (- delta)) (<= (- a2 8)   delta))
  (and (>= (- a2 9)   (- delta)) (<= (- a2 9)   delta))
  (and (>= (- a2 10)  (- delta)) (<= (- a2 10)  delta))
 )
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4) Constraints from Scala code:
;;    (i)   (y + b) == 5 * a1
;;          => -delta2 <= (y + b) - (5*a1) <= delta2
;;
;;    (ii)  (y + c) == 7 * a2
;;          => -delta2 <= (y + c) - (7*a2) <= delta2
;;
;;    (iii) b > 0
;;    (iv)  c > 0
;;    (v)   a1 != 0 (already enforced by skipping integer 0)
;;    (vi)  a2 != 0 (already enforced likewise)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; (y + b) - (5*a1) <= delta2
(assert (<= (- (+ y b) (* 5 a1)) delta2))

;; (y + b) - (5*a1) >= -delta2
(assert (>= (- (+ y b) (* 5 a1)) (- delta2)))

;; (y + c) - (7*a2) <= delta2
(assert (<= (- (+ y c) (* 7 a2)) delta2))

;; (y + c) - (7*a2) >= -delta2
(assert (>= (- (+ y c) (* 7 a2)) (- delta2)))

;; b > 0
(assert (> b 0))

;; c > 0
(assert (> c 0))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 5) Check satisfiability & get a model
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(check-sat)
(get-model)
