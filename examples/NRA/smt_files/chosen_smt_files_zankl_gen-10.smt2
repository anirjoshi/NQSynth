(set-info :smt-lib-version 2.6)
(set-logic QF_NRA)
(declare-fun delta () Real)
(define-fun myeq ( (x Real) (y Real) ) Bool ( and (<= (- x y) delta) (<= (- y x) delta) ) )


(assert (<= 0 delta))
(set-info :source |
Harald Roman Zankl <Harald.Zankl@uibk.ac.at>

|)
(set-info :category "crafted")
(declare-fun a () Real)
(assert (myeq (* 4 (* a a)) 2))
(check-sat)
(exit)
