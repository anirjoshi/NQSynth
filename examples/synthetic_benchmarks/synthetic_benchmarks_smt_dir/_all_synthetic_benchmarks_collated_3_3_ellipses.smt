; benchmark generated from python API
(set-info :status unknown)
(declare-fun b () Real)
(declare-fun z () Real)
(declare-fun y () Real)
(declare-fun x () Real)
(declare-fun a () Real)
(assert
 (let ((?x70 (+ (+ 0.0 (* (* (- 1.0) x) x)) (* (* (- 1.0) y) y))))
 (let ((?x14 (+ 0.0 (* (* 1.0 x) x))))
 (let ((?x80 (+ (+ ?x14 (* (* (* 1.0 y) y) y)) (* (* (- 2.0) x) a))))
 (let ((?x81 (+ (+ (+ ?x14 (* (* 1.0 y) y)) (* (* 1.0 z) z)) (* (- 1.0) a))))
 (let (($x84 (and (> 0.0 ?x81) (> 0.0 (+ (+ ?x80 (* (- 2.0) y)) (* (- 3.0) a))) (> 0.0 (+ (+ ?x70 (* (* (- 1.0) z) z)) (* 1.0 b))))))
 (and $x84)))))))
(check-sat)

