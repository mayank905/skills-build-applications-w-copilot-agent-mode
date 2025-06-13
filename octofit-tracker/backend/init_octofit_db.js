const { MongoClient } = require('mongodb');

async function init() {
  const client = await MongoClient.connect('mongodb://localhost:27017');
  const db = client.db('octofit_db');

  await db.createCollection("users");
db.createCollection("teams")
db.createCollection("activity")
db.createCollection("leaderboard")
db.createCollection("workouts")
db.users.createIndex({ email: 1 }, { unique: true })}
