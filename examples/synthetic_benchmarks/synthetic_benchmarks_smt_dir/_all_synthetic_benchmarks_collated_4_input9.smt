; benchmark generated from python API
(set-info :status unknown)
(declare-fun r2 () Real)
(declare-fun x () Real)
(declare-fun y () Real)
(declare-fun r1 () Real)
(assert
 (let ((?x50 (+ (+ (+ 0.0 (* (* 1.0 y) y)) (* (* 1.0 x) x)) (* (- 1.0) r2))))
 (let ((?x18 (+ (+ 0.0 (* (* (* 1.0 y) y) r1)) (* (* 4.0 x) x))))
 (and (and (> 0.0 (+ ?x18 (* (- 1.0) r1))) (> 0.0 ?x50))))))
(check-sat)

