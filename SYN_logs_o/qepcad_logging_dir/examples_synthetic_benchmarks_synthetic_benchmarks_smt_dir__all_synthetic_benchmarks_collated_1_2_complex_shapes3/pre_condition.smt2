; benchmark generated from python API
(set-info :status unknown)
(declare-fun r () Real)
(declare-fun a () Real)
(assert
 (and (< 0.0 r) (or (and (distinct 0.0 a) true) (< 0.0 (+ (- 1.0) (* 36.0 r))))))
(check-sat)


