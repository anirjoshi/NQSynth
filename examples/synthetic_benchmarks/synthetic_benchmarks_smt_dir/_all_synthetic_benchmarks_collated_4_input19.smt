; benchmark generated from python API
(set-info :status unknown)
(declare-fun c () Real)
(declare-fun z () Real)
(declare-fun y () Real)
(declare-fun b () Real)
(declare-fun x () Real)
(declare-fun a () Real)
(assert
 (let ((?x54 (+ (+ (+ 0.0 (* (* 1.0 y) y)) (* (* 1.0 z) z)) (* (- 1.0) c))))
 (let ((?x63 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* 1.0 z) z)) (* (- 1.0) b))))
 (let ((?x74 (+ (+ (+ 0.0 (* (* 1.0 x) x)) (* (* 1.0 y) y)) (* (- 1.0) a))))
 (and (and (> 0.0 ?x74) (> 0.0 ?x63) (> 0.0 ?x54)))))))
(check-sat)

