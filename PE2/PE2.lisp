(defun n-th-fib (n)
  (if (< n 2) n
      (+ (n-th-fib (- n 1)) (n-th-fib (- n 2)))))

(defvar *even-fib-sum* 0)

(do ((n 0 (1+ n))
     (fib 0 (n-th-fib n)))
    ((>= fib 4000000))
  (if (evenp fib) (setf *even-fib-sum*
			(+ *even-fib-sum* fib))))

(print *even-fib-sum*)






