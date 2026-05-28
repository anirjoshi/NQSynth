; benchmark generated from python API
(set-info :status unknown)
(declare-fun z () Real)
(declare-fun y () Real)
(declare-fun x () Real)
(assert
 (let ((?x65 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* (- 1.0) y) y)) (* (- 10.0) z))))
 (let ((?x59 (+ (+ (+ 0.0 (* (* 1.0 y) y)) (* (* (- 1.0) x) y)) (* 1.0 z))))
 (and (and (> 0.0 ?x59) (> 0.0 ?x65))))))
(check-sat)

