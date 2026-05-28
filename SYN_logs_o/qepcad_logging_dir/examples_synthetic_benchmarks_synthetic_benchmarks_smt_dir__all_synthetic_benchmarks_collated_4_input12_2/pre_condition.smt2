; benchmark generated from python API
(set-info :status unknown)
(declare-fun r () Real)
(declare-fun c () Real)
(assert
 (let (($x58 (and (> 0.0 (+ 3.0 c)) (< 0.0 (+ 1.0 (* 2.0 c) (* 2.0 r))))))
 (let (($x51 (> 0.0 (+ r (^ r 2.0) (* (- 2.0) c) (* (* 2.0 c) r)))))
 (and (and (distinct 0.0 r) true) (> 0.0 (+ r (* (- 1.0) (^ c 2.0)) (* (- 2.0) c))) (or (< 0.0 (+ 1.0 c)) (> 0.0 (+ 1.0 r)) $x51 $x58)))))
(check-sat)


