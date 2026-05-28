; benchmark generated from python API
(set-info :status unknown)
(declare-fun r2 () Real)
(declare-fun y () Real)
(declare-fun x () Real)
(declare-fun r1 () Real)
(assert
 (let ((?x69 (+ (+ 0.0 (* (* (* (* (- 1.0) x) x) x) x)) (* (* (* (* (- 1.0) y) y) y) y))))
 (let ((?x20 (+ (+ 0.0 (* (* (* (* 1.0 x) x) x) x)) (* (* (* (* 1.0 y) y) y) y))))
 (let (($x61 (and (> 0.0 (+ ?x20 (* (- 1.0) r1))) (> 0.0 (+ ?x69 (* 1.0 r2))))))
 (and $x61)))))
(check-sat)

