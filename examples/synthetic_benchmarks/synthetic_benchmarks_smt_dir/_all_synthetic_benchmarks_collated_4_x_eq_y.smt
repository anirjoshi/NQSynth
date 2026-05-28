; benchmark generated from python API
(set-info :status unknown)
(declare-fun y () Real)
(declare-fun x () Real)
(assert
 (let (($x23 (and (>= 0.0 (+ (+ 0.0 (* 1.0 x)) (* (- 1.0) y))) (>= 0.0 (+ (+ 0.0 (* (- 1.0) x)) (* 1.0 y))))))
 (and $x23)))
(check-sat)

