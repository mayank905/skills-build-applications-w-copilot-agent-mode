// Connect to the 'octofit_db' database before running this script if using the mongo shell.

db.createCollection("users")
db.createCollection("teams")
db.createCollection("activity")
db.createCollection("leaderboard")
db.createCollection("workouts")
db.users.createIndex({ email: 1 }, { unique: true })
