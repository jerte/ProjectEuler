(defun is-prime (x)
  (if (<= x 2) t
      (do ((n 2 (1+ n)))
	  ((>= n (+ (sqrt x) 1)))
	(if (equalp 0 (mod x n)) (return-from is-prime nil))))
  (return-from is-prime t))

(defun prime-factors (x)
  (do ((n 1 (1+ n))
       (factors ())
       (x1 x))
      ((equalp x (apply '* factors)) factors)
    (when (and (is-prime n) (equalp 0 (mod x1 n)))
      (push n factors) (setf x1 (/ x1 n))
      (if (equalp 0 (mod x1 n))
      
      
