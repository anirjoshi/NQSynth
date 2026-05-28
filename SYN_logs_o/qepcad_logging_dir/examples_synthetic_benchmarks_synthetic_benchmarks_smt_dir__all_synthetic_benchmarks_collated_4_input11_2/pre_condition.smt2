; benchmark generated from python API
(set-info :status unknown)
(declare-fun c () Real)
(declare-fun d () Real)
(assert
 (let (($x46 (or (< 0.0 d) (> 0.0 (+ (- 1.0) (* 4.0 c))) (> 0.0 (+ (^ d 2.0) (* (- 1.0) c))))))
 (and (< 0.0 (+ 1.0 (* 4.0 c) (* 4.0 d))) $x46)))
(check-sat)


