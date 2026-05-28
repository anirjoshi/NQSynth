; benchmark generated from python API
(set-info :status unknown)
(declare-fun y () Real)
(declare-fun x () Real)
(declare-fun r () Real)
(assert
 (let ((?x53 (+ (+ 0.0 (* (* (- 1.0) x) x)) (* (* (- 1.0) y) y))))
 (let ((?x55 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* 1.0 y) y)) (* (* (- 1.0) r) r))))
 (and (and (> 0.0 ?x55) (> 0.0 (+ ?x53 25.0)))))))
(check-sat)

