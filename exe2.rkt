#lang racket
; Write a procedure that takes a list, and returns the same list with the second value removed. For example, given (list 3 1 4), it returns (list 3 4). 
(define (drop-two lst)
  (if (null? lst)
      '()
      (cons (car lst) (cdr (cdr lst)))))

;done
;________________________________________________________________

; Write a procedure that takes in a list, and returns the reverse of the list. For 
; example, if it takes in '(a b c), it will output '(c b a).
(define (reverse-list lst)
  (if (null? lst)
      '()
      (append (reverse-list (cdr lst)) (list (car lst)))))
;done
;_________________________________________________________________


; Write a procedure that takes a list of length n, and returns a list of n copies of
; the list. For example, if the input list is (list 1 2 3), the output list is 
; (list (list 1 2 3) (list 1 2 3) (list 1 2 3)).
(define (copy-n lst)
  (map (lambda (x) lst ) lst))

;done
;_________________________________________________________________

; Write a procedure that takes a positive integer n, and returns a list of the 
; integers from 1 to n. For example, given input 3, it will return (list 1 2 3).
(define (count-list n)
  (if (equal? n 1)
      (list 1)
      (append (count-list (+ n -1)) (list n))))

;done
;_________________________________________________________________

; Write a procedure that takes a list of numbers, and returns the maximum value.
(define (max-list lst)
  (apply max lst))
;done
;_________________________________________________________________

; Write a procedure that takes a list of numbers, and replaces each number with #t if
; the number is greater than 5, and #f otherwise. For example, given input 
; (list 5 4 7), it will return (list #f #f #t).

(define (tf-list lst)
  (map (lambda (x) (if (> x 5) '(#t) '(#f))) lst))

;done
;_________________________________________________________________

; Write a procedure that takes three strings, x, y, and z, and returns the 
; concatenation of the three strings.

(define (concat-strs x y z)
  (append x y z))

;done
;_________________________________________________________________

; Write a procedure that takes a string x, and a positive integer n, and returns the 
; string x^n.
(define (xn-gen x n)
  (if (equal? n 0)
      '()
      (append x (xn-gen x (- n 1)))))
;done
;_________________________________________________________________

; Define L as a language containing a single string, L={[a]}. Write a procedure that 
; takes a string, and decides if it is a member of the language L*. That is, given a 
; string x, the procedure should return #t if x is a member of L*, and #f otherwise.
(define (is-a? str)
  (if (null? str)
      #t
      (if (equal? (car str) (car '(a)))
          (is-a? (cdr str))
          #f)))
;done
;_________________________________________________________________

; Define L as a language containing a single string, L={[ab]}. Write a procedure that 
; takes a string, and decides if it is a member of the language L.
(define (is-ab? str)
  (equal? str '(a b)))

;done
;_________________________________________________________________

; Suppose that we are given two languages, A and B, and we are also given a procedure 
; f that decides if a string is in A, and a procedure g that decides if a string is 
; in B. For example, when we evaluate (f x), it will return #t if x is in A, and #f 
; otherwise. Write a procedure that takes a string x and the two procedures f and g 
; as arguments, and decides whether x is in the intersection of A and B.


;_________________________________________________________________

; Write a procedure that takes two languages A and B (which are input as lists of 
; strings), and returns the concatenation of A and B.
(define (concat-lang a b)
  (if (equal? (length a) (length b))
      (cons (list (car a) (car b)) (concat-lang (cdr a) (cdr b)))
      '()))
;_________________________________________________________________

; Let A and B be languages. We'll use concat(A,B) to denote the concatenation of A 
; and B, in that order. Find an example of languages A and B such that concat(A,B) = 
; concat(B,A).

_________________________________________________________________

; Let A and B be languages. Find an example of languages A and B such that 
; concat(A,B) does not equal concat(B,A).

_________________________________________________________________

; Find an example of a language L such that L=L^2, i.e. L=concat(L,L).

_________________________________________________________________

; Formal languages are often used to model aspects of natural languages. Can you 
; think of some fragment of English that could be modeled using the operations 
; defined in class?