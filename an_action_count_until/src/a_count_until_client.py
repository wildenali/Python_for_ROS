#!/usr/bin/env python

import rospy
import actionlib

from an_action_count_until.msg import CountUntilAction, CountUntilGoal

class CountUntilClient:
	def __init__(self):
		self._ac = actionlib.SimpleActionClient('/count_until', CountUntilAction)
		self._ac.wait_for_server()
		rospy.loginfo("Action server is up, we can send new goals!")
	
	def send_goal_and_get_result(self):
		goal = CountUntilGoal(max_number=10, wait_duration=0.5)
		self._ac.send_goal(goal)
		rospy.loginfo("Goal has been sent")
		self._ac.wait_for_result()
		rospy.loginfo(self._ac.get_result())
		
if __name__ == '__main__':
	rospy.init_node('count_until_client')
	
	client = CountUntilClient()
	
	client.send_goal_and_get_result()
