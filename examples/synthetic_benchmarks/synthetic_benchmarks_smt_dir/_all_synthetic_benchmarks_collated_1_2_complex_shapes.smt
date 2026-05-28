; benchmark generated from python API
(set-info :status unknown)
(declare-fun r () Real)
(declare-fun y () Real)
(declare-fun x () Real)
(declare-fun a () Real)
(assert
 (let ((?x84 (* (- 1.0) r)))
 (let ((?x79 (+ (+ 0.0 (* (* (* (* 1.0 x) x) x) x)) (* (* (* (* 1.0 y) y) y) y))))
 (let ((?x20 (+ (+ 0.0 (* (* (* (* 2.0 y) y) y) y)) (* (* (* (* 2.0 a) a) a) a))))
 (let ((?x149 (+ (+ ?x20 (* (* (* (* 257.0 x) x) x) x)) (* (* (* (* (- 20.0) x) a) a) a))))
 (let ((?x143 (+ (+ ?x149 (* (* (* (* 252.0 x) x) x) y)) (* (* (* (* 102.0 x) x) y) y))))
 (let ((?x127 (+ (+ ?x143 (* (* (* (* 6.0 y) y) a) a)) (* (* (* (* (- 260.0) x) x) x) a))))
 (let ((?x130 (+ (+ (+ ?x127 (* (* (* (* 180.0 x) x) y) a)) (- 3.0)) ?x84)))
 (and (and (> 0.0 ?x130) (> 0.0 (+ ?x79 ?x84))))))))))))
(check-sat)

