; benchmark generated from python API
(set-info :status unknown)
(declare-fun y () Real)
(declare-fun x () Real)
(assert
 (let ((?x26 (+ (+ (+ 0.0 (* (* (- 1.0) x) x)) (* (* (- 1.0) y) y)) 5.0)))
 (let ((?x16 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* 1.0 y) y)) (- 5.0))))
 (and (>= 0.0 ?x16) (>= 0.0 ?x26)))))
(check-sat)

