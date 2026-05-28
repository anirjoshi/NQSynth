; benchmark generated from python API
(set-info :status unknown)
(declare-fun skoS () Real)
(declare-fun delta () Real)
(assert
 (let (($x15 (<= 0.0 delta)))
 (and $x15 (<= 0.0 (+ (- 217.0) (* 100.0 skoS))))))
(check-sat)


