; benchmark generated from python API
(set-info :status unknown)
(declare-fun c () Real)
(declare-fun z () Real)
(declare-fun y () Real)
(declare-fun b () Real)
(declare-fun x () Real)
(declare-fun a () Real)
(assert
 (let ((?x27 (* (* (* 1.0 z) z) z)))
 (let ((?x58 (+ (+ (+ 0.0 (* (* (* 1.0 y) y) y)) ?x27) (* (- 1.0) c))))
 (let ((?x67 (+ (+ (+ 0.0 (* (* (* 1.0 x) x) x)) ?x27) (* (- 1.0) b))))
 (let ((?x19 (* (* (* 1.0 y) y) y)))
 (let ((?x16 (+ 0.0 (* (* (* 1.0 x) x) x))))
 (let (($x66 (and (> 0.0 (+ (+ ?x16 ?x19) (* (- 1.0) a))) (> 0.0 ?x67) (> 0.0 ?x58))))
 (and $x66))))))))
(check-sat)

