; benchmark generated from python API
(set-info :status unknown)
(declare-fun y () Real)
(declare-fun x () Real)
(assert
 (let ((?x49 (+ (+ 0.0 (* (* (- 1.0) x) x)) (* (* (- 1.0) y) y))))
 (let ((?x45 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* 1.0 y) y)) (- 25.0))))
 (and (and (>= 0.0 ?x45) (>= 0.0 (+ ?x49 1.0)))))))
(check-sat)

