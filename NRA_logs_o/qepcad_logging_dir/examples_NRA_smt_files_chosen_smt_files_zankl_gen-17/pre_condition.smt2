; benchmark generated from python API
(set-info :status unknown)
(declare-fun delta () Real)
(declare-fun b () Real)
(assert
 (let ((?x50 (^ delta 2.0)))
 (let ((?x49 (^ b 2.0)))
 (let (($x55 (>= 0.0 (+ (- 2.0) ?x49 ?x50 (* (- 1.0) delta) (* (* (- 2.0) b) delta)))))
 (and (<= 0.0 (+ (- 3.0) delta (^ b 3.0))) (<= 0.0 (+ 3.0 delta (* (- 1.0) (^ b 3.0)))) (or (< 0.0 (+ (- 2.0) delta)) $x55))))))
(check-sat)


