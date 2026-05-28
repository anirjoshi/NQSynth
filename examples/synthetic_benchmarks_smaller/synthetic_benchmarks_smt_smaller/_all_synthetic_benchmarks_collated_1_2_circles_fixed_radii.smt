; benchmark generated from python API
(set-info :status unknown)
(declare-fun y () Real)
(declare-fun x () Real)
(assert
 (let ((?x62 (+ (+ 0.0 (* (* (- 1.0) x) x)) (* (* (- 1.0) y) y))))
 (let ((?x53 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* 1.0 y) y)) (- 5.0))))
 (and (and (> 0.0 ?x53) (> 0.0 (+ ?x62 (/ 4999.0 1000.0))))))))
(check-sat)

