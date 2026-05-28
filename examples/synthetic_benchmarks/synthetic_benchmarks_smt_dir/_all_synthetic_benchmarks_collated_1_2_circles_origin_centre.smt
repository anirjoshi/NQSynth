; benchmark generated from python API
(set-info :status unknown)
(declare-fun r2 () Real)
(declare-fun y () Real)
(declare-fun x () Real)
(declare-fun r1 () Real)
(assert
 (let ((?x67 (+ (+ 0.0 (* (* (- 1.0) x) x)) (* (* (- 1.0) y) y))))
 (let ((?x61 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* 1.0 y) y)) (* (* (- 1.0) r1) r1))))
 (and (and (> 0.0 ?x61) (> 0.0 (+ ?x67 (* (* 1.0 r2) r2))))))))
(check-sat)

