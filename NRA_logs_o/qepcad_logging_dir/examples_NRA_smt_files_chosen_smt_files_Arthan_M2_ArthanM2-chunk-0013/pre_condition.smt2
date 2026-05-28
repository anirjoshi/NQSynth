; benchmark generated from python API
(set-info :status unknown)
(declare-fun delta () Real)
(declare-fun skoSINS () Real)
(declare-fun skoM () Real)
(assert
 (and (<= 0.0 (+ (- 2.0) delta)) (<= 0.0 (+ (- 2.0) skoM)) (>= 0.0 (+ skoM (* (- 1.0) delta))) (>= 0.0 (+ (- 1.0) (^ skoSINS 2.0) (* (- 1.0) delta)))))
(check-sat)


