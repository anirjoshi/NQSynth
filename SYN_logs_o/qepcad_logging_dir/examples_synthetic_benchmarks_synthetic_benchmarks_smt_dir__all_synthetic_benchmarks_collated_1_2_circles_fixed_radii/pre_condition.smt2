; benchmark generated from python API
(set-info :status unknown)
(declare-fun y () Real)
(assert
 (let ((?x36 (^ y 2.0)))
 (let ((?x37 (+ (- 5.0) ?x36)))
 (> 0.0 ?x37))))
(check-sat)


