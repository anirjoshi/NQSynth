; benchmark generated from python API
(set-info :status unknown)
(declare-fun a () Real)
(declare-fun y () Real)
(declare-fun x () Real)
(declare-fun z () Real)
(assert
 (let ((?x16 (+ (+ 0.0 (* (* 1.0 x) x)) (* (* 1.0 y) y))))
 (let ((?x73 (+ (+ (+ ?x16 (* (* (- 2.0) x) a)) (* (- 2.0) y)) (* (* 1.0 a) a))))
 (let (($x69 (and (> 0.0 (+ (+ ?x16 (* (* (- 1.0) z) z)) (* 1.0 a))) (> 0.0 (+ ?x73 (- 3.0))))))
 (and $x69)))))
(check-sat)

