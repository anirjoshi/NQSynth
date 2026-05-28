; benchmark generated from python API
(set-info :status unknown)
(declare-fun r () Real)
(declare-fun a () Real)
(assert
 (let ((?x40 (^ a 2.0)))
 (let ((?x57 (+ 1024.0 ?x40 (* (* (- 1.0) (^ a 4.0)) (^ r 3.0)) (* (* (- 48.0) r) ?x40) (* (* 36.0 (^ a 4.0)) (^ r 4.0)) (* (* 384.0 ?x40) (^ r 2.0)))))
 (and (< 0.0 (+ (- 1.0) (* 36.0 r))) (> 0.0 ?x57)))))
(check-sat)


