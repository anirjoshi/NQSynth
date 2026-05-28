; benchmark generated from python API
(set-info :status unknown)
(declare-fun skoX () Real)
(declare-fun skoS2 () Real)
(declare-fun delta () Real)
(assert
 (let (($x15 (<= 0.0 delta)))
 (and $x15 (< 0.0 skoS2) (< 0.0 skoX) (> 0.0 (+ (- 1.0) skoX)))))
(check-sat)


