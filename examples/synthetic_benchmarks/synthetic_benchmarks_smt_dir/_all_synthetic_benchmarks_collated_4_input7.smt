; benchmark generated from python API
(set-info :status unknown)
(declare-fun r () Real)
(declare-fun y () Real)
(declare-fun x () Real)
(declare-fun b () Real)
(declare-fun a () Real)
(assert
 (let ((?x66 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* 1.0 y) y)) (* (- 20.0) x))))
 (let ((?x62 (+ (+ (+ ?x66 (* (- 20.0) y)) (* (* (- 1.0) r) r)) 200.0)))
 (let ((?x21 (+ (+ 0.0 (* (* (* (* 1.0 x) x) a) a)) (* (* (* (* 1.0 y) y) b) b))))
 (let (($x72 (and (> 0.0 (+ ?x21 (* (* (* (* (- 1.0) a) a) b) b))) (> 0.0 ?x62))))
 (and $x72))))))
(check-sat)

