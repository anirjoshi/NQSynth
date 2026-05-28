; benchmark generated from python API
(set-info :status unknown)
(declare-fun r2 () Real)
(declare-fun y () Real)
(declare-fun x () Real)
(declare-fun r1 () Real)
(assert
 (let ((?x20 (+ (+ 0.0 (* (* (* (* 1.0 x) x) x) x)) (* (* (* (* 1.0 y) y) y) y))))
 (let ((?x83 (- 4.0)))
 (let ((?x67 (* ?x83 y)))
 (let ((?x84 (* ?x83 x)))
 (let ((?x88 (+ (+ (+ ?x20 (* (* ?x84 x) x)) (* (* ?x67 y) y)) (* (* 6.0 x) x))))
 (let ((?x91 (+ (+ (+ (+ (+ ?x88 ?x84) (* (* 6.0 y) y)) ?x67) 2.0) (* (- 1.0) r1))))
 (and (and (> 0.0 ?x91) (> 0.0 (+ ?x20 (* (- 1.0) r2))))))))))))
(check-sat)

