import React, { useEffect, useState } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch('https://probable-disco-p7jqx56prrw2rxj4-8000.app.github.dev/api/workouts/')
      .then(res => res.json())
      .then(data => setWorkouts(data));
  }, []);

  return (
    <div className="card mt-4">
      <div className="card-body">
        <h2 className="card-title mb-4">Workouts</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Type</th>
              <th>Details</th>
              <th>Date</th>
            </tr>
          </thead>
          <tbody>
            {workouts.map(workout => (
              <tr key={workout._id}>
                <td>{workout.workout_type}</td>
                <td>{workout.details}</td>
                <td>{workout.date ? new Date(workout.date).toLocaleString() : ''}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Workouts;
