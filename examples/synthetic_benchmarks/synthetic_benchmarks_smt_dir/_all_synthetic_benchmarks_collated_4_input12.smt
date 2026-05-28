; benchmark generated from python API
(set-info :status unknown)
(declare-fun x () Real)
(declare-fun y () Real)
(assert
 (let ((?x32 (- 2.0)))
 (let ((?x28 (+ (+ 0.0 (* (* (* 1.0 y) y) y)) (* (* (* (* 1.0 x) x) x) x))))
 (let ((?x13 (* (* 1.0 x) x)))
 (let ((?x21 (* ?x13 x)))
 (let ((?x33 (+ (+ (+ 0.0 (* (* (* (* 1.0 y) y) y) y)) ?x21) ?x32)))
 (let (($x51 (>= 0.0 (+ (+ (+ 0.0 (* (* 1.0 y) y)) ?x13) (- 8.0)))))
 (and (and $x51 (>= 0.0 ?x33) (>= 0.0 (+ ?x28 ?x32)))))))))))
(check-sat)

