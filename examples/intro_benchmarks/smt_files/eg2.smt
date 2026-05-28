; benchmark generated from python API
(set-info :status unknown)
(declare-fun y () Real)
(declare-fun x () Real)
(assert
 (let ((?x24 (+ (+ (+ 0.0 (* (* (- 1.0) x) x)) (* (* (- 1.0) y) y)) 1.0)))
 (let ((?x16 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* 1.0 y) y)) (- 1.0))))
 (and (>= 0.0 ?x16) (>= 0.0 ?x24)))))
(check-sat)

