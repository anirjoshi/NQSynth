; benchmark generated from python API
(set-info :status unknown)
(declare-fun delta () Real)
(declare-fun a () Real)
(declare-fun t () Real)
(declare-fun s () Real)
(assert
 (let ((?x20 (* (- 1.0) delta)))
 (let ((?x29 (* (* 1.0 t) a)))
 (let ((?x50 (+ (+ (+ (+ 0.0 (* (* (- 1.0) s) a)) (* (- 1.0) a)) ?x29) ?x20)))
 (let ((?x41 (+ (+ (+ 0.0 (* (* (* 1.0 s) s) t)) (* 1.0 a)) (* (* (- 1.0) t) a))))
 (let (($x33 (>= 0.0 (+ (+ (+ 0.0 (* (* (- 2.0) s) a)) (* ?x29 a)) ?x20))))
 (let ((?x19 (+ (+ 0.0 (* (* (* 2.0 s) t) t)) (* (* (* (- 1.0) t) t) a))))
 (and (>= 0.0 (+ ?x19 ?x20)) $x33 (>= 0.0 (+ ?x41 ?x20)) (>= 0.0 ?x50)))))))))
(check-sat)

