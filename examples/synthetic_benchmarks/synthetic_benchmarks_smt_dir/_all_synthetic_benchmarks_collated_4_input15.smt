; benchmark generated from python API
(set-info :status unknown)
(declare-fun b () Real)
(declare-fun a () Real)
(declare-fun y () Real)
(declare-fun x () Real)
(assert
 (let ((?x66 (- 1.0)))
 (let ((?x64 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* 1.0 y) y)) (* (* (- 2.0) x) a))))
 (let ((?x65 (+ (+ (+ ?x64 (* (* (- 2.0) y) b)) (* (* 1.0 a) a)) (* (* 1.0 b) b))))
 (let ((?x20 (+ (+ 0.0 (* (* (* (* 1.0 x) x) x) x)) (* (* (* (* 1.0 y) y) y) y))))
 (and (and (> 0.0 (+ ?x20 ?x66)) (> 0.0 (+ ?x65 ?x66)))))))))
(check-sat)

