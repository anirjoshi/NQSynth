; benchmark generated from python API
(set-info :status unknown)
(declare-fun a () Real)
(declare-fun y () Real)
(declare-fun x () Real)
(declare-fun z () Real)
(assert
 (let ((?x13 (+ 0.0 (* (* 1.0 x) x))))
 (let ((?x66 (+ (+ ?x13 (* (* (* 1.0 y) y) y)) (* (* (- 2.0) x) a))))
 (let ((?x79 (+ (+ ?x13 (* (* (* 1.0 y) y) a)) (* (* (- 1.0) z) z))))
 (let (($x71 (and (> 0.0 (+ ?x79 (* 1.0 a))) (> 0.0 (+ (+ ?x66 (* (- 2.0) y)) (* (- 3.0) a))))))
 (and $x71))))))
(check-sat)

