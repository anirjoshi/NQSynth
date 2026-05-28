; benchmark generated from python API
(set-info :status unknown)
(declare-fun delta () Real)
(declare-fun y () Real)
(declare-fun x () Real)
(assert
 (let ((?x18 (* (- 1.0) delta)))
 (let ((?x27 (+ (+ (+ 0.0 (* (* (- 1.0) x) x)) (* (* (- 1.0) y) y)) 1.0)))
 (let ((?x17 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* 1.0 y) y)) (- 1.0))))
 (and (>= 0.0 (+ ?x17 ?x18)) (>= 0.0 (+ ?x27 ?x18)))))))
(check-sat)

