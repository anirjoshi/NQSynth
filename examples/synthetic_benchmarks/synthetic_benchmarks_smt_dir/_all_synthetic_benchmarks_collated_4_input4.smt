; benchmark generated from python API
(set-info :status unknown)
(declare-fun d () Real)
(declare-fun x () Real)
(declare-fun y () Real)
(declare-fun c () Real)
(assert
 (let ((?x47 (+ (+ (+ 0.0 (* (* 1.0 y) y)) (* (* 1.0 x) x)) (* (- 1.0) d))))
 (let ((?x59 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* (- 1.0) y) y)) (* 1.0 c))))
 (and (and (> 0.0 ?x59) (> 0.0 ?x47))))))
(check-sat)

