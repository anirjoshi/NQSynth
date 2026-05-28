(set-logic NRA)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 1) Declare variables as Real
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(declare-fun weight () Real)
(declare-fun w1 () Real)
(declare-fun w2 () Real)
(declare-fun w3 () Real)
(declare-fun w4 () Real)
(declare-fun delta () Real)
(declare-fun delta2 () Real)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 2) Integer-likeness constraints for weight, w1, w2, w3, w4
;;    Each must be within +/- delta of an integer in [-10..10].
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; --- weight ---
(assert
 (or
  (and (>= (- weight -10) (- delta)) (<= (- weight -10) delta))
  (and (>= (- weight -9)  (- delta)) (<= (- weight -9)  delta))
  (and (>= (- weight -8)  (- delta)) (<= (- weight -8)  delta))
  (and (>= (- weight -7)  (- delta)) (<= (- weight -7)  delta))
  (and (>= (- weight -6)  (- delta)) (<= (- weight -6)  delta))
  (and (>= (- weight -5)  (- delta)) (<= (- weight -5)  delta))
  (and (>= (- weight -4)  (- delta)) (<= (- weight -4)  delta))
  (and (>= (- weight -3)  (- delta)) (<= (- weight -3)  delta))
  (and (>= (- weight -2)  (- delta)) (<= (- weight -2)  delta))
  (and (>= (- weight -1)  (- delta)) (<= (- weight -1)  delta))
  (and (>= (- weight 0)   (- delta)) (<= (- weight 0)   delta))
  (and (>= (- weight 1)   (- delta)) (<= (- weight 1)   delta))
  (and (>= (- weight 2)   (- delta)) (<= (- weight 2)   delta))
  (and (>= (- weight 3)   (- delta)) (<= (- weight 3)   delta))
  (and (>= (- weight 4)   (- delta)) (<= (- weight 4)   delta))
  (and (>= (- weight 5)   (- delta)) (<= (- weight 5)   delta))
  (and (>= (- weight 6)   (- delta)) (<= (- weight 6)   delta))
  (and (>= (- weight 7)   (- delta)) (<= (- weight 7)   delta))
  (and (>= (- weight 8)   (- delta)) (<= (- weight 8)   delta))
  (and (>= (- weight 9)   (- delta)) (<= (- weight 9)   delta))
  (and (>= (- weight 10)  (- delta)) (<= (- weight 10)  delta))
 )
)

;; --- w1 ---
(assert
 (or
  (and (>= (- w1 -10) (- delta)) (<= (- w1 -10) delta))
  (and (>= (- w1 -9)  (- delta)) (<= (- w1 -9)  delta))
  (and (>= (- w1 -8)  (- delta)) (<= (- w1 -8)  delta))
  (and (>= (- w1 -7)  (- delta)) (<= (- w1 -7)  delta))
  (and (>= (- w1 -6)  (- delta)) (<= (- w1 -6)  delta))
  (and (>= (- w1 -5)  (- delta)) (<= (- w1 -5)  delta))
  (and (>= (- w1 -4)  (- delta)) (<= (- w1 -4)  delta))
  (and (>= (- w1 -3)  (- delta)) (<= (- w1 -3)  delta))
  (and (>= (- w1 -2)  (- delta)) (<= (- w1 -2)  delta))
  (and (>= (- w1 -1)  (- delta)) (<= (- w1 -1)  delta))
  (and (>= (- w1 0)   (- delta)) (<= (- w1 0)   delta))
  (and (>= (- w1 1)   (- delta)) (<= (- w1 1)   delta))
  (and (>= (- w1 2)   (- delta)) (<= (- w1 2)   delta))
  (and (>= (- w1 3)   (- delta)) (<= (- w1 3)   delta))
  (and (>= (- w1 4)   (- delta)) (<= (- w1 4)   delta))
  (and (>= (- w1 5)   (- delta)) (<= (- w1 5)   delta))
  (and (>= (- w1 6)   (- delta)) (<= (- w1 6)   delta))
  (and (>= (- w1 7)   (- delta)) (<= (- w1 7)   delta))
  (and (>= (- w1 8)   (- delta)) (<= (- w1 8)   delta))
  (and (>= (- w1 9)   (- delta)) (<= (- w1 9)   delta))
  (and (>= (- w1 10)  (- delta)) (<= (- w1 10)  delta))
 )
)

;; --- w2 ---
(assert
 (or
  (and (>= (- w2 -10) (- delta)) (<= (- w2 -10) delta))
  (and (>= (- w2 -9)  (- delta)) (<= (- w2 -9)  delta))
  (and (>= (- w2 -8)  (- delta)) (<= (- w2 -8)  delta))
  (and (>= (- w2 -7)  (- delta)) (<= (- w2 -7)  delta))
  (and (>= (- w2 -6)  (- delta)) (<= (- w2 -6)  delta))
  (and (>= (- w2 -5)  (- delta)) (<= (- w2 -5)  delta))
  (and (>= (- w2 -4)  (- delta)) (<= (- w2 -4)  delta))
  (and (>= (- w2 -3)  (- delta)) (<= (- w2 -3)  delta))
  (and (>= (- w2 -2)  (- delta)) (<= (- w2 -2)  delta))
  (and (>= (- w2 -1)  (- delta)) (<= (- w2 -1)  delta))
  (and (>= (- w2 0)   (- delta)) (<= (- w2 0)   delta))
  (and (>= (- w2 1)   (- delta)) (<= (- w2 1)   delta))
  (and (>= (- w2 2)   (- delta)) (<= (- w2 2)   delta))
  (and (>= (- w2 3)   (- delta)) (<= (- w2 3)   delta))
  (and (>= (- w2 4)   (- delta)) (<= (- w2 4)   delta))
  (and (>= (- w2 5)   (- delta)) (<= (- w2 5)   delta))
  (and (>= (- w2 6)   (- delta)) (<= (- w2 6)   delta))
  (and (>= (- w2 7)   (- delta)) (<= (- w2 7)   delta))
  (and (>= (- w2 8)   (- delta)) (<= (- w2 8)   delta))
  (and (>= (- w2 9)   (- delta)) (<= (- w2 9)   delta))
  (and (>= (- w2 10)  (- delta)) (<= (- w2 10)  delta))
 )
)

;; --- w3 ---
(assert
 (or
  (and (>= (- w3 -10) (- delta)) (<= (- w3 -10) delta))
  (and (>= (- w3 -9)  (- delta)) (<= (- w3 -9)  delta))
  (and (>= (- w3 -8)  (- delta)) (<= (- w3 -8)  delta))
  (and (>= (- w3 -7)  (- delta)) (<= (- w3 -7)  delta))
  (and (>= (- w3 -6)  (- delta)) (<= (- w3 -6)  delta))
  (and (>= (- w3 -5)  (- delta)) (<= (- w3 -5)  delta))
  (and (>= (- w3 -4)  (- delta)) (<= (- w3 -4)  delta))
  (and (>= (- w3 -3)  (- delta)) (<= (- w3 -3)  delta))
  (and (>= (- w3 -2)  (- delta)) (<= (- w3 -2)  delta))
  (and (>= (- w3 -1)  (- delta)) (<= (- w3 -1)  delta))
  (and (>= (- w3 0)   (- delta)) (<= (- w3 0)   delta))
  (and (>= (- w3 1)   (- delta)) (<= (- w3 1)   delta))
  (and (>= (- w3 2)   (- delta)) (<= (- w3 2)   delta))
  (and (>= (- w3 3)   (- delta)) (<= (- w3 3)   delta))
  (and (>= (- w3 4)   (- delta)) (<= (- w3 4)   delta))
  (and (>= (- w3 5)   (- delta)) (<= (- w3 5)   delta))
  (and (>= (- w3 6)   (- delta)) (<= (- w3 6)   delta))
  (and (>= (- w3 7)   (- delta)) (<= (- w3 7)   delta))
  (and (>= (- w3 8)   (- delta)) (<= (- w3 8)   delta))
  (and (>= (- w3 9)   (- delta)) (<= (- w3 9)   delta))
  (and (>= (- w3 10)  (- delta)) (<= (- w3 10)  delta))
 )
)

;; --- w4 ---
(assert
 (or
  (and (>= (- w4 -10) (- delta)) (<= (- w4 -10) delta))
  (and (>= (- w4 -9)  (- delta)) (<= (- w4 -9)  delta))
  (and (>= (- w4 -8)  (- delta)) (<= (- w4 -8)  delta))
  (and (>= (- w4 -7)  (- delta)) (<= (- w4 -7)  delta))
  (and (>= (- w4 -6)  (- delta)) (<= (- w4 -6)  delta))
  (and (>= (- w4 -5)  (- delta)) (<= (- w4 -5)  delta))
  (and (>= (- w4 -4)  (- delta)) (<= (- w4 -4)  delta))
  (and (>= (- w4 -3)  (- delta)) (<= (- w4 -3)  delta))
  (and (>= (- w4 -2)  (- delta)) (<= (- w4 -2)  delta))
  (and (>= (- w4 -1)  (- delta)) (<= (- w4 -1)  delta))
  (and (>= (- w4 0)   (- delta)) (<= (- w4 0)   delta))
  (and (>= (- w4 1)   (- delta)) (<= (- w4 1)   delta))
  (and (>= (- w4 2)   (- delta)) (<= (- w4 2)   delta))
  (and (>= (- w4 3)   (- delta)) (<= (- w4 3)   delta))
  (and (>= (- w4 4)   (- delta)) (<= (- w4 4)   delta))
  (and (>= (- w4 5)   (- delta)) (<= (- w4 5)   delta))
  (and (>= (- w4 6)   (- delta)) (<= (- w4 6)   delta))
  (and (>= (- w4 7)   (- delta)) (<= (- w4 7)   delta))
  (and (>= (- w4 8)   (- delta)) (<= (- w4 8)   delta))
  (and (>= (- w4 9)   (- delta)) (<= (- w4 9)   delta))
  (and (>= (- w4 10)  (- delta)) (<= (- w4 10)  delta))
 )
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 3) Core Condition from Scala code:
;;
;;    !(0 <= weight && weight <= 39) || (
;;         w1 + 3*w2 + 9*w3 + 27*w4 == weight
;;      && -1 <= w1 <= 1
;;      && -1 <= w2 <= 1
;;      && -1 <= w3 <= 1
;;      && -1 <= w4 <= 1
;;    )
;;
;;  => (or  (or (< weight 0) (> weight 39))
;;           (and
;;              -delta2 <= [w1+3*w2+9*w3+27*w4 - weight] <= delta2
;;              -1 <= w1 <= 1, etc. ))
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(assert
 (or
  ;; Part 1: weight < 0 or weight > 39
  (or (< weight 0) (> weight 39))

  ;; Part 2: if weight in [0..39], then the 'equalities' must hold
  (and
    ;; approximate equality for w1+3*w2+9*w3+27*w4 == weight
    (<= (- (+ w1 (* 3 w2) (* 9 w3) (* 27 w4)) weight) delta2)
    (>= (- (+ w1 (* 3 w2) (* 9 w3) (* 27 w4)) weight) (- delta2))

    ;; -1 <= w1 <= 1
    (>= w1 -1)
    (<= w1 1)

    ;; -1 <= w2 <= 1
    (>= w2 -1)
    (<= w2 1)

    ;; -1 <= w3 <= 1
    (>= w3 -1)
    (<= w3 1)

    ;; -1 <= w4 <= 1
    (>= w4 -1)
    (<= w4 1)
  )
 )
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4) Check satisfiability & get a model
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(check-sat)
(get-model)
