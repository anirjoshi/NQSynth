; benchmark generated from python API
(set-info :status unknown)
(declare-fun b () Real)
(declare-fun delta () Real)
(assert
 (let (($x46 (or (> 0.0 (+ 1.0 b)) (< 0.0 (+ 2.0 delta (* (- 1.0) (^ b 2.0)))))))
 (and (<= 0.0 (+ (- 3.0) delta (^ b 2.0))) (<= 0.0 (+ 3.0 delta (* (- 1.0) (^ b 2.0)))) $x46)))
(check-sat)


