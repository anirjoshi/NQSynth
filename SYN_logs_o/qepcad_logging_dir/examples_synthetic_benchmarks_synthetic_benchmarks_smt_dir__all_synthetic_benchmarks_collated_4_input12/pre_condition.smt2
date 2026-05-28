; benchmark generated from python API
(set-info :status unknown)
(declare-fun x () Real)
(assert
 (let ((?x50 (^ x 12.0)))
 (let ((?x48 (^ x 10.0)))
 (let ((?x72 (+ (- 4.0) ?x48 ?x50 (* (- 1.0) (^ x 6.0)) (* (- 1.0) (^ x 9.0)) (* (- 1.0) (^ x 11.0)) (* (- 8.0) (^ x 3.0)) (* (- 5.0) (^ x 8.0)) (* 3.0 (^ x 7.0)) (* 14.0 (^ x 4.0)))))
 (let (($x42 (<= 0.0 (+ 2.0 (^ x 3.0) (* 2.0 x) (* 2.0 (^ x 2.0))))))
 (and $x42 (or (> 0.0 (+ (- 1.0) x)) (>= 0.0 ?x72))))))))
(check-sat)


