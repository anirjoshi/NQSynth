; benchmark generated from python API
(set-info :status unknown)
(declare-fun c () Real)
(declare-fun y () Real)
(declare-fun x () Real)
(assert
 (let ((?x46 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* 1.0 y) y)) (* (* (- 1.0) c) c))))
 (let ((?x52 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (- 1.0) y)) (* 1.0 c))))
 (and (and (>= 0.0 ?x52) (>= 0.0 ?x46))))))
(check-sat)

