(set-logic NRA)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 1) Declare variables as Real
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(declare-fun total () Real)
(declare-fun limit1 () Real)
(declare-fun limit2 () Real)
(declare-fun limit3 () Real)
(declare-fun a () Real)
(declare-fun b () Real)
(declare-fun c () Real)
(declare-fun d () Real)
(declare-fun delta () Real)
(declare-fun delta2 () Real)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 2) Integer-likeness constraints for total, limit1, limit2,
;;    limit3, a, b, c, d. Each must be within +/- delta
;;    of an integer in [-10..10].
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; --- total ---
(assert
 (or
  (and (>= (- total -10) (- delta)) (<= (- total -10) delta))
  (and (>= (- total -9)  (- delta)) (<= (- total -9)  delta))
  (and (>= (- total -8)  (- delta)) (<= (- total -8)  delta))
  (and (>= (- total -7)  (- delta)) (<= (- total -7)  delta))
  (and (>= (- total -6)  (- delta)) (<= (- total -6)  delta))
  (and (>= (- total -5)  (- delta)) (<= (- total -5)  delta))
  (and (>= (- total -4)  (- delta)) (<= (- total -4)  delta))
  (and (>= (- total -3)  (- delta)) (<= (- total -3)  delta))
  (and (>= (- total -2)  (- delta)) (<= (- total -2)  delta))
  (and (>= (- total -1)  (- delta)) (<= (- total -1)  delta))
  (and (>= (- total 0)   (- delta)) (<= (- total 0)   delta))
  (and (>= (- total 1)   (- delta)) (<= (- total 1)   delta))
  (and (>= (- total 2)   (- delta)) (<= (- total 2)   delta))
  (and (>= (- total 3)   (- delta)) (<= (- total 3)   delta))
  (and (>= (- total 4)   (- delta)) (<= (- total 4)   delta))
  (and (>= (- total 5)   (- delta)) (<= (- total 5)   delta))
  (and (>= (- total 6)   (- delta)) (<= (- total 6)   delta))
  (and (>= (- total 7)   (- delta)) (<= (- total 7)   delta))
  (and (>= (- total 8)   (- delta)) (<= (- total 8)   delta))
  (and (>= (- total 9)   (- delta)) (<= (- total 9)   delta))
  (and (>= (- total 10)  (- delta)) (<= (- total 10)  delta))
 )
)

;; --- limit1 ---
(assert
 (or
  (and (>= (- limit1 -10) (- delta)) (<= (- limit1 -10) delta))
  (and (>= (- limit1 -9)  (- delta)) (<= (- limit1 -9)  delta))
  (and (>= (- limit1 -8)  (- delta)) (<= (- limit1 -8)  delta))
  (and (>= (- limit1 -7)  (- delta)) (<= (- limit1 -7)  delta))
  (and (>= (- limit1 -6)  (- delta)) (<= (- limit1 -6)  delta))
  (and (>= (- limit1 -5)  (- delta)) (<= (- limit1 -5)  delta))
  (and (>= (- limit1 -4)  (- delta)) (<= (- limit1 -4)  delta))
  (and (>= (- limit1 -3)  (- delta)) (<= (- limit1 -3)  delta))
  (and (>= (- limit1 -2)  (- delta)) (<= (- limit1 -2)  delta))
  (and (>= (- limit1 -1)  (- delta)) (<= (- limit1 -1)  delta))
  (and (>= (- limit1 0)   (- delta)) (<= (- limit1 0)   delta))
  (and (>= (- limit1 1)   (- delta)) (<= (- limit1 1)   delta))
  (and (>= (- limit1 2)   (- delta)) (<= (- limit1 2)   delta))
  (and (>= (- limit1 3)   (- delta)) (<= (- limit1 3)   delta))
  (and (>= (- limit1 4)   (- delta)) (<= (- limit1 4)   delta))
  (and (>= (- limit1 5)   (- delta)) (<= (- limit1 5)   delta))
  (and (>= (- limit1 6)   (- delta)) (<= (- limit1 6)   delta))
  (and (>= (- limit1 7)   (- delta)) (<= (- limit1 7)   delta))
  (and (>= (- limit1 8)   (- delta)) (<= (- limit1 8)   delta))
  (and (>= (- limit1 9)   (- delta)) (<= (- limit1 9)   delta))
  (and (>= (- limit1 10)  (- delta)) (<= (- limit1 10)  delta))
 )
)

;; --- limit2 ---
(assert
 (or
  (and (>= (- limit2 -10) (- delta)) (<= (- limit2 -10) delta))
  (and (>= (- limit2 -9)  (- delta)) (<= (- limit2 -9)  delta))
  (and (>= (- limit2 -8)  (- delta)) (<= (- limit2 -8)  delta))
  (and (>= (- limit2 -7)  (- delta)) (<= (- limit2 -7)  delta))
  (and (>= (- limit2 -6)  (- delta)) (<= (- limit2 -6)  delta))
  (and (>= (- limit2 -5)  (- delta)) (<= (- limit2 -5)  delta))
  (and (>= (- limit2 -4)  (- delta)) (<= (- limit2 -4)  delta))
  (and (>= (- limit2 -3)  (- delta)) (<= (- limit2 -3)  delta))
  (and (>= (- limit2 -2)  (- delta)) (<= (- limit2 -2)  delta))
  (and (>= (- limit2 -1)  (- delta)) (<= (- limit2 -1)  delta))
  (and (>= (- limit2 0)   (- delta)) (<= (- limit2 0)   delta))
  (and (>= (- limit2 1)   (- delta)) (<= (- limit2 1)   delta))
  (and (>= (- limit2 2)   (- delta)) (<= (- limit2 2)   delta))
  (and (>= (- limit2 3)   (- delta)) (<= (- limit2 3)   delta))
  (and (>= (- limit2 4)   (- delta)) (<= (- limit2 4)   delta))
  (and (>= (- limit2 5)   (- delta)) (<= (- limit2 5)   delta))
  (and (>= (- limit2 6)   (- delta)) (<= (- limit2 6)   delta))
  (and (>= (- limit2 7)   (- delta)) (<= (- limit2 7)   delta))
  (and (>= (- limit2 8)   (- delta)) (<= (- limit2 8)   delta))
  (and (>= (- limit2 9)   (- delta)) (<= (- limit2 9)   delta))
  (and (>= (- limit2 10)  (- delta)) (<= (- limit2 10)  delta))
 )
)

;; --- limit3 ---
(assert
 (or
  (and (>= (- limit3 -10) (- delta)) (<= (- limit3 -10) delta))
  (and (>= (- limit3 -9)  (- delta)) (<= (- limit3 -9)  delta))
  (and (>= (- limit3 -8)  (- delta)) (<= (- limit3 -8)  delta))
  (and (>= (- limit3 -7)  (- delta)) (<= (- limit3 -7)  delta))
  (and (>= (- limit3 -6)  (- delta)) (<= (- limit3 -6)  delta))
  (and (>= (- limit3 -5)  (- delta)) (<= (- limit3 -5)  delta))
  (and (>= (- limit3 -4)  (- delta)) (<= (- limit3 -4)  delta))
  (and (>= (- limit3 -3)  (- delta)) (<= (- limit3 -3)  delta))
  (and (>= (- limit3 -2)  (- delta)) (<= (- limit3 -2)  delta))
  (and (>= (- limit3 -1)  (- delta)) (<= (- limit3 -1)  delta))
  (and (>= (- limit3 0)   (- delta)) (<= (- limit3 0)   delta))
  (and (>= (- limit3 1)   (- delta)) (<= (- limit3 1)   delta))
  (and (>= (- limit3 2)   (- delta)) (<= (- limit3 2)   delta))
  (and (>= (- limit3 3)   (- delta)) (<= (- limit3 3)   delta))
  (and (>= (- limit3 4)   (- delta)) (<= (- limit3 4)   delta))
  (and (>= (- limit3 5)   (- delta)) (<= (- limit3 5)   delta))
  (and (>= (- limit3 6)   (- delta)) (<= (- limit3 6)   delta))
  (and (>= (- limit3 7)   (- delta)) (<= (- limit3 7)   delta))
  (and (>= (- limit3 8)   (- delta)) (<= (- limit3 8)   delta))
  (and (>= (- limit3 9)   (- delta)) (<= (- limit3 9)   delta))
  (and (>= (- limit3 10)  (- delta)) (<= (- limit3 10)  delta))
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

;; --- d ---
(assert
 (or
  (and (>= (- d -10) (- delta)) (<= (- d -10) delta))
  (and (>= (- d -9)  (- delta)) (<= (- d -9)  delta))
  (and (>= (- d -8)  (- delta)) (<= (- d -8)  delta))
  (and (>= (- d -7)  (- delta)) (<= (- d -7)  delta))
  (and (>= (- d -6)  (- delta)) (<= (- d -6)  delta))
  (and (>= (- d -5)  (- delta)) (<= (- d -5)  delta))
  (and (>= (- d -4)  (- delta)) (<= (- d -4)  delta))
  (and (>= (- d -3)  (- delta)) (<= (- d -3)  delta))
  (and (>= (- d -2)  (- delta)) (<= (- d -2)  delta))
  (and (>= (- d -1)  (- delta)) (<= (- d -1)  delta))
  (and (>= (- d 0)   (- delta)) (<= (- d 0)   delta))
  (and (>= (- d 1)   (- delta)) (<= (- d 1)   delta))
  (and (>= (- d 2)   (- delta)) (<= (- d 2)   delta))
  (and (>= (- d 3)   (- delta)) (<= (- d 3)   delta))
  (and (>= (- d 4)   (- delta)) (<= (- d 4)   delta))
  (and (>= (- d 5)   (- delta)) (<= (- d 5)   delta))
  (and (>= (- d 6)   (- delta)) (<= (- d 6)   delta))
  (and (>= (- d 7)   (- delta)) (<= (- d 7)   delta))
  (and (>= (- d 8)   (- delta)) (<= (- d 8)   delta))
  (and (>= (- d 9)   (- delta)) (<= (- d 9)   delta))
  (and (>= (- d 10)  (- delta)) (<= (- d 10)  delta))
 )
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 3) The equality  a + 17b + 295c + 5124d == total
;;    => -delta2 <= [a + 17b + 295c + 5124d - total] <= delta2
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(assert (<= (- (+ a (* 17 b) (* 295 c) (* 5124 d)) total) delta2))
(assert (>= (- (+ a (* 17 b) (* 295 c) (* 5124 d)) total) (- delta2)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4) Inequalities from Scala code:
;;    0 <= a <= limit1
;;    0 <= b <= limit2
;;    0 <= c <= limit3
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; 0 <= a
(assert (>= a 0))
;; a <= limit1
(assert (<= a limit1))

;; 0 <= b
(assert (>= b 0))
;; b <= limit2
(assert (<= b limit2))

;; 0 <= c
(assert (>= c 0))
;; c <= limit3
(assert (<= c limit3))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 5) Finally, check satisfiability & get a model
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(check-sat)
(get-model)
