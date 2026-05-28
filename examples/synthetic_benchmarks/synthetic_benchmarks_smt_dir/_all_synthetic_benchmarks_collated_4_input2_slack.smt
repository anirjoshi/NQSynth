; benchmark generated from python API
(set-info :status unknown)
(declare-fun d2 () Real)
(declare-fun x () Real)
(declare-fun y () Real)
(declare-fun d1 () Real)
(assert
 (let ((?x54 (+ (+ (+ 0.0 (* (* (- 1.0) y) y)) (* 1.0 x)) (* (- 1.0) d2))))
 (let ((?x58 (+ (+ (+ 0.0 (* (* 1.0 y) y)) (* (- 1.0) x)) (* (- 1.0) d1))))
 (and (and (> 0.0 ?x58) (> 0.0 ?x54))))))
(check-sat)

