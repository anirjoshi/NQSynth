; benchmark generated from python API
(set-info :status unknown)
(declare-fun skoS () Real)
(declare-fun pi () Real)
(declare-fun delta () Real)
(assert
 (let (($x46 (<= 0.0 skoS)))
 (let (($x15 (<= 0.0 delta)))
 (and $x15 $x46 (< 0.0 (+ (- 15707963.0) (* 5000000.0 pi))) (> 0.0 (+ (- 31415927.0) (* 10000000.0 pi))) (> 0.0 (+ (* (- 1.0) pi) (* 2.0 skoS)))))))
(check-sat)


