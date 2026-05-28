; benchmark generated from python API
(set-info :status unknown)
(declare-fun r () Real)
(declare-fun y () Real)
(declare-fun x () Real)
(assert
 (let ((?x41 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* 1.0 y) y)) (* (* (- 1.0) r) r))))
 (and (and (> 0.0 ?x41)))))
(check-sat)

