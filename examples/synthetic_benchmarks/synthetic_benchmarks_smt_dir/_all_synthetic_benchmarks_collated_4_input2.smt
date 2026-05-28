; benchmark generated from python API
(set-info :status unknown)
(declare-fun x () Real)
(declare-fun y () Real)
(assert
 (let (($x31 (>= 0.0 (+ (+ 0.0 (* (* (- 1.0) y) y)) (* 1.0 x)))))
 (let (($x43 (>= 0.0 (+ (+ 0.0 (* (* 1.0 y) y)) (* (- 1.0) x)))))
 (and (and $x43 $x31)))))
(check-sat)

