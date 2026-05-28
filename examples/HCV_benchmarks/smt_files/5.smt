; benchmark generated from python API
(set-info :status unknown)
(declare-fun delta () Real)
(declare-fun M () Real)
(declare-fun P () Real)
(declare-fun r () Real)
(declare-fun K () Real)
(declare-fun v () Real)
(assert
 (let (($x61 (>= 0.0 (+ (+ (+ 0.0 (* (- 1.0) P)) (* 5.0 M)) (* (- 1.0) delta)))))
 (let (($x54 (>= 0.0 (+ (+ (+ 0.0 (* 1.0 P)) (* (- 5.0) M)) (* (- 1.0) delta)))))
 (let ((?x30 (* (- 1.0) delta)))
 (let ((?x42 (+ (+ 0.0 (* (* (* (* (* (- (/ 1.0 2.0)) v) v) r) r) M)) (* (* (* (- 1.0) K) v) v))))
 (let ((?x24 (+ (+ 0.0 (* (* (* (* (* (/ 1.0 2.0) v) v) r) r) M)) (* (* (* 1.0 K) v) v))))
 (and (>= 0.0 (+ (+ ?x24 (* (* (* (- 1.0) K) r) r)) ?x30)) (>= 0.0 (+ (+ ?x42 (* (* (* 1.0 K) r) r)) ?x30)) $x54 $x61)))))))
(check-sat)

