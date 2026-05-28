; benchmark generated from python API
(set-info :status unknown)
(declare-fun r2 () Real)
(assert
 (let ((?x47 (* 8.0 (^ r2 2.0))))
 (let ((?x44 (* 4.0 (^ r2 3.0))))
 (let ((?x41 (* 4.0 r2)))
 (let ((?x48 (+ (- 1.0) ?x41 ?x44 ?x47)))
 (< 0.0 ?x48))))))
(check-sat)


