from flow import FlowClient
from notifications import Notifications
from sportstracker import SportsTrackerLib
import logging
import os
import re
import traceback
import yaml

class App:
	def run(self):
		workdir = os.path.dirname(os.path.realpath(__file__))

		# enable logging
		logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO, filename=workdir+'/output.log')

		try:
			# read config file
			config = yaml.load(open(workdir+'/config.yml'))

			client = FlowClient()
			client.login(config['POLAR_USER'], config['POLAR_PASS'])

			# get last 10 activities
			activities = sorted(filter(lambda a: a.type == "EXERCISE" and (a.distance and a.distance > 0), client.activities()), key= lambda a: a.timestamp)
			activities = activities[-10:]
			
			stlib = SportsTrackerLib()
			stlib.login(config['SPORTSTRACKER_USER'], config['SPORTSTRACKER_PASS'])

			synced = []
			p = re.compile('\[polar:[0-9]+\]', re.IGNORECASE)
			for workout in stlib.get_workouts():
				if ('description' in workout):
					result = p.findall(workout['description'])	
					if len(result) > 0:
						synced.append(int(result[0].split(':')[1][:-1]))

			logging.debug('len(synced) = {}'.format(len(synced)))

			added = 0
			for activity in activities:
				if (activity.listItemId not in synced):
					stlib.add_workout(str(activity.listItemId) + '.gpx', activity.gpx(), '[polar:{}]'.format(activity.listItemId))
					added = added + 1


			Notifications.display(config['SUCCESS_TITLE'], config['SUCCESS_SYNCED_MSG'].format(added) if added > 0 else config['SUCCESS_NOT_SYNCED_MSG'])

		except Exception as e:
			logging.error("type error: " + str(e))
			logging.error(traceback.format_exc())
			Notifications.display(config['FAILURE_TITLE'], config['FAILURE_MSG'])


if __name__ == "__main__":
	app = App()
	app.run()
