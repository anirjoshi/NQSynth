; benchmark generated from python API
(set-info :status unknown)
(declare-fun c () Real)
(declare-fun x () Real)
(declare-fun y () Real)
(assert
 (let ((?x15 (+ (+ 0.0 (* (* 1.0 x) x)) (* (* 1.0 y) y))))
 (let (($x58 (> 0.0 (+ (+ (+ ?x15 (* (- 4.0) x)) (* 1.0 c)) 3.0))))
 (and (and (> 0.0 (+ ?x15 (* (* (- 1.0) c) c))) $x58)))))
(check-sat)

