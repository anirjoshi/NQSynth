; benchmark generated from python API
(set-info :status unknown)
(declare-fun skoS () Real)
(declare-fun pi () Real)
(declare-fun delta () Real)
(assert
 (let ((?x88 (^ skoS 3.0)))
 (let (($x94 (>= 0.0 (+ (- 2.0) ?x88 (* (- 1.0) skoS) (* 4.0 (^ skoS 2.0))))))
 (let (($x70 (<= 0.0 skoS)))
 (let (($x15 (<= 0.0 delta)))
 (and $x15 $x70 (< 0.0 (+ (- 15707963.0) (* 5000000.0 pi))) (> 0.0 (+ (- 31415927.0) (* 10000000.0 pi))) $x94))))))
(check-sat)


