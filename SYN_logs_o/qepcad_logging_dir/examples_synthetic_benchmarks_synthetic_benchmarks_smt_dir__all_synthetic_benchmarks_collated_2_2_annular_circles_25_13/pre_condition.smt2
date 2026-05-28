; benchmark generated from python API
(set-info :status unknown)
(declare-fun y () Real)
(assert
 (and (<= 0.0 (+ 5.0 y)) (>= 0.0 (+ (- 5.0) y))))
(check-sat)


