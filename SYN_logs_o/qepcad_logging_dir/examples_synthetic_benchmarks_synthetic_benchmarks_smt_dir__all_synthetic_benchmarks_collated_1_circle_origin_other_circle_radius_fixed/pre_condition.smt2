; benchmark generated from python API
(set-info :status unknown)
(declare-fun r () Real)
(assert
 (and (and (distinct 0.0 (+ (- 5.0) r)) true) (and (distinct 0.0 (+ 5.0 r)) true) (or (< 0.0 (+ (- 5.0) r)) (> 0.0 (+ 5.0 r)))))
(check-sat)


