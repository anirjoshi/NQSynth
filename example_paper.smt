; benchmark generated from python API
(set-info :status unknown)
(declare-fun z () Real)
(declare-fun y () Real)
(declare-fun x () Real)
(assert
 (let ((?x36 (* 4.0 z)))
 (let ((?x34 (+ (+ (+ 0.0 (* (* (- (/ 1.0 9.0)) x) x)) (* (* (- (/ 1.0 16.0)) y) y)) (* (* (- 1.0) z) z))))
 (let ((?x20 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* (/ 1.0 9.0) y) y)) (* (* (/ 1.0 16.0) z) z))))
 (and (>= 0.0 (+ ?x20 (- 1.0))) (> 0.0 (+ (+ ?x34 ?x36) (- 2.0))))))))
(check-sat)

