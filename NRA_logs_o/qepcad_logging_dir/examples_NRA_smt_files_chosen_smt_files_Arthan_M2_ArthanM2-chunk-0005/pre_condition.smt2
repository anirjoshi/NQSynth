; benchmark generated from python API
(set-info :status unknown)
(declare-fun delta () Real)
(declare-fun skoSINS () Real)
(declare-fun skoM () Real)
(assert
 (let (($x15 (<= 0.0 delta)))
 (and $x15 (<= 0.0 (+ (- 2.0) skoM)) (>= 0.0 (+ (- 1.0) (^ skoSINS 2.0) (* (- 1.0) delta))))))
(check-sat)


