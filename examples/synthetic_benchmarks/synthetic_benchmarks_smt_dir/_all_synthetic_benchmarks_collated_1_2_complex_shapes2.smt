; benchmark generated from python API
(set-info :status unknown)
(declare-fun r () Real)
(declare-fun y () Real)
(declare-fun x () Real)
(declare-fun a () Real)
(assert
 (let ((?x48 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* 1.0 y) y)) (* (- 1.0) r))))
 (let ((?x57 (+ (+ (+ 0.0 (* (- 6.0) x)) 1.0) (* (* (* (* 1.0 y) y) y) a))))
 (and (and (> 0.0 ?x57) (> 0.0 ?x48))))))
(check-sat)

