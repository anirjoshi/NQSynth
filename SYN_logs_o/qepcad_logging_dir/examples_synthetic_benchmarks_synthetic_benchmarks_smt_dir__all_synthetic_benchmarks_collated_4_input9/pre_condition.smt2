; benchmark generated from python API
(set-info :status unknown)
(declare-fun r2 () Real)
(declare-fun r1 () Real)
(assert
 (and (< 0.0 r2) (and (distinct 0.0 r1) true) (or (< 0.0 r1) (< 0.0 (+ (- 1.0) r2)))))
(check-sat)


