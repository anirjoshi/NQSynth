; benchmark generated from python API
(set-info :status unknown)
(declare-fun r2 () Real)
(declare-fun y () Real)
(declare-fun x () Real)
(declare-fun r1 () Real)
(assert
 (let ((?x102 (* (* (* (* (* (* (* (- 1.0) y) y) y) y) y) y) y)))
 (let ((?x92 (* (* (* (* (* (* (* (- 1.0) x) x) x) x) x) x) x)))
 (let ((?x82 (+ (+ 0.0 (* (* (* (* (* ?x92 x) x) x) x) x)) (* (* (* (* (* ?x102 y) y) y) y) y))))
 (let ((?x31 (* (* (* (* (* (* (* (* 1.0 y) y) y) y) y) y) y) y)))
 (let ((?x18 (* (* (* (* (* (* (* (* 1.0 x) x) x) x) x) x) x) x)))
 (let ((?x36 (+ (+ 0.0 (* (* (* (* ?x18 x) x) x) x)) (* (* (* (* ?x31 y) y) y) y))))
 (let (($x74 (and (> 0.0 (+ ?x36 (* (- 1.0) r1))) (> 0.0 (+ ?x82 (* 1.0 r2))))))
 (and $x74)))))))))
(check-sat)

