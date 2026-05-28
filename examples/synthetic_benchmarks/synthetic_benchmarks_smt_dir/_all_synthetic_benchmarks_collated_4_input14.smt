; benchmark generated from python API
(set-info :status unknown)
(declare-fun x () Real)
(declare-fun z () Real)
(declare-fun y () Real)
(assert
 (let ((?x18 (+ (+ (+ 0.0 (* (* 1.0 y) y)) (* (* 1.0 z) z)) (* (* 1.0 x) x))))
 (and (and (>= 0.0 (+ ?x18 (- 16.0)))))))
(check-sat)

