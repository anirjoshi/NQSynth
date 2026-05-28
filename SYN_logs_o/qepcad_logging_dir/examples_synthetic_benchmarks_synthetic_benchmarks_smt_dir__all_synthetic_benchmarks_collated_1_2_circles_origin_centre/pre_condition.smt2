; benchmark generated from python API
(set-info :status unknown)
(declare-fun r1 () Real)
(declare-fun r2 () Real)
(assert
 (and (< 0.0 (+ r1 r2)) (> 0.0 (+ r1 r2)) (< 0.0 (+ r2 (* (- 1.0) r1))) (> 0.0 (+ r2 (* (- 1.0) r1)))))
(check-sat)


