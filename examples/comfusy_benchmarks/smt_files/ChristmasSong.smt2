(set-logic NRA)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 1) Declare all variables (originally Int) now as Real
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(declare-fun eLines () Real)
(declare-fun iLines () Real)
(declare-fun iSyls () Real)
(declare-fun nSyls () Real)
(declare-fun line7 () Real)
(declare-fun line8 () Real)
(declare-fun nsLines () Real)
(declare-fun nLines () Real)
(declare-fun tLines () Real)
(declare-fun tLinesFact () Real)

;; Extra real parameters for "integer closeness" and "equality closeness"
(declare-fun delta () Real)
(declare-fun delta2 () Real)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Helper Macros
;;
;; In older or strict solvers, we often have to nest (or ...) pairs
;; because (or b1 b2 b3 ...) might not parse well. So we define a small
;; trick to nest them. We'll write them out by hand so we never pass
;; more than two arguments to each (or ...).
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; A small helper "or" for a list of booleans can be nested as:
;;   (or b1 (or b2 (or b3 (or b4 ... ))))

;; Similarly, we replace "(- delta)" by "(* -1 delta)" to do unary minus.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 2) For each variable, disjoin the 21 possible almost-integer constraints
;;    from -10 to 10.  We'll nest or's in a chain.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Because it's large, let's show the pattern for eLines, then we do the same
;; for all other variables. Each disjunct is:
;;   (and (>= (+ eLines 10) (* -1 delta)) (<= (+ eLines 10) delta))
;; etc.

;; We'll define a small function to nest or's:
;;   (or D1 (or D2 (or D3 (...))))
;;
;; Each Dk is (and (>= (+ var -k) (* -1 delta)) (<= (+ var -k) delta)) if k < 0
;; or       (and (>= (- var k) (* -1 delta)) (<= (- var k) delta)) if k > 0
;; and similarly for k=0.

;; eLines
(assert
  (or
    (and (>= (+ eLines 10) (* -1 delta)) (<= (+ eLines 10) delta))
    (or
      (and (>= (+ eLines 9) (* -1 delta)) (<= (+ eLines 9) delta))
      (or
        (and (>= (+ eLines 8) (* -1 delta)) (<= (+ eLines 8) delta))
        (or
          (and (>= (+ eLines 7) (* -1 delta)) (<= (+ eLines 7) delta))
          (or
            (and (>= (+ eLines 6) (* -1 delta)) (<= (+ eLines 6) delta))
            (or
              (and (>= (+ eLines 5) (* -1 delta)) (<= (+ eLines 5) delta))
              (or
                (and (>= (+ eLines 4) (* -1 delta)) (<= (+ eLines 4) delta))
                (or
                  (and (>= (+ eLines 3) (* -1 delta)) (<= (+ eLines 3) delta))
                  (or
                    (and (>= (+ eLines 2) (* -1 delta)) (<= (+ eLines 2) delta))
                    (or
                      (and (>= (+ eLines 1) (* -1 delta)) (<= (+ eLines 1) delta))
                      (or
                        (and (>= eLines (* -1 delta)) (<= eLines delta))
                        (or
                          (and (>= (- eLines 1) (* -1 delta)) (<= (- eLines 1) delta))
                          (or
                            (and (>= (- eLines 2) (* -1 delta)) (<= (- eLines 2) delta))
                            (or
                              (and (>= (- eLines 3) (* -1 delta)) (<= (- eLines 3) delta))
                              (or
                                (and (>= (- eLines 4) (* -1 delta)) (<= (- eLines 4) delta))
                                (or
                                  (and (>= (- eLines 5) (* -1 delta)) (<= (- eLines 5) delta))
                                  (or
                                    (and (>= (- eLines 6) (* -1 delta)) (<= (- eLines 6) delta))
                                    (or
                                      (and (>= (- eLines 7) (* -1 delta)) (<= (- eLines 7) delta))
                                      (or
                                        (and (>= (- eLines 8) (* -1 delta)) (<= (- eLines 8) delta))
                                        (or
                                          (and (>= (- eLines 9) (* -1 delta)) (<= (- eLines 9) delta))
                                          (and (>= (- eLines 10) (* -1 delta)) (<= (- eLines 10) delta))
                                        )
                                      )
                                    )
                                  )
                                )
                              )
                            )
                          )
                        )
                      )
                    )
                  )
                )
              )
            )
          )
        )
      )
    )
  )
)

;; iLines
(assert
  (or
    (and (>= (+ iLines 10) (* -1 delta)) (<= (+ iLines 10) delta))
    (or
      (and (>= (+ iLines 9) (* -1 delta)) (<= (+ iLines 9) delta))
      (or
        (and (>= (+ iLines 8) (* -1 delta)) (<= (+ iLines 8) delta))
        (or
          (and (>= (+ iLines 7) (* -1 delta)) (<= (+ iLines 7) delta))
          (or
            (and (>= (+ iLines 6) (* -1 delta)) (<= (+ iLines 6) delta))
            (or
              (and (>= (+ iLines 5) (* -1 delta)) (<= (+ iLines 5) delta))
              (or
                (and (>= (+ iLines 4) (* -1 delta)) (<= (+ iLines 4) delta))
                (or
                  (and (>= (+ iLines 3) (* -1 delta)) (<= (+ iLines 3) delta))
                  (or
                    (and (>= (+ iLines 2) (* -1 delta)) (<= (+ iLines 2) delta))
                    (or
                      (and (>= (+ iLines 1) (* -1 delta)) (<= (+ iLines 1) delta))
                      (or
                        (and (>= iLines (* -1 delta)) (<= iLines delta))
                        (or
                          (and (>= (- iLines 1) (* -1 delta)) (<= (- iLines 1) delta))
                          (or
                            (and (>= (- iLines 2) (* -1 delta)) (<= (- iLines 2) delta))
                            (or
                              (and (>= (- iLines 3) (* -1 delta)) (<= (- iLines 3) delta))
                              (or
                                (and (>= (- iLines 4) (* -1 delta)) (<= (- iLines 4) delta))
                                (or
                                  (and (>= (- iLines 5) (* -1 delta)) (<= (- iLines 5) delta))
                                  (or
                                    (and (>= (- iLines 6) (* -1 delta)) (<= (- iLines 6) delta))
                                    (or
                                      (and (>= (- iLines 7) (* -1 delta)) (<= (- iLines 7) delta))
                                      (or
                                        (and (>= (- iLines 8) (* -1 delta)) (<= (- iLines 8) delta))
                                        (or
                                          (and (>= (- iLines 9) (* -1 delta)) (<= (- iLines 9) delta))
                                          (and (>= (- iLines 10) (* -1 delta)) (<= (- iLines 10) delta))
                                        )
                                      )
                                    )
                                  )
                                )
                              )
                            )
                          )
                        )
                      )
                    )
                  )
                )
              )
            )
          )
        )
      )
    )
  )
)

;; iSyls
(assert
  (or
    (and (>= (+ iSyls 10) (* -1 delta)) (<= (+ iSyls 10) delta))
    (or
      (and (>= (+ iSyls 9) (* -1 delta)) (<= (+ iSyls 9) delta))
      (or
        (and (>= (+ iSyls 8) (* -1 delta)) (<= (+ iSyls 8) delta))
        (or
          (and (>= (+ iSyls 7) (* -1 delta)) (<= (+ iSyls 7) delta))
          (or
            (and (>= (+ iSyls 6) (* -1 delta)) (<= (+ iSyls 6) delta))
            (or
              (and (>= (+ iSyls 5) (* -1 delta)) (<= (+ iSyls 5) delta))
              (or
                (and (>= (+ iSyls 4) (* -1 delta)) (<= (+ iSyls 4) delta))
                (or
                  (and (>= (+ iSyls 3) (* -1 delta)) (<= (+ iSyls 3) delta))
                  (or
                    (and (>= (+ iSyls 2) (* -1 delta)) (<= (+ iSyls 2) delta))
                    (or
                      (and (>= (+ iSyls 1) (* -1 delta)) (<= (+ iSyls 1) delta))
                      (or
                        (and (>= iSyls (* -1 delta)) (<= iSyls delta))
                        (or
                          (and (>= (- iSyls 1) (* -1 delta)) (<= (- iSyls 1) delta))
                          (or
                            (and (>= (- iSyls 2) (* -1 delta)) (<= (- iSyls 2) delta))
                            (or
                              (and (>= (- iSyls 3) (* -1 delta)) (<= (- iSyls 3) delta))
                              (or
                                (and (>= (- iSyls 4) (* -1 delta)) (<= (- iSyls 4) delta))
                                (or
                                  (and (>= (- iSyls 5) (* -1 delta)) (<= (- iSyls 5) delta))
                                  (or
                                    (and (>= (- iSyls 6) (* -1 delta)) (<= (- iSyls 6) delta))
                                    (or
                                      (and (>= (- iSyls 7) (* -1 delta)) (<= (- iSyls 7) delta))
                                      (or
                                        (and (>= (- iSyls 8) (* -1 delta)) (<= (- iSyls 8) delta))
                                        (or
                                          (and (>= (- iSyls 9) (* -1 delta)) (<= (- iSyls 9) delta))
                                          (and (>= (- iSyls 10) (* -1 delta)) (<= (- iSyls 10) delta))
                                        )
                                      )
                                    )
                                  )
                                )
                              )
                            )
                          )
                        )
                      )
                    )
                  )
                )
              )
            )
          )
        )
      )
    )
  )
)

;; nSyls
(assert
  (or
    (and (>= (+ nSyls 10) (* -1 delta)) (<= (+ nSyls 10) delta))
    (or
      (and (>= (+ nSyls 9) (* -1 delta)) (<= (+ nSyls 9) delta))
      (or
        (and (>= (+ nSyls 8) (* -1 delta)) (<= (+ nSyls 8) delta))
        (or
          (and (>= (+ nSyls 7) (* -1 delta)) (<= (+ nSyls 7) delta))
          (or
            (and (>= (+ nSyls 6) (* -1 delta)) (<= (+ nSyls 6) delta))
            (or
              (and (>= (+ nSyls 5) (* -1 delta)) (<= (+ nSyls 5) delta))
              (or
                (and (>= (+ nSyls 4) (* -1 delta)) (<= (+ nSyls 4) delta))
                (or
                  (and (>= (+ nSyls 3) (* -1 delta)) (<= (+ nSyls 3) delta))
                  (or
                    (and (>= (+ nSyls 2) (* -1 delta)) (<= (+ nSyls 2) delta))
                    (or
                      (and (>= (+ nSyls 1) (* -1 delta)) (<= (+ nSyls 1) delta))
                      (or
                        (and (>= nSyls (* -1 delta)) (<= nSyls delta))
                        (or
                          (and (>= (- nSyls 1) (* -1 delta)) (<= (- nSyls 1) delta))
                          (or
                            (and (>= (- nSyls 2) (* -1 delta)) (<= (- nSyls 2) delta))
                            (or
                              (and (>= (- nSyls 3) (* -1 delta)) (<= (- nSyls 3) delta))
                              (or
                                (and (>= (- nSyls 4) (* -1 delta)) (<= (- nSyls 4) delta))
                                (or
                                  (and (>= (- nSyls 5) (* -1 delta)) (<= (- nSyls 5) delta))
                                  (or
                                    (and (>= (- nSyls 6) (* -1 delta)) (<= (- nSyls 6) delta))
                                    (or
                                      (and (>= (- nSyls 7) (* -1 delta)) (<= (- nSyls 7) delta))
                                      (or
                                        (and (>= (- nSyls 8) (* -1 delta)) (<= (- nSyls 8) delta))
                                        (or
                                          (and (>= (- nSyls 9) (* -1 delta)) (<= (- nSyls 9) delta))
                                          (and (>= (- nSyls 10) (* -1 delta)) (<= (- nSyls 10) delta))
                                        )
                                      )
                                    )
                                  )
                                )
                              )
                            )
                          )
                        )
                      )
                    )
                  )
                )
              )
            )
          )
        )
      )
    )
  )
)

;; line7
(assert
  (or
    (and (>= (+ line7 10) (* -1 delta)) (<= (+ line7 10) delta))
    (or
      (and (>= (+ line7 9) (* -1 delta)) (<= (+ line7 9) delta))
      (or
        (and (>= (+ line7 8) (* -1 delta)) (<= (+ line7 8) delta))
        (or
          (and (>= (+ line7 7) (* -1 delta)) (<= (+ line7 7) delta))
          (or
            (and (>= (+ line7 6) (* -1 delta)) (<= (+ line7 6) delta))
            (or
              (and (>= (+ line7 5) (* -1 delta)) (<= (+ line7 5) delta))
              (or
                (and (>= (+ line7 4) (* -1 delta)) (<= (+ line7 4) delta))
                (or
                  (and (>= (+ line7 3) (* -1 delta)) (<= (+ line7 3) delta))
                  (or
                    (and (>= (+ line7 2) (* -1 delta)) (<= (+ line7 2) delta))
                    (or
                      (and (>= (+ line7 1) (* -1 delta)) (<= (+ line7 1) delta))
                      (or
                        (and (>= line7 (* -1 delta)) (<= line7 delta))
                        (or
                          (and (>= (- line7 1) (* -1 delta)) (<= (- line7 1) delta))
                          (or
                            (and (>= (- line7 2) (* -1 delta)) (<= (- line7 2) delta))
                            (or
                              (and (>= (- line7 3) (* -1 delta)) (<= (- line7 3) delta))
                              (or
                                (and (>= (- line7 4) (* -1 delta)) (<= (- line7 4) delta))
                                (or
                                  (and (>= (- line7 5) (* -1 delta)) (<= (- line7 5) delta))
                                  (or
                                    (and (>= (- line7 6) (* -1 delta)) (<= (- line7 6) delta))
                                    (or
                                      (and (>= (- line7 7) (* -1 delta)) (<= (- line7 7) delta))
                                      (or
                                        (and (>= (- line7 8) (* -1 delta)) (<= (- line7 8) delta))
                                        (or
                                          (and (>= (- line7 9) (* -1 delta)) (<= (- line7 9) delta))
                                          (and (>= (- line7 10) (* -1 delta)) (<= (- line7 10) delta))
                                        )
                                      )
                                    )
                                  )
                                )
                              )
                            )
                          )
                        )
                      )
                    )
                  )
                )
              )
            )
          )
        )
      )
    )
  )
)

;; line8
(assert
  (or
    (and (>= (+ line8 10) (* -1 delta)) (<= (+ line8 10) delta))
    (or
      (and (>= (+ line8 9) (* -1 delta)) (<= (+ line8 9) delta))
      (or
        (and (>= (+ line8 8) (* -1 delta)) (<= (+ line8 8) delta))
        (or
          (and (>= (+ line8 7) (* -1 delta)) (<= (+ line8 7) delta))
          (or
            (and (>= (+ line8 6) (* -1 delta)) (<= (+ line8 6) delta))
            (or
              (and (>= (+ line8 5) (* -1 delta)) (<= (+ line8 5) delta))
              (or
                (and (>= (+ line8 4) (* -1 delta)) (<= (+ line8 4) delta))
                (or
                  (and (>= (+ line8 3) (* -1 delta)) (<= (+ line8 3) delta))
                  (or
                    (and (>= (+ line8 2) (* -1 delta)) (<= (+ line8 2) delta))
                    (or
                      (and (>= (+ line8 1) (* -1 delta)) (<= (+ line8 1) delta))
                      (or
                        (and (>= line8 (* -1 delta)) (<= line8 delta))
                        (or
                          (and (>= (- line8 1) (* -1 delta)) (<= (- line8 1) delta))
                          (or
                            (and (>= (- line8 2) (* -1 delta)) (<= (- line8 2) delta))
                            (or
                              (and (>= (- line8 3) (* -1 delta)) (<= (- line8 3) delta))
                              (or
                                (and (>= (- line8 4) (* -1 delta)) (<= (- line8 4) delta))
                                (or
                                  (and (>= (- line8 5) (* -1 delta)) (<= (- line8 5) delta))
                                  (or
                                    (and (>= (- line8 6) (* -1 delta)) (<= (- line8 6) delta))
                                    (or
                                      (and (>= (- line8 7) (* -1 delta)) (<= (- line8 7) delta))
                                      (or
                                        (and (>= (- line8 8) (* -1 delta)) (<= (- line8 8) delta))
                                        (or
                                          (and (>= (- line8 9) (* -1 delta)) (<= (- line8 9) delta))
                                          (and (>= (- line8 10) (* -1 delta)) (<= (- line8 10) delta))
                                        )
                                      )
                                    )
                                  )
                                )
                              )
                            )
                          )
                        )
                      )
                    )
                  )
                )
              )
            )
          )
        )
      )
    )
  )
)

;; nsLines
(assert
  (or
    (and (>= (+ nsLines 10) (* -1 delta)) (<= (+ nsLines 10) delta))
    (or
      (and (>= (+ nsLines 9) (* -1 delta)) (<= (+ nsLines 9) delta))
      (or
        (and (>= (+ nsLines 8) (* -1 delta)) (<= (+ nsLines 8) delta))
        (or
          (and (>= (+ nsLines 7) (* -1 delta)) (<= (+ nsLines 7) delta))
          (or
            (and (>= (+ nsLines 6) (* -1 delta)) (<= (+ nsLines 6) delta))
            (or
              (and (>= (+ nsLines 5) (* -1 delta)) (<= (+ nsLines 5) delta))
              (or
                (and (>= (+ nsLines 4) (* -1 delta)) (<= (+ nsLines 4) delta))
                (or
                  (and (>= (+ nsLines 3) (* -1 delta)) (<= (+ nsLines 3) delta))
                  (or
                    (and (>= (+ nsLines 2) (* -1 delta)) (<= (+ nsLines 2) delta))
                    (or
                      (and (>= (+ nsLines 1) (* -1 delta)) (<= (+ nsLines 1) delta))
                      (or
                        (and (>= nsLines (* -1 delta)) (<= nsLines delta))
                        (or
                          (and (>= (- nsLines 1) (* -1 delta)) (<= (- nsLines 1) delta))
                          (or
                            (and (>= (- nsLines 2) (* -1 delta)) (<= (- nsLines 2) delta))
                            (or
                              (and (>= (- nsLines 3) (* -1 delta)) (<= (- nsLines 3) delta))
                              (or
                                (and (>= (- nsLines 4) (* -1 delta)) (<= (- nsLines 4) delta))
                                (or
                                  (and (>= (- nsLines 5) (* -1 delta)) (<= (- nsLines 5) delta))
                                  (or
                                    (and (>= (- nsLines 6) (* -1 delta)) (<= (- nsLines 6) delta))
                                    (or
                                      (and (>= (- nsLines 7) (* -1 delta)) (<= (- nsLines 7) delta))
                                      (or
                                        (and (>= (- nsLines 8) (* -1 delta)) (<= (- nsLines 8) delta))
                                        (or
                                          (and (>= (- nsLines 9) (* -1 delta)) (<= (- nsLines 9) delta))
                                          (and (>= (- nsLines 10) (* -1 delta)) (<= (- nsLines 10) delta))
                                        )
                                      )
                                    )
                                  )
                                )
                              )
                            )
                          )
                        )
                      )
                    )
                  )
                )
              )
            )
          )
        )
      )
    )
  )
)

;; nLines
(assert
  (or
    (and (>= (+ nLines 10) (* -1 delta)) (<= (+ nLines 10) delta))
    (or
      (and (>= (+ nLines 9) (* -1 delta)) (<= (+ nLines 9) delta))
      (or
        (and (>= (+ nLines 8) (* -1 delta)) (<= (+ nLines 8) delta))
        (or
          (and (>= (+ nLines 7) (* -1 delta)) (<= (+ nLines 7) delta))
          (or
            (and (>= (+ nLines 6) (* -1 delta)) (<= (+ nLines 6) delta))
            (or
              (and (>= (+ nLines 5) (* -1 delta)) (<= (+ nLines 5) delta))
              (or
                (and (>= (+ nLines 4) (* -1 delta)) (<= (+ nLines 4) delta))
                (or
                  (and (>= (+ nLines 3) (* -1 delta)) (<= (+ nLines 3) delta))
                  (or
                    (and (>= (+ nLines 2) (* -1 delta)) (<= (+ nLines 2) delta))
                    (or
                      (and (>= (+ nLines 1) (* -1 delta)) (<= (+ nLines 1) delta))
                      (or
                        (and (>= nLines (* -1 delta)) (<= nLines delta))
                        (or
                          (and (>= (- nLines 1) (* -1 delta)) (<= (- nLines 1) delta))
                          (or
                            (and (>= (- nLines 2) (* -1 delta)) (<= (- nLines 2) delta))
                            (or
                              (and (>= (- nLines 3) (* -1 delta)) (<= (- nLines 3) delta))
                              (or
                                (and (>= (- nLines 4) (* -1 delta)) (<= (- nLines 4) delta))
                                (or
                                  (and (>= (- nLines 5) (* -1 delta)) (<= (- nLines 5) delta))
                                  (or
                                    (and (>= (- nLines 6) (* -1 delta)) (<= (- nLines 6) delta))
                                    (or
                                      (and (>= (- nLines 7) (* -1 delta)) (<= (- nLines 7) delta))
                                      (or
                                        (and (>= (- nLines 8) (* -1 delta)) (<= (- nLines 8) delta))
                                        (or
                                          (and (>= (- nLines 9) (* -1 delta)) (<= (- nLines 9) delta))
                                          (and (>= (- nLines 10) (* -1 delta)) (<= (- nLines 10) delta))
                                        )
                                      )
                                    )
                                  )
                                )
                              )
                            )
                          )
                        )
                      )
                    )
                  )
                )
              )
            )
          )
        )
      )
    )
  )
)

;; tLines
(assert
  (or
    (and (>= (+ tLines 10) (* -1 delta)) (<= (+ tLines 10) delta))
    (or
      (and (>= (+ tLines 9) (* -1 delta)) (<= (+ tLines 9) delta))
      (or
        (and (>= (+ tLines 8) (* -1 delta)) (<= (+ tLines 8) delta))
        (or
          (and (>= (+ tLines 7) (* -1 delta)) (<= (+ tLines 7) delta))
          (or
            (and (>= (+ tLines 6) (* -1 delta)) (<= (+ tLines 6) delta))
            (or
              (and (>= (+ tLines 5) (* -1 delta)) (<= (+ tLines 5) delta))
              (or
                (and (>= (+ tLines 4) (* -1 delta)) (<= (+ tLines 4) delta))
                (or
                  (and (>= (+ tLines 3) (* -1 delta)) (<= (+ tLines 3) delta))
                  (or
                    (and (>= (+ tLines 2) (* -1 delta)) (<= (+ tLines 2) delta))
                    (or
                      (and (>= (+ tLines 1) (* -1 delta)) (<= (+ tLines 1) delta))
                      (or
                        (and (>= tLines (* -1 delta)) (<= tLines delta))
                        (or
                          (and (>= (- tLines 1) (* -1 delta)) (<= (- tLines 1) delta))
                          (or
                            (and (>= (- tLines 2) (* -1 delta)) (<= (- tLines 2) delta))
                            (or
                              (and (>= (- tLines 3) (* -1 delta)) (<= (- tLines 3) delta))
                              (or
                                (and (>= (- tLines 4) (* -1 delta)) (<= (- tLines 4) delta))
                                (or
                                  (and (>= (- tLines 5) (* -1 delta)) (<= (- tLines 5) delta))
                                  (or
                                    (and (>= (- tLines 6) (* -1 delta)) (<= (- tLines 6) delta))
                                    (or
                                      (and (>= (- tLines 7) (* -1 delta)) (<= (- tLines 7) delta))
                                      (or
                                        (and (>= (- tLines 8) (* -1 delta)) (<= (- tLines 8) delta))
                                        (or
                                          (and (>= (- tLines 9) (* -1 delta)) (<= (- tLines 9) delta))
                                          (and (>= (- tLines 10) (* -1 delta)) (<= (- tLines 10) delta))
                                        )
                                      )
                                    )
                                  )
                                )
                              )
                            )
                          )
                        )
                      )
                    )
                  )
                )
              )
            )
          )
        )
      )
    )
  )
)

;; tLinesFact
(assert
  (or
    (and (>= (+ tLinesFact 10) (* -1 delta)) (<= (+ tLinesFact 10) delta))
    (or
      (and (>= (+ tLinesFact 9) (* -1 delta)) (<= (+ tLinesFact 9) delta))
      (or
        (and (>= (+ tLinesFact 8) (* -1 delta)) (<= (+ tLinesFact 8) delta))
        (or
          (and (>= (+ tLinesFact 7) (* -1 delta)) (<= (+ tLinesFact 7) delta))
          (or
            (and (>= (+ tLinesFact 6) (* -1 delta)) (<= (+ tLinesFact 6) delta))
            (or
              (and (>= (+ tLinesFact 5) (* -1 delta)) (<= (+ tLinesFact 5) delta))
              (or
                (and (>= (+ tLinesFact 4) (* -1 delta)) (<= (+ tLinesFact 4) delta))
                (or
                  (and (>= (+ tLinesFact 3) (* -1 delta)) (<= (+ tLinesFact 3) delta))
                  (or
                    (and (>= (+ tLinesFact 2) (* -1 delta)) (<= (+ tLinesFact 2) delta))
                    (or
                      (and (>= (+ tLinesFact 1) (* -1 delta)) (<= (+ tLinesFact 1) delta))
                      (or
                        (and (>= tLinesFact (* -1 delta)) (<= tLinesFact delta))
                        (or
                          (and (>= (- tLinesFact 1) (* -1 delta)) (<= (- tLinesFact 1) delta))
                          (or
                            (and (>= (- tLinesFact 2) (* -1 delta)) (<= (- tLinesFact 2) delta))
                            (or
                              (and (>= (- tLinesFact 3) (* -1 delta)) (<= (- tLinesFact 3) delta))
                              (or
                                (and (>= (- tLinesFact 4) (* -1 delta)) (<= (- tLinesFact 4) delta))
                                (or
                                  (and (>= (- tLinesFact 5) (* -1 delta)) (<= (- tLinesFact 5) delta))
                                  (or
                                    (and (>= (- tLinesFact 6) (* -1 delta)) (<= (- tLinesFact 6) delta))
                                    (or
                                      (and (>= (- tLinesFact 7) (* -1 delta)) (<= (- tLinesFact 7) delta))
                                      (or
                                        (and (>= (- tLinesFact 8) (* -1 delta)) (<= (- tLinesFact 8) delta))
                                        (or
                                          (and (>= (- tLinesFact 9) (* -1 delta)) (<= (- tLinesFact 9) delta))
                                          (and (>= (- tLinesFact 10) (* -1 delta)) (<= (- tLinesFact 10) delta))
                                        )
                                      )
                                    )
                                  )
                                )
                              )
                            )
                          )
                        )
                      )
                    )
                  )
                )
              )
            )
          )
        )
      )
    )
  )
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 3) Convert the equality constraints LHS = RHS into:
;;         -delta2 <= (LHS - RHS) <= delta2
;;    Here we also rewrite unary minus as (* -1 delta2), if needed.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; tLines == eLines + nLines
(assert
  (and
    (>= (- tLines (+ eLines nLines)) (* -1 delta2))
    (<= (- tLines (+ eLines nLines)) delta2)
  )
)

;; nLines == iLines + nsLines
(assert
  (and
    (>= (- nLines (+ iLines nsLines)) (* -1 delta2))
    (<= (- nLines (+ iLines nsLines)) delta2)
  )
)

;; nLines == line7 + line8
(assert
  (and
    (>= (- nLines (+ line7 line8)) (* -1 delta2))
    (<= (- nLines (+ line7 line8)) delta2)
  )
)

;; nSyls + iSyls == 7 * line7 + 8 * line8
(assert
  (and
    (>= (- (+ nSyls iSyls) (+ (* 7 line7) (* 8 line8))) (* -1 delta2))
    (<= (- (+ nSyls iSyls) (+ (* 7 line7) (* 8 line8))) delta2)
  )
)

;; tLines == 4 * tLinesFact
(assert
  (and
    (>= (- tLines (* 4 tLinesFact)) (* -1 delta2))
    (<= (- tLines (* 4 tLinesFact)) delta2)
  )
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4) Convert inequalities (>= 0) to real form in prefix notation
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; line8 >= 0
(assert (>= line8 0))

;; line7 >= 0
(assert (>= line7 0))

;; tLines >= 0
(assert (>= tLines 0))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 5) Finally, check satisfiability and retrieve a model
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(check-sat)
(get-model)
