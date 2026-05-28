; benchmark generated from python API
(set-info :status unknown)
(declare-fun x () Real)
(declare-fun r2 () Real)
(declare-fun y () Real)
(declare-fun r1 () Real)
(assert
 (let ((?x25 (+ (+ (+ 0.0 (* 1.0 y)) (* (* 1.0 x) y)) (* 1.0 r2))))
 (let ((?x54 (+ (+ (+ 0.0 (* 1.0 x)) (* (* (- 1.0) y) y)) (* (- 1.0) r1))))
 (let (($x57 (and (> 0.0 ?x54) (> 0.0 ?x25) (> 0.0 (+ 0.0 (* (- 1.0) x))))))
 (and $x57)))))
(check-sat)

