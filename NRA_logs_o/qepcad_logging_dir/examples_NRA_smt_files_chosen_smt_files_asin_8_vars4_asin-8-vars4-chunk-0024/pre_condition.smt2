; benchmark generated from python API
(set-info :status unknown)
(declare-fun delta () Real)
(declare-fun skoS2 () Real)
(declare-fun skoX () Real)
(assert
 (let (($x15 (<= 0.0 delta)))
 (and $x15 (< 0.0 skoS2) (< 0.0 skoX) (> 0.0 (+ (- 1.0) skoX)) (<= 0.0 (+ (- 2.0) delta (^ skoS2 2.0))) (>= 0.0 (+ (- 2.0) (^ skoS2 2.0) (* (- 1.0) delta))))))
(check-sat)


