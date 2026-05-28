; benchmark generated from python API
(set-info :status unknown)
(declare-fun r2 () Real)
(declare-fun y () Real)
(declare-fun x () Real)
(assert
 (let ((?x56 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* 1.0 y) y)) (* (- 1.0) r2))))
 (let ((?x73 (* (- 4.0) y)))
 (let ((?x80 (+ (+ 0.0 (* (* (* (* 1.0 x) x) x) x)) (* (* ?x73 y) y))))
 (let (($x66 (and (> 0.0 (+ (+ (+ ?x80 (* (* 6.0 x) x)) ?x73) 2.0)) (> 0.0 ?x56))))
 (and $x66))))))
(check-sat)

