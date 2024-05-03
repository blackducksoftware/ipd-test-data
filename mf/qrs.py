    def finish_job(self, runner_data):
        """job completed, Update tables accordingly"""
        job_id = runner_data["job"]["job_id"]
        jm_conn = self.dbwrapper.fp_conn()
        #state transition in progress -> 'done'/'failed'
        logger.info("%s job completed, updating status to %s for repo %s", job_id, runner_data["job"]["location"], runner_data["status"])
        repo_updated = orm.update_repo_status(jm_conn, runner_data["job"]["location"], runner_data["status"], orm.status_in_progress)
        if repo_updated:
            orm.update_job_status(jm_conn,job_id,runner_data["status"], attempts=True)
        else:
            logger.warning("Issue updating repo status for %s, skipping job update, leaving in running state...", runner_data["job"]["location"])

        return runner_data["status"]

    def runner_heartbeat(self, job_data):
        """Runner contact -> update job status to in progress"""
        logger.info("Runner is still working on %s", job_data["location"])
        orm.update_job_status(self.dbwrapper.fp_conn(),job_data["job_id"], orm.status_in_progress)
        return job_data
