; benchmark generated from python API
(set-info :status unknown)
(declare-fun skoS () Real)
(declare-fun delta () Real)
(assert
 (let (($x15 (<= 0.0 delta)))
 (and $x15 (<= 0.0 (+ (- 9.0) (* 20.0 skoS))))))
(check-sat)


