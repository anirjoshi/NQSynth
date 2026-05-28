; benchmark generated from python API
(set-info :status unknown)
(declare-fun skoM () Real)
(declare-fun delta () Real)
(assert
 (let (($x15 (<= 0.0 delta)))
 (and $x15 (<= 0.0 (+ (- 2.0) skoM)))))
(check-sat)


