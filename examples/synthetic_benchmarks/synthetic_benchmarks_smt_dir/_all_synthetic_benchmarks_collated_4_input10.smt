; benchmark generated from python API
(set-info :status unknown)
(declare-fun r () Real)
(declare-fun x () Real)
(declare-fun y () Real)
(assert
 (let ((?x39 (+ (+ (+ 0.0 (* (* 1.0 y) y)) (* (* 1.0 x) x)) (* (- 1.0) r))))
 (let (($x42 (>= 0.0 ?x39)))
 (and (and $x42 $x42)))))
(check-sat)

