(set-logic NRA)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; List of variables appearing in this SMT file:
;   x, y, g, lower, upper, delta, delta2
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(declare-fun x () Real)
(declare-fun y () Real)
(declare-fun g () Real)
(declare-fun lower () Real)
(declare-fun upper () Real)
(declare-fun delta () Real)
(declare-fun delta2 () Real)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Force x to be within delta of some integer in [-10..10].
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
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

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Force y to be within delta of some integer in [-10..10].
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
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

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Force g to be within delta of some integer in [-10..10].
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(assert
  (or
    (and (>= (- g -10) (- delta)) (<= (- g -10) delta))
    (and (>= (- g -9)  (- delta)) (<= (- g -9)  delta))
    (and (>= (- g -8)  (- delta)) (<= (- g -8)  delta))
    (and (>= (- g -7)  (- delta)) (<= (- g -7)  delta))
    (and (>= (- g -6)  (- delta)) (<= (- g -6)  delta))
    (and (>= (- g -5)  (- delta)) (<= (- g -5)  delta))
    (and (>= (- g -4)  (- delta)) (<= (- g -4)  delta))
    (and (>= (- g -3)  (- delta)) (<= (- g -3)  delta))
    (and (>= (- g -2)  (- delta)) (<= (- g -2)  delta))
    (and (>= (- g -1)  (- delta)) (<= (- g -1)  delta))
    (and (>= (- g 0)   (- delta)) (<= (- g 0)   delta))
    (and (>= (- g 1)   (- delta)) (<= (- g 1)   delta))
    (and (>= (- g 2)   (- delta)) (<= (- g 2)   delta))
    (and (>= (- g 3)   (- delta)) (<= (- g 3)   delta))
    (and (>= (- g 4)   (- delta)) (<= (- g 4)   delta))
    (and (>= (- g 5)   (- delta)) (<= (- g 5)   delta))
    (and (>= (- g 6)   (- delta)) (<= (- g 6)   delta))
    (and (>= (- g 7)   (- delta)) (<= (- g 7)   delta))
    (and (>= (- g 8)   (- delta)) (<= (- g 8)   delta))
    (and (>= (- g 9)   (- delta)) (<= (- g 9)   delta))
    (and (>= (- g 10)  (- delta)) (<= (- g 10)  delta))
  )
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Force lower to be within delta of some integer in [-10..10].
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(assert
  (or
    (and (>= (- lower -10) (- delta)) (<= (- lower -10) delta))
    (and (>= (- lower -9)  (- delta)) (<= (- lower -9)  delta))
    (and (>= (- lower -8)  (- delta)) (<= (- lower -8)  delta))
    (and (>= (- lower -7)  (- delta)) (<= (- lower -7)  delta))
    (and (>= (- lower -6)  (- delta)) (<= (- lower -6)  delta))
    (and (>= (- lower -5)  (- delta)) (<= (- lower -5)  delta))
    (and (>= (- lower -4)  (- delta)) (<= (- lower -4)  delta))
    (and (>= (- lower -3)  (- delta)) (<= (- lower -3)  delta))
    (and (>= (- lower -2)  (- delta)) (<= (- lower -2)  delta))
    (and (>= (- lower -1)  (- delta)) (<= (- lower -1)  delta))
    (and (>= (- lower 0)   (- delta)) (<= (- lower 0)   delta))
    (and (>= (- lower 1)   (- delta)) (<= (- lower 1)   delta))
    (and (>= (- lower 2)   (- delta)) (<= (- lower 2)   delta))
    (and (>= (- lower 3)   (- delta)) (<= (- lower 3)   delta))
    (and (>= (- lower 4)   (- delta)) (<= (- lower 4)   delta))
    (and (>= (- lower 5)   (- delta)) (<= (- lower 5)   delta))
    (and (>= (- lower 6)   (- delta)) (<= (- lower 6)   delta))
    (and (>= (- lower 7)   (- delta)) (<= (- lower 7)   delta))
    (and (>= (- lower 8)   (- delta)) (<= (- lower 8)   delta))
    (and (>= (- lower 9)   (- delta)) (<= (- lower 9)   delta))
    (and (>= (- lower 10)  (- delta)) (<= (- lower 10)  delta))
  )
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Force upper to be within delta of some integer in [-10..10].
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(assert
  (or
    (and (>= (- upper -10) (- delta)) (<= (- upper -10) delta))
    (and (>= (- upper -9)  (- delta)) (<= (- upper -9)  delta))
    (and (>= (- upper -8)  (- delta)) (<= (- upper -8)  delta))
    (and (>= (- upper -7)  (- delta)) (<= (- upper -7)  delta))
    (and (>= (- upper -6)  (- delta)) (<= (- upper -6)  delta))
    (and (>= (- upper -5)  (- delta)) (<= (- upper -5)  delta))
    (and (>= (- upper -4)  (- delta)) (<= (- upper -4)  delta))
    (and (>= (- upper -3)  (- delta)) (<= (- upper -3)  delta))
    (and (>= (- upper -2)  (- delta)) (<= (- upper -2)  delta))
    (and (>= (- upper -1)  (- delta)) (<= (- upper -1)  delta))
    (and (>= (- upper 0)   (- delta)) (<= (- upper 0)   delta))
    (and (>= (- upper 1)   (- delta)) (<= (- upper 1)   delta))
    (and (>= (- upper 2)   (- delta)) (<= (- upper 2)   delta))
    (and (>= (- upper 3)   (- delta)) (<= (- upper 3)   delta))
    (and (>= (- upper 4)   (- delta)) (<= (- upper 4)   delta))
    (and (>= (- upper 5)   (- delta)) (<= (- upper 5)   delta))
    (and (>= (- upper 6)   (- delta)) (<= (- upper 6)   delta))
    (and (>= (- upper 7)   (- delta)) (<= (- upper 7)   delta))
    (and (>= (- upper 8)   (- delta)) (<= (- upper 8)   delta))
    (and (>= (- upper 9)   (- delta)) (<= (- upper 9)   delta))
    (and (>= (- upper 10)  (- delta)) (<= (- upper 10)  delta))
  )
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Original inequalities from Scala code:
;   x > 0
;   y > 0
;   0 <= lower <= 100
;   0 <= upper <= 100
;   lower <= g <= upper
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(assert (> x 0))
(assert (> y 0))

(assert (>= lower 0))
(assert (<= lower 100))
(assert (>= upper 0))
(assert (<= upper 100))

(assert (<= lower g))
(assert (>= upper g))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Equality constraint: 18*g == 3*x + 2*y
; Converted to -delta2 <= 18*g - (3*x + 2*y) <= delta2
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(assert (>= (- (* 18 g) (+ (* 3 x) (* 2 y))) (- delta2)))
(assert (<= (- (* 18 g) (+ (* 3 x) (* 2 y))) delta2))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Finally, ask for a model
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(check-sat)
(get-model)
