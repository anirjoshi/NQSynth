; benchmark generated from python API
(set-info :status unknown)
(declare-fun c () Real)
(declare-fun d () Real)
(assert
 (and (< 0.0 d) (< 0.0 (+ d (* (- 1.0) c)))))
(check-sat)


