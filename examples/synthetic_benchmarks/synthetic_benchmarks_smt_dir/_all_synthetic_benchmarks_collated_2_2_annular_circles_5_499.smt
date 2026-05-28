; benchmark generated from python API
(set-info :status unknown)
(declare-fun y () Real)
(declare-fun x () Real)
(assert
 (let ((?x51 (+ (+ 0.0 (* (* (- 1.0) x) x)) (* (* (- 1.0) y) y))))
 (let ((?x44 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* 1.0 y) y)) (- 5.0))))
 (and (and (>= 0.0 ?x44) (>= 0.0 (+ ?x51 (/ 499.0 100.0))))))))
(check-sat)

