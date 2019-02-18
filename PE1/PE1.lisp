(defparameter *the-list* ())
(dotimes (i 1000) (push (+ i 1) *the-list*))

(defun multiple-o-3-o-5 (x)
  (or (equalp (mod x 3) 0) (equalp (mod x 5)))
  
(apply '+ (remove-if-not #'multiple-o-3-o-5 *the-list*))
