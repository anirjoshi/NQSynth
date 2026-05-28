; benchmark generated from python API
(set-info :status unknown)
(declare-fun b () Real)
(declare-fun delta () Real)
(assert
 (and (<= 0.0 (+ (- 3.0) delta (^ b 3.0))) (<= 0.0 (+ 3.0 delta (* (- 1.0) (^ b 3.0))))))
(check-sat)


