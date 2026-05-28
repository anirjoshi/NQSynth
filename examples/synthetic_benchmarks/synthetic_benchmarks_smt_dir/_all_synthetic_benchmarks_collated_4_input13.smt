; benchmark generated from python API
(set-info :status unknown)
(declare-fun x () Real)
(declare-fun y () Real)
(assert
 (let ((?x37 (+ (+ (+ 0.0 (* (* 1.0 y) y)) (* (* 1.0 x) x)) (- 16.0))))
 (and (and (>= 0.0 ?x37)))))
(check-sat)

