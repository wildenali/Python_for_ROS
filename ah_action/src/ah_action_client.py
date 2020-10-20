#!/usr/bin/env python

import rospy
import actionlib
from ah_action.msg import TimerAction, TimerGoal, TimerResult

rospy.init_node('timer_action_client')		# menamai node
client = actionlib.SimpleActionClient('timer', TimerAction)		# menghubungkan ke server yg namanya timer
client.wait_for_server()		# tunggu konek ke server

goal = TimerGoal()
goal.time_to_wait = rospy.Duration.from_sec(3.0)	# setting waktu berapa lama waktu yg ditunggu si client, yg akan di kirim ke server
client.send_goal(goal)		# kirim data ke server
client.wait_for_result()	# tunggu hasilnya
print('Time elapsed: %f' %(client.get_result().time_elapsed.to_sec()))
