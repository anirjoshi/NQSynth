; benchmark generated from python API
(set-info :status unknown)
(declare-fun delta () Real)
(declare-fun b () Real)
(assert
 (let ((?x49 (* (- 1.0) delta)))
 (let ((?x48 (^ delta 2.0)))
 (let ((?x38 (^ b 2.0)))
 (let (($x58 (or (< 0.0 (+ (- 2.0) delta)) (>= 0.0 (+ (- 2.0) ?x38 ?x48 ?x49 (* (* (- 2.0) b) delta))) (>= 0.0 (+ (- 2.0) ?x38 ?x48 ?x49 (* (* 2.0 b) delta))))))
 (and (<= 0.0 (+ (- 3.0) delta ?x38)) (<= 0.0 (+ 3.0 delta (* (- 1.0) ?x38))) $x58))))))
(check-sat)


