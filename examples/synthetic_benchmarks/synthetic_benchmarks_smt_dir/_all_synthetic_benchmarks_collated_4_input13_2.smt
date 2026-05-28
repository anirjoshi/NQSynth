; benchmark generated from python API
(set-info :status unknown)
(declare-fun b () Real)
(declare-fun a () Real)
(declare-fun x () Real)
(declare-fun y () Real)
(assert
 (let ((?x66 (- 1.0)))
 (let ((?x16 (+ (+ 0.0 (* (* 1.0 y) y)) (* (* 1.0 x) x))))
 (let ((?x64 (+ (+ ?x16 (* (* (- 2.0) y) a)) (* (* (- 2.0) x) b))))
 (let ((?x72 (+ (+ (+ ?x64 (* (* 1.0 a) a)) (* (* 1.0 b) b)) ?x66)))
 (and (and (> 0.0 (+ ?x16 ?x66)) (> 0.0 ?x72))))))))
(check-sat)

