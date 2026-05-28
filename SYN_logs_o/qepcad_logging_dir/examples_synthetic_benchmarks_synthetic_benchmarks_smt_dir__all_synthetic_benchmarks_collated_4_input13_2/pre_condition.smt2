; benchmark generated from python API
(set-info :status unknown)
(declare-fun b () Real)
(declare-fun a () Real)
(assert
 (let ((?x41 (^ b 2.0)))
 (let ((?x40 (^ a 2.0)))
 (let ((?x42 (+ (- 4.0) ?x40 ?x41)))
 (> 0.0 ?x42)))))
(check-sat)


