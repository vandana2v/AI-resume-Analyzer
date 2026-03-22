export default function JobList({ jobs }) {
  return (
    <>
      {jobs.map((job, i) => (
        <div className="job-card" key={i}>
          <h3>{job.title}</h3>
          <p>{job.company}</p>
          <strong>Match: {job.match_score}%</strong>
        </div>
      ))}
    </>
  );
}