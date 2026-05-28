; benchmark generated from python API
(set-info :status unknown)
(declare-fun x () Real)
(assert
 (and (<= 0.0 (+ 4.0 x)) (>= 0.0 (+ (- 4.0) x))))
(check-sat)


