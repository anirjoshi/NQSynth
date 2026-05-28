; benchmark generated from python API
(set-info :status unknown)
(declare-fun r () Real)
(declare-fun c () Real)
(declare-fun x () Real)
(declare-fun l () Real)
(assert
 (let ((?x17 (+ (+ 0.0 (* (* 1.0 x) x)) (* (* 1.0 l) l))))
 (let ((?x69 (+ (+ (+ ?x17 (* (* (- 2.0) x) c)) (* (- 2.0) c)) (* 1.0 r))))
 (let (($x63 (and (> 0.0 (+ ?x17 (* (* (- 1.0) r) r))) (> 0.0 ?x69))))
 (and $x63)))))
(check-sat)

