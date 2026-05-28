; benchmark generated from python API
(set-info :status unknown)
(declare-fun y () Real)
(declare-fun x () Real)
(declare-fun c () Real)
(assert
 (let ((?x63 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* (- 1.0) y) y)) (- 10.0))))
 (let ((?x59 (+ (+ (+ 0.0 (* (* 1.0 y) y)) (* (* (- 1.0) x) y)) (* 1.0 c))))
 (and (and (> 0.0 ?x59) (> 0.0 ?x63))))))
(check-sat)

