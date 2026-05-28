; benchmark generated from python API
(set-info :status unknown)
(declare-fun c () Real)
(assert
 (and (> 0.0 (+ 5.0 (* 2.0 c))) (> 0.0 (+ 3.0 (^ c 2.0) (* 5.0 c)))))
(check-sat)


