; benchmark generated from python API
(set-info :status unknown)
(declare-fun skoS2 () Real)
(declare-fun pi () Real)
(declare-fun skoX () Real)
(declare-fun delta () Real)
(assert
 (let (($x15 (<= 0.0 delta)))
 (and $x15 (< 0.0 skoX) (> 0.0 (+ (- 1.0) skoX)) (< 0.0 (+ (- 15707963.0) (* 5000000.0 pi))) (> 0.0 (+ (- 31415927.0) (* 10000000.0 pi))) (and (distinct 0.0 (+ 1.0 (* 2.0 skoS2))) true))))
(check-sat)


