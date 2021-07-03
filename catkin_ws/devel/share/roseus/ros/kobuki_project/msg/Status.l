;; Auto-generated. Do not edit!


(when (boundp 'kobuki_project::Status)
  (if (not (find-package "KOBUKI_PROJECT"))
    (make-package "KOBUKI_PROJECT"))
  (shadow 'Status (find-package "KOBUKI_PROJECT")))
(unless (find-package "KOBUKI_PROJECT::STATUS")
  (make-package "KOBUKI_PROJECT::STATUS"))

(in-package "ROS")
;;//! \htmlinclude Status.msg.html


(defclass kobuki_project::Status
  :super ros::object
  :slots (_x _y _left _front _right _power ))

(defmethod kobuki_project::Status
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:left __left) nil)
    ((:front __front) nil)
    ((:right __right) nil)
    ((:power __power) 0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _left __left)
   (setq _front __front)
   (setq _right __right)
   (setq _power (round __power))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:left
   (&optional __left)
   (if __left (setq _left __left)) _left)
  (:front
   (&optional __front)
   (if __front (setq _front __front)) _front)
  (:right
   (&optional __right)
   (if __right (setq _right __right)) _right)
  (:power
   (&optional __power)
   (if __power (setq _power __power)) _power)
  (:serialization-length
   ()
   (+
    ;; float32 _x
    4
    ;; float32 _y
    4
    ;; bool _left
    1
    ;; bool _front
    1
    ;; bool _right
    1
    ;; uint32 _power
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _left
       (if _left (write-byte -1 s) (write-byte 0 s))
     ;; bool _front
       (if _front (write-byte -1 s) (write-byte 0 s))
     ;; bool _right
       (if _right (write-byte -1 s) (write-byte 0 s))
     ;; uint32 _power
       (write-long _power s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _left
     (setq _left (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _front
     (setq _front (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _right
     (setq _right (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; uint32 _power
     (setq _power (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get kobuki_project::Status :md5sum-) "e2b13e0be7f646a991aebf8dd021b595")
(setf (get kobuki_project::Status :datatype-) "kobuki_project/Status")
(setf (get kobuki_project::Status :definition-)
      "float32 x     # X position
float32 y     # Y position
bool left     # left bumper
bool front    # front bumper
bool right    # right bumper
uint32 power  # power system state: 0: unplugged, 1: plugged to adapter, 2: plugged to dock, 3: charged, 4: battery_low, 5: battery_critical 

")



(provide :kobuki_project/Status "e2b13e0be7f646a991aebf8dd021b595")


