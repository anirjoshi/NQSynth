; benchmark generated from python API
(set-info :status unknown)
(declare-fun delta () Real)
(declare-fun a () Real)
(declare-fun t () Real)
(declare-fun s () Real)
(assert
 (let ((?x18 (* (- 1.0) delta)))
 (let ((?x44 (+ (+ (+ 0.0 (* (- 1.0) s)) (* (- (/ 3.0 2.0)) a)) (* (* 1.0 t) a))))
 (let ((?x37 (+ (+ (+ 0.0 (* 1.0 s)) (* (- (/ 3.0 2.0)) a)) (* (* (- 1.0) t) a))))
 (let ((?x29 (+ (+ (+ 0.0 (* (- 2.0) s)) (* (* (* 1.0 t) t) a)) ?x18)))
 (let ((?x19 (+ (+ (+ 0.0 (* 2.0 s)) (* (* (* (- 1.0) t) t) a)) ?x18)))
 (and (>= 0.0 ?x19) (>= 0.0 ?x29) (>= 0.0 (+ ?x37 ?x18)) (>= 0.0 (+ ?x44 ?x18)))))))))
(check-sat)

