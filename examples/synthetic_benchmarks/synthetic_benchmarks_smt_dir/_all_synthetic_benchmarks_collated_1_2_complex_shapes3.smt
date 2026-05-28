; benchmark generated from python API
(set-info :status unknown)
(declare-fun x () Real)
(declare-fun r () Real)
(declare-fun a () Real)
(declare-fun y () Real)
(assert
 (let (($x50 (> 0.0 (+ (+ 0.0 (* (* 1.0 x) x)) (* (- 1.0) r)))))
 (let ((?x49 (+ (+ (+ 0.0 (* (- 6.0) x)) 1.0) (* (* (* (* 1.0 y) y) y) a))))
 (let (($x63 (and (> 0.0 ?x49) $x50 (> 0.0 (+ (+ 0.0 (* (* 1.0 x) x)) (- 1.0))))))
 (and $x63)))))
(check-sat)

