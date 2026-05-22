# Job Posting Acceptance Criteria

## Create Job Posting

Given a valid job payload,
When the API receives a POST request,
Then the API returns HTTP 201 Created
And the job is saved to the configured repository backend.

## Get All Jobs

Given jobs exist,
When the API receives a GET request for all jobs,
Then the API returns HTTP 200 OK
And returns a JSON array of jobs.

## Get Job By ID

Given a job exists,
When the API receives a GET request for that job ID,
Then the API returns HTTP 200 OK
And returns the matching job.

## Update Job

Given a job exists,
When the API receives a PUT request with valid fields,
Then the API returns HTTP 200 OK
And the job is updated in the configured repository backend.

## Delete Job

Given a job exists,
When the API receives a DELETE request for that job ID,
Then the API returns HTTP 204 No Content
And the job is removed from the configured repository backend.
