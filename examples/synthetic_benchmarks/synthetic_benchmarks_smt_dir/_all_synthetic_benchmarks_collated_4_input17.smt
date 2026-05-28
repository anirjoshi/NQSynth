; benchmark generated from python API
(set-info :status unknown)
(declare-fun b () Real)
(declare-fun y () Real)
(declare-fun x () Real)
(declare-fun a () Real)
(assert
 (let ((?x45 (- 1.0)))
 (let ((?x64 (* ?x45 y)))
 (let ((?x11 (* 1.0 x)))
 (let ((?x77 (+ (+ (+ 0.0 (* (* (* ?x45 x) x) x)) (* (* ?x64 y) y)) (* (* (* (* ?x45 x) x) y) y))))
 (let ((?x15 (* 1.0 y)))
 (let ((?x21 (+ (+ (+ 0.0 (* (* ?x11 x) x)) (* (* ?x15 y) y)) (* (* (* ?x11 x) y) y))))
 (let (($x78 (and (> 0.0 (+ (+ (+ ?x21 ?x11) ?x15) (* 1.0 a))) (> 0.0 (+ (+ (+ ?x77 ?x11) ?x64) (* ?x45 b))))))
 (and $x78)))))))))
(check-sat)

