One of the easiest ways to implement a queue in a distributed system for jobs that take several minutes to run and can be run simultaneously is to use a message-queue system such as RabbitMQ or Apache Kafka.

Here is a high-level overview of how you can implement a queue using RabbitMQ:

Set up a RabbitMQ server as a message broker in your distributed system. This will serve as the central hub for managing the queue of jobs.

When a job needs to be added to the queue, a producer application sends a message to a specific queue on the RabbitMQ server. The message should contain all the necessary information for the job to be processed.

Multiple consumer applications can be set up to listen for messages on the queue. When a consumer receives a message, it can start processing the job.

If a job fails during processing, the consumer application should handle the failure appropriately. This may involve retrying the job, logging the failure, and potentially notifying an administrator.

As jobs are completed, the consumer applications can send messages back to the producer application or to another queue to notify of the completion status.

By using a message-queue system like RabbitMQ, you can easily implement a distributed queue that can handle multiple jobs running simultaneously and handle failures gracefully. Additionally, message-queue systems often provide features for tracking message delivery, handling retries, and managing message durability, which can be crucial in a distributed system handling long-running jobs.
