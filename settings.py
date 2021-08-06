# 20/07/2021 - 04/08/2021
class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game settings."""

		# Screen Settings
		self.screen_width = 1535
		self.screen_height = 790
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_speed = 1.0

		# Bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		# Alien sttings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		# fleet_direction of 1 represents right: -1 represents left.
		self.fleet_direction = 1