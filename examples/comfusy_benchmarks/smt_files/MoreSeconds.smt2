(set-logic NRA)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 1) Declare variables as Real
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(declare-fun secnum () Real)
(declare-fun hours () Real)
(declare-fun minutes () Real)
(declare-fun seconds () Real)
(declare-fun delta () Real)
(declare-fun delta2 () Real)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 2) Integer-likeness constraints for secnum, hours, minutes,
;;    seconds. Each must be within +/- delta of an integer
;;    in [-10..10].
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; --- secnum ---
(assert
 (or
  (and (>= (- secnum -10) (- delta)) (<= (- secnum -10) delta))
  (and (>= (- secnum -9)  (- delta)) (<= (- secnum -9)  delta))
  (and (>= (- secnum -8)  (- delta)) (<= (- secnum -8)  delta))
  (and (>= (- secnum -7)  (- delta)) (<= (- secnum -7)  delta))
  (and (>= (- secnum -6)  (- delta)) (<= (- secnum -6)  delta))
  (and (>= (- secnum -5)  (- delta)) (<= (- secnum -5)  delta))
  (and (>= (- secnum -4)  (- delta)) (<= (- secnum -4)  delta))
  (and (>= (- secnum -3)  (- delta)) (<= (- secnum -3)  delta))
  (and (>= (- secnum -2)  (- delta)) (<= (- secnum -2)  delta))
  (and (>= (- secnum -1)  (- delta)) (<= (- secnum -1)  delta))
  (and (>= (- secnum 0)   (- delta)) (<= (- secnum 0)   delta))
  (and (>= (- secnum 1)   (- delta)) (<= (- secnum 1)   delta))
  (and (>= (- secnum 2)   (- delta)) (<= (- secnum 2)   delta))
  (and (>= (- secnum 3)   (- delta)) (<= (- secnum 3)   delta))
  (and (>= (- secnum 4)   (- delta)) (<= (- secnum 4)   delta))
  (and (>= (- secnum 5)   (- delta)) (<= (- secnum 5)   delta))
  (and (>= (- secnum 6)   (- delta)) (<= (- secnum 6)   delta))
  (and (>= (- secnum 7)   (- delta)) (<= (- secnum 7)   delta))
  (and (>= (- secnum 8)   (- delta)) (<= (- secnum 8)   delta))
  (and (>= (- secnum 9)   (- delta)) (<= (- secnum 9)   delta))
  (and (>= (- secnum 10)  (- delta)) (<= (- secnum 10)  delta))
 )
)

;; --- hours ---
(assert
 (or
  (and (>= (- hours -10) (- delta)) (<= (- hours -10) delta))
  (and (>= (- hours -9)  (- delta)) (<= (- hours -9)  delta))
  (and (>= (- hours -8)  (- delta)) (<= (- hours -8)  delta))
  (and (>= (- hours -7)  (- delta)) (<= (- hours -7)  delta))
  (and (>= (- hours -6)  (- delta)) (<= (- hours -6)  delta))
  (and (>= (- hours -5)  (- delta)) (<= (- hours -5)  delta))
  (and (>= (- hours -4)  (- delta)) (<= (- hours -4)  delta))
  (and (>= (- hours -3)  (- delta)) (<= (- hours -3)  delta))
  (and (>= (- hours -2)  (- delta)) (<= (- hours -2)  delta))
  (and (>= (- hours -1)  (- delta)) (<= (- hours -1)  delta))
  (and (>= (- hours 0)   (- delta)) (<= (- hours 0)   delta))
  (and (>= (- hours 1)   (- delta)) (<= (- hours 1)   delta))
  (and (>= (- hours 2)   (- delta)) (<= (- hours 2)   delta))
  (and (>= (- hours 3)   (- delta)) (<= (- hours 3)   delta))
  (and (>= (- hours 4)   (- delta)) (<= (- hours 4)   delta))
  (and (>= (- hours 5)   (- delta)) (<= (- hours 5)   delta))
  (and (>= (- hours 6)   (- delta)) (<= (- hours 6)   delta))
  (and (>= (- hours 7)   (- delta)) (<= (- hours 7)   delta))
  (and (>= (- hours 8)   (- delta)) (<= (- hours 8)   delta))
  (and (>= (- hours 9)   (- delta)) (<= (- hours 9)   delta))
  (and (>= (- hours 10)  (- delta)) (<= (- hours 10)  delta))
 )
)

;; --- minutes ---
(assert
 (or
  (and (>= (- minutes -10) (- delta)) (<= (- minutes -10) delta))
  (and (>= (- minutes -9)  (- delta)) (<= (- minutes -9)  delta))
  (and (>= (- minutes -8)  (- delta)) (<= (- minutes -8)  delta))
  (and (>= (- minutes -7)  (- delta)) (<= (- minutes -7)  delta))
  (and (>= (- minutes -6)  (- delta)) (<= (- minutes -6)  delta))
  (and (>= (- minutes -5)  (- delta)) (<= (- minutes -5)  delta))
  (and (>= (- minutes -4)  (- delta)) (<= (- minutes -4)  delta))
  (and (>= (- minutes -3)  (- delta)) (<= (- minutes -3)  delta))
  (and (>= (- minutes -2)  (- delta)) (<= (- minutes -2)  delta))
  (and (>= (- minutes -1)  (- delta)) (<= (- minutes -1)  delta))
  (and (>= (- minutes 0)   (- delta)) (<= (- minutes 0)   delta))
  (and (>= (- minutes 1)   (- delta)) (<= (- minutes 1)   delta))
  (and (>= (- minutes 2)   (- delta)) (<= (- minutes 2)   delta))
  (and (>= (- minutes 3)   (- delta)) (<= (- minutes 3)   delta))
  (and (>= (- minutes 4)   (- delta)) (<= (- minutes 4)   delta))
  (and (>= (- minutes 5)   (- delta)) (<= (- minutes 5)   delta))
  (and (>= (- minutes 6)   (- delta)) (<= (- minutes 6)   delta))
  (and (>= (- minutes 7)   (- delta)) (<= (- minutes 7)   delta))
  (and (>= (- minutes 8)   (- delta)) (<= (- minutes 8)   delta))
  (and (>= (- minutes 9)   (- delta)) (<= (- minutes 9)   delta))
  (and (>= (- minutes 10)  (- delta)) (<= (- minutes 10)  delta))
 )
)

;; --- seconds ---
(assert
 (or
  (and (>= (- seconds -10) (- delta)) (<= (- seconds -10) delta))
  (and (>= (- seconds -9)  (- delta)) (<= (- seconds -9)  delta))
  (and (>= (- seconds -8)  (- delta)) (<= (- seconds -8)  delta))
  (and (>= (- seconds -7)  (- delta)) (<= (- seconds -7)  delta))
  (and (>= (- seconds -6)  (- delta)) (<= (- seconds -6)  delta))
  (and (>= (- seconds -5)  (- delta)) (<= (- seconds -5)  delta))
  (and (>= (- seconds -4)  (- delta)) (<= (- seconds -4)  delta))
  (and (>= (- seconds -3)  (- delta)) (<= (- seconds -3)  delta))
  (and (>= (- seconds -2)  (- delta)) (<= (- seconds -2)  delta))
  (and (>= (- seconds -1)  (- delta)) (<= (- seconds -1)  delta))
  (and (>= (- seconds 0)   (- delta)) (<= (- seconds 0)   delta))
  (and (>= (- seconds 1)   (- delta)) (<= (- seconds 1)   delta))
  (and (>= (- seconds 2)   (- delta)) (<= (- seconds 2)   delta))
  (and (>= (- seconds 3)   (- delta)) (<= (- seconds 3)   delta))
  (and (>= (- seconds 4)   (- delta)) (<= (- seconds 4)   delta))
  (and (>= (- seconds 5)   (- delta)) (<= (- seconds 5)   delta))
  (and (>= (- seconds 6)   (- delta)) (<= (- seconds 6)   delta))
  (and (>= (- seconds 7)   (- delta)) (<= (- seconds 7)   delta))
  (and (>= (- seconds 8)   (- delta)) (<= (- seconds 8)   delta))
  (and (>= (- seconds 9)   (- delta)) (<= (- seconds 9)   delta))
  (and (>= (- seconds 10)  (- delta)) (<= (- seconds 10)  delta))
 )
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 3) Equality constraint:
;;    hours*3600 + minutes*60 + seconds == secnum
;;    => -delta2 <= (3600*hours + 60*minutes + seconds - secnum) <= delta2
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(assert (<= (- (+ (* 3600 hours) (* 60 minutes) seconds) secnum) delta2))
(assert (>= (- (+ (* 3600 hours) (* 60 minutes) seconds) secnum) (- delta2)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4) Inequalities from Scala code:
;;    0 <= minutes <= 60
;;    0 <= seconds <= 60
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; 0 <= minutes
(assert (>= minutes 0))
;; minutes <= 60
(assert (<= minutes 60))

;; 0 <= seconds
(assert (>= seconds 0))
;; seconds <= 60
(assert (<= seconds 60))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 5) Check satisfiability & get a model
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(check-sat)
(get-model)
