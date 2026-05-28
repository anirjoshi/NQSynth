; benchmark generated from python API
(set-info :status unknown)
(declare-fun x () Real)
(declare-fun d1 () Real)
(declare-fun d2 () Real)
(assert
 (and (< 0.0 (+ d1 d2)) (< 0.0 (+ d1 x))))
(check-sat)


